print('**' * 23)
print('*****RESTAURANT BILL AND TIP CALCULATOR*****')
print('**' * 23)
no_of_friends = float(input('Enter number of friends: '))
bill_amount = float(input('Enter total bill: '))
tip_percentage = float(input('Enter tip percentage: ')) * 0.01

amount_per_person = ((1 + tip_percentage) * bill_amount) / no_of_friends

print('Each person will pay: ', amount_per_person)
