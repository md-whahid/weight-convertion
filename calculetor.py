weight = int(input('Enter your weighht : '))

weight_type = input("Type 'kg' or 'lbs' ")

if weight_type.lower() == 'kg':
    lbs = weight * 2.2
    print(f'Your weight is {lbs} pound')

elif weight_type.lower() == 'lbs':
    kg = weight / 2.2
    print(f'Your weight is {kg} kg')

else:
    print('You did something wrong..!')
