def main():

    monthly_sales = get_sales()

    advanced_pay = get_advanced_pay()

    commission_rate = get_commission_rate(monthly_sales)

    monthly_pay = (monthly_sales * commission_rate) - advanced_pay

    if monthly_pay < 0:
        imbursement = abs(monthly_pay)
        print("You must reimburse the company with an amount of $", imbursement)
    else:
        print("Your monthly pay is $", monthly_pay)

def get_advanced_pay():

    while True:
        advance = float(input("Enter advanced pay: "))
        if advance >= 0 and advance <= 2000:
            break
        elif advance > 2000:
            print("Advance pay cannot be greater than $2000")
            continue
    return advance

def get_sales():

    sales = float(input("Enter monthly sales: "))
    return sales

def get_commission_rate(sale):

    if sale < 10000:
        rate = 0.10
    elif sale >= 10000 and sale <= 14999:
        rate = 0.12
    elif sale >= 15000 and sale <= 17999:
        rate = 0.14
    elif sale >= 18000 and sale <= 21999:
        rate = 0.16
    else:
        rate = 0.18
    return rate


main()
