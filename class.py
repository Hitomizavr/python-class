class Transport(object):
    # конструктор
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создаем объект класса Transport
autobus = Transport("Автобус ЛиАЗ-5292", 65, 5250)

print("Название автомобиля:", autobus.name, 
"Максимальная скорость:", autobus.max_speed, "км/ч.",
"Пробег:", autobus.mileage, "км/ч.");