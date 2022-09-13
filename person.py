from dataclasses import dataclass, field


@dataclass(kw_only=True, frozen=False)  # keyword args 로만 초기화 가능, 객체 생성후 field 변경 불가
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    _search_string: str = field(
        init=False, repr=False
    )  # initializer 에 포함시키지 않음, __repr__ 실행시 field 를 제외함

    def __post_init__(self):  # __init__ 후에 실행됨
        self._search_string = f"{self.name} {self.address}"


person1 = Person(name="sukjun", address="suji")
person2 = Person(name="ricepotato", address="paju")

print(person1)
print(person2)
