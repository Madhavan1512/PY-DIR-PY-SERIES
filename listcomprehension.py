numbers = [1,2,3,4,5,6,7,8]
even = []
for i in numbers: # can also be written as even = [i for i in numbers if i % 2 == 0]
    if i % 2 == 0:
        even.append(i)
print(even)
print(numbers)
