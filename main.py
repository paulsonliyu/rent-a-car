from car import Car


def main():
    print('Welcome to Rent-A-Car!')
    renter = Car()
    while True:
        print('\nWhat would you like to do?')
        print('1. Rent a car\n2. Return a car\n3. Quit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            renter.rent()
        elif choice == 2:
            renter.return_car()
        elif choice == 3:
            quit()


if __name__ == '__main__':
    main()
