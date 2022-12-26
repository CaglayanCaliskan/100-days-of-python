age: int
name: str


def police_check(age: int) -> bool:
    if age > 18:
        check = True
    else:
        check = False
    return check


if police_check(age=1):
    print("yes go on")
else:
    print("stop stop")
