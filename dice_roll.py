import random
dice=[1,2,3,4,5,6]
number_of_dice= input("Enter the number of dice to be rolled ( 1 or 2)")
if number_of_dice == '1':
    print("Rolling...")
    print("The value is ")
    res= random.choice(dice)
    print(res)
else:
    print("Rolling...")
    print("The values are ")
    d1= random.choice(dice)
    d2=random.choice(dice)
    print(d1,d2)

    