class Pizza():
#описание пиццы
    def __init__(self, size, price):
    #свойства пиццы
        self.size = size
        self.price = price
        self.age = 1
    def display_info(self):
        print("Пицца " + str(self.size) + " cм Готова" + " с вас " + self.price)
    def age_of_pizza(self, day):
        self.age += day
Four_cheese = Pizza(30, "10$")
Four_cheese.display_info()

class ProductsForPizza(Pizza):
    def  __init__(self, meet, meet_size):
        super().__init__(self,meet_size)
        self.meet = meet
        self.meet_size = meet_size
    def display_meets(self):
        print("Вы выбрали " + self.meet + " и указали размер " + str(self.meet_size))

PFP = ProductsForPizza("Ветчина",5)
PFP.display_meets()

