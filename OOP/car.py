class Car(object):

    def __init__(self, model, mileage, manufacture):
        self.model = model
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        if self.manufacture == "Tesla":
            print(f"{self.model} is running out of electricity!! Charge me!")
        else:
            print(f"{self.model} is running out of gas!")

    def brakes(self):
        print(f"{self.mileage}")

if __name__ == "__main__":
    teslaS = Car("ModelS", 312321321, "Tesla")
    ferrari = Car("812Superfast", 4234234, "Ferrari")

    print(teslaS.model)
    print(teslaS.mileage)
    print(teslaS.manufacture)
    teslaS.gas()
    teslaS.brakes()

    print(ferrari.model)
    print(ferrari.mileage)
    print(ferrari.manufacture)
    ferrari.gas()
    ferrari.brakes()
