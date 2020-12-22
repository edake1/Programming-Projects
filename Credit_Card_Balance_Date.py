#! python3

import datetime
import calendar

balance = int(input('Enter Credit Card balance: '))
interest_rate = int(input('Enter interest rate(%): ')) * 0.01
monthly_payment = int(input('Enter monthly credit card payment: '))


today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day
start_date = today + datetime.timedelta(days=days_till_end_month + 1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    try:
        if balance < 0:
            balance = 0
        print(end_date, balance)
    except OverflowError:
        print('SORRY!!! You are in debt for life')

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
