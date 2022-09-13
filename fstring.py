"""fstring.. formatting..
https://youtu.be/Mfmr_Puhtew
"""
import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


def main():
    number = 12
    hello = "hello"
    world = "world!"

    print(f"The number is {number:o}")  # 8진수 출력
    print(f"The number is {number:x}")  # 16 진수로 출력
    print(f"The number is {number:03}")  # 0 을 왼쪽에 채우고 3자리수로 출력
    print(f"The number is {3.23341:.2f}")  # 소수점 두자리까지 출력
    print(f"The number is {1356000000:,.2f}")  # 3자리로 끊어 , 붙여줌
    print(f"The number is {.0343412:.2%}")  # 백분율 소수점 둘째자리까지 표시

    print(f"The number is {100:3}")  # 자리수 맞춰 출력
    print(f"The number is {13:3}")  # 자리수 맞춰 출력
    print(f"The number is {6:3}")  # 자리수 맞춰 출력

    print(f"{hello:>10}")  # 10 자리에 맞에 앞에 공백 추가
    print(f"{world:>10}")

    print(f"{hello:_>10}")  # 10 자리에 맞에 앞에 '_' 추가

    print(f"{hello:^10}world")  # 10 자리의 가운데 출력되게 양쪽에 공백 추가
    print(f"{hello:_^10}world")  # 10 자리의 가운데 출력되게 양쪽에 _ 추가

    user = User("sukjun", "sagong")
    print(f"User: {user}")
    print(f"User: {user!r}")  # repr 메소드 결과 출력
    print(f"User: {repr(user)}")  # repr 메소드 결과 출력

    today = datetime.datetime.now()
    print(f"simple date printing {today}")
    print(f"date printing datetime {today:%Y-%m-%d %H:%M:%S.%f}")  # 날짜 형식 출력
    print(
        f"date printing datetime {today:%y-%m-%d %H:%M:%S.%f}"
    )  # 위 출력과 같지만 년도를 두자리로 출력
    print(f"date printing datetime %X {today:%X}")  # 간단 출력 현재 locale
    print(f"date printing only time {today:%H:%M:%S.%f}")  # 시간만 출력
    print(f"date printing only time {today:%T}")  # 시간만 출력
    print(f"today is {today:%A}")  # 요일 출력
    print(f"today is {today:%A, %B %d, %Y}")  # 요일 출력

    dictionary = {"hello": "world"}
    print(f"hello, {dictionary['hello']}")  # dict 를 사용하는 경우

    x = 33
    y = 22
    print(f"{x = } {y=}")  # x = 33 y=22


if __name__ == "__main__":
    main()
