import random


class Car:
    def __init__(self):
        self.name = None
        self.date = None
        self.plate_num = None
        self.brand = None
        self.model = None
        self.return_condition = None
        self.return_date = None

    def rent(self):
        self.name = input('Enter your name: ')
        self.date = input('Enter today\'s date: ')
        self.brand = input('Enter the brand you want: ')
        self.model = input('Enter the model you want: ')
        self._license_plate_gen()
        print(f'Here is your license plate: {self.plate_num}')

    def _license_plate_gen(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        self.plate_num = ''.join([random.choice(chars) for i in range(3)] + [random.choice(nums) for i in range(4)])

    def return_car(self):
        self.return_date = input('What is the return date?: ')
        self.return_condition = input('What is the return condition?: ')

        print('\nHere is your receipt:\n')
        self._receipt()

    def _receipt(self):
        print(f'Name: {self.name}')
        print(f'Rent Date: {self.date}')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'License Plate: {self.plate_num}')
        print(f'Return Date: {self.return_date}')
        print(f'Return Condition: {self.return_condition}')
