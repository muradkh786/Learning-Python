pizzas = ['cheese', 'jalapeno', 'chicken']
for pizza in pizzas:
    print("I like to eat " + pizza + " pizza.\n")

print("I really love pizza!")

print('\n')

my_friends_pizzas = pizzas[:]

pizzas.append('buffalo')

my_friends_pizzas.append('pineapple')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print('\n')

print("My friends favorite pizzas are:")
for pizza in my_friends_pizzas:
    print(pizza)