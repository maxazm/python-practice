class Car(object):

    def __init__(self, model, mileage, manufacturer):
        self.model = model
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print("{0.manufacturer}の{0.model}（燃費:{0.mileage}）, アクセル全開！".format(self))

    def brakes(self):
        print("{0.manufacturer}の{0.model}（燃費:{0.mileage}）, ブレーキ！".format(self))


class Truck(Car):

    def __init__(self, model, mileage, manufacturer, max_capacity, curr_capacity):
        super().__init__(model=model, mileage = mileage, manufacturer=manufacturer)
        self.max_capacity = max_capacity
        self.curr_capacity = curr_capacity
        print("Truck is called")

    def load(self, kg):
        if self.curr_capacity + kg < 0:
            self.print_info()
            print(f"{self.curr_capacity}kgを超える荷物を下ろすことができません")
        elif self.curr_capacity + kg > self.max_capacity:
            self.curr_capacity += kg
            self.print_info()
            print("最大積載量を超えました")
        else:
            self.curr_capacity += kg
            self.print_info()

    def print_info(self):
        print("現在の積載量は{}kgです".format(self.curr_capacity))

truck = Truck("Big Truck", "14", "TOYOTA", 2000, 1200)
print(truck.max_capacity)
truck.load(100)
truck.load(1000)
truck.load(-10000)