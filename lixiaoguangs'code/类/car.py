class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 521

    def update_odometer(self,mileage):
        """将里程表设置成指定的值
        禁止将里程表往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading += miles
              
    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
          #里程值变成可以修改的
    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it")
class Battery():
    """模拟电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        mag = "THIS CAR CAN GO APPROXIMATELY" + str(range)
        msg += "miles on a full charge."
        print(msg)
    
        #开始继承
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
    #super().__init__
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+ str(self.battery_size) + "-kwh battery")
    def fill_gas_tank():
        """电动车没有邮箱"""
        print("This car doesn;t need a gas tank!")
    def mine(self):
        print("I want to buy a tesla medel 3, but I have no money!")
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            battery_size = 85
my_tesla = ElectricCar('tesla','medel s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.upgrade_battery()
my_tesla.battery.get_range()


#电瓶升级


