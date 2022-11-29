def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 2, 1))


def calculate(n, **kwargs):
    print((kwargs))

    # for key, value in kwargs.items():
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.modal = kwargs.get("modal")
        self.color = kwargs.get("color")


my_car = Car(make="Nissan", color='red')

print(my_car)
