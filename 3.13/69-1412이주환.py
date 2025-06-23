class Car:
    def __init__(self, displ, drv):
        self.displ = displ
        self.drv = drv
    def getCar(self):
        print(f'자동차 정보 : {self.displ}, {self.drv}구동')
    
my_car = Car(3000, "4륜")
my_car.getCar()
