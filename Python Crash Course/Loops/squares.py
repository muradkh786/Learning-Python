squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehension example 
squares2 = [values2**2 for values2 in range(1,11)]
print(squares2)