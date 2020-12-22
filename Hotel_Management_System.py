import datetime


class hotel_manage:
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1000, name='', address='', cindate='', coutdate='', room_no=1):
        print("\n\n********WELCOME TO HOTEL TRANSYLVANIA********")
        self.rt = rt
        self.s = s
        self.p = p
        self.r = r
        self.t = t
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.room_no = room_no

    def input_data(self):
        self.name = input('\nEnter your full name: ')
        self.address = input('\nEnter your address: ')
        self.cindate = input('\nEnter your check in date (YYYY-MM-DD): ')
        self.coutdate = input('\nEnter your check out date (YYYY-MM-DD): ')
        a = datetime.date.fromisoformat(self.cindate)
        b = datetime.date.fromisoformat(self.coutdate)
        duration = str(b - a)
        global dur
        dur = duration.split(',')[0]
        print('Your room no: ', self.room_no, '\n')

    def room_rent(self):
        print('We have the following rooms for you:-')
        print('1.   Class A----->10000')
        print('2.   Class B----->8000')
        print('3.   Class C----->6000')
        print('4.   Class D----->4000')

        x = int(input('Please enter the number of your choice----->'))
        n = int(input('For how many nights did you stayL----->'))

        if x == 1:
            print('You have chosen a Class A room')
            self.s = 10000 * n
        elif x == 2:
            print('You have chosen a Class B room')
            self.s = 8000 * n
        elif x == 3:
            print('You have chosen a Class C room')
            self.s = 6000 * n
        elif x == 4:
            print('You have chosen a Class D room')
            self.s = 4000 * n
        else:
            print('PLEASE CHOOSE A ROOM')
        print('Your chosen room rent is', self.s, '\n')

    def food_purchased(self):
        print('********RESTAURANT MENU********')
        print('1.Dessert----->100', '2.Drinks----->50', '3.Breakfast----->90', '4.Lunch----->120', '5.Dinner----->180', '6.EXIT')

        while True:
            c = int(input('Enter the number of your choice: '))

            if c == 1:
                d = int(input('Enter the quantity: '))
                self.r += 100 * d
            elif c == 2:
                d = int(input('Enter the quantity: '))
                self.r += 50 * d
            elif c == 3:
                d = int(input('Enter the quantity: '))
                self.r += 90 * d
            elif c == 4:
                d = int(input('Enter the quantity: '))
                self.r += 120 * d
            elif c == 5:
                d = int(input('Enter the quantity: '))
                self.r += 180 * d
            elif c == 6:
                break
            else:
                print('You have entered an invalid key')

        print('Total food cost= Gh', self.r, '\n')

    def hotel_bill(self):
        print('********HOTEL BILL********')
        print('Customer details:')
        print('Customer name: ', self.name)
        print('Customer address: ', self.address)
        print('Check in date: ', self.cindate)
        print('Check out date: ', self.coutdate)
        print('Room no.', self.room_no)
        print(f'You spent {dur} at Hotel Transylvania')
        print('Your room rent is:', self.s)
        print('Your food bill is:', self.r)

        self.rt = self.s + self.t + self.p + self.r

        print('Your sub total purchased is:', self.rt)
        print('Additional Service Charges is:', self.a)
        print('Your Grandtotal purchased is:', self.rt + self.a, '\n')
        self.room_no += 1

    def main():
        a = hotel_manage

        while True:
            print('1.   Enter Customer Data')
            print('2.   Calculate Room Rent')
            print('3.   Calculate Food Purchased')
            print('4.   Show Total Cost')
            print('5.   EXIT')

            b = int(input('\nEnter the number of your choice: '))

            if b == 1:
                a.input_data()

            elif b == 2:
                a.room_rent()

            elif b == 3:
                a.food_purchased()

            elif b == 4:
                a.hotel_bill()

            elif b == 5:
                quit()
        if __name__ == '__main__':
            main()


emp = hotel_manage()
emp.input_data()
emp.room_rent()
emp.food_purchased()
emp.hotel_bill()
emp.main
