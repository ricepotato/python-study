import pydantic


class BWListCreate(pydantic.BaseModel):
    value: str
    type: str
    source: str

    class Config:
        orm_mode = True

    def __hash__(self):
        return hash((self.source, self.value))

    def __eq__(self, other):
        return (self.value == other.value) and (self.source == other.source)


class BWList(BWListCreate):
    id: int

    class Config:
        orm_mode = True

    def __hash__(self):
        return hash((self.source, self.value))

    def __eq__(self, other):
        if self.id == other.id:
            return True

        return (self.value == other.value) and (self.source == other.source)


class HashableBase(pydantic.BaseModel):
    type: str
    value: str

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __hash__(self):
        return hash((self.value, self.type))


class Hashable1(pydantic.BaseModel):
    type: str
    value: str

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __hash__(self):
        return hash((self.value, self.type))


class Hashable2(pydantic.BaseModel):
    type: str
    value: str
    metadata: dict

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def __hash__(self):
        return hash((self.value, self.type))


class HashableChild1(HashableBase):
    pass


class HashableChild2(HashableBase):
    metadata: dict


def test_remove_dup():
    set1 = {1, 2, 3, 4}
    set2 = {2, 3}

    new_set = set1 - set2
    assert len(new_set) == 2
    assert 1 in new_set
    assert 4 in new_set


def test_bwlist_hashable():
    bw1 = BWList(
        id=1,
        value="0x45eb6d727fb8c1eb89284b65d336f2c6bcba0f73",
        type="address",
        source="bicscan",
        score=0,
        author="bicscan admin",
        description="bicscan whitelist",
    )

    bw2 = BWList(
        id=2,
        value="0x45eb6d727fb8c1eb89284b65d336f2c6bcba0f73",
        type="address",
        source="bicscan",
        score=50,
        author="bicscan admin",
        description="bicscan whitelist",
    )

    bw_list = [bw1, bw2]
    bw_set = {v for v in bw_list}
    assert bw_set
    assert len(bw_set) == 1


def test_hashable_set_remove_dup():
    set1 = set(
        [
            Hashable1(type="address", value="0x1234"),
            Hashable1(type="address", value="0x1235"),
            Hashable1(type="address", value="0x1236"),
        ]
    )

    set2 = set(
        [
            Hashable2(type="address", value="0x1234", metadata={}),
            Hashable2(type="address", value="0x1235", metadata={}),
            Hashable2(type="address", value="0x1237", metadata={}),
            Hashable2(type="address", value="0x1238", metadata={}),
        ]
    )

    result = set1 - set2
    assert len(result) == 1
    assert next(iter(result)).value == "0x1236"

    result = set2 - set1
    assert len(result) == 2

    assert "0x1237" in [r.value for r in result]
    assert "0x1238" in [r.value for r in result]


def test_hashable_set_remove_dup_child():
    set1 = set(
        [
            HashableChild1(type="address", value="0x1234"),
            HashableChild1(type="address", value="0x1235"),
            HashableChild1(type="address", value="0x1236"),
        ]
    )

    set2 = set(
        [
            HashableChild2(type="address", value="0x1234", metadata={}),
            HashableChild2(type="address", value="0x1235", metadata={}),
            HashableChild2(type="address", value="0x1237", metadata={}),
            HashableChild2(type="address", value="0x1238", metadata={}),
        ]
    )

    result = set1 - set2
    assert len(result) == 1
    assert next(iter(result)).value == "0x1236"

    result = set2 - set1
    assert len(result) == 2

    assert "0x1237" in [r.value for r in result]
    assert "0x1238" in [r.value for r in result]


def test_hashable_type():
    set1 = {
        1,
        2,
        3,
        4,
        BWList(
            id=1,
            value="0x45eb6d727fb8c1eb89284b65d336f2c6bcba0f73",
            type="address",
            source="bicscan",
            score=0,
            author="bicscan admin",
            description="bicscan whitelist",
        ),
    }
    set2 = {2, 3}

    new_set = set1 - set2
    assert len(new_set) == 3
    assert 1 in new_set
    assert 4 in new_set
