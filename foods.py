my_foods = ['daal', 'aloo gobi', 'pizza', 'french fries', 'chicken sammich', 'falafel', 'zaatar bread', 'rice', 'chicken']
friends_foods = my_foods[:]

print("The first three items in the list are:")
for food in my_foods[:3]:
    print(food)

middleIndex = int(len(my_foods) / 2)
print('\n')

print("Three items in the middle are: ")
for food in my_foods[middleIndex-1:middleIndex+2]:
    print(food)

print('\n')

print("The last three items in the list are: ")
for food in my_foods[len(my_foods)-3:]:
    print(food)