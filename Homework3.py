class ConstructedShark:
    def __init__(self, age):
        self.age = age

def main():
    stevie = ConstructedShark(3)
    print(stevie.age)

if __name__ == "__main__":
    main()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    MyDog = Dog('rexi',5)
    print(MyDog.name)

if __name__ == '__main__':
    main()


class Car:
    @staticmethod
    def start():
        pass


def main():
    Car.start()


class Husky(Dog):
    def howl(self):
        print("ahoo")

def main():
    MyHusky = Husky('rexi',5)
    MyHusky.howl()

if __name__ == '__main__':
    main()

class BlackHusky(Husky):
    def return_color(self):
        return('black')

def main():
    MyDog = BlackHusky('Rexi', 11)
    MyDog.howl()
    print(MyDog.return_color())

if __name__ == '__main__':
    main()


import array as AXX
A = AXX.array("i", [2, 4, 6])
for i in A:
    print(i)

DogList = [Dog("Foxi", 7), Dog("rexi", 8), Dog("Muxy", 99)]
for i in DogList:
    print(i.name)


class Animal:
    def breath(self):
        print("beathing")

class BlackHusky(Husky, Animal):
    pass

def main():
    Breath = BlackHusky("puppy", 1)
    Breath.breath()

if __name__ == '__main__':
    main()

