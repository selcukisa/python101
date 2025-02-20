numbers = [1 , 2 , 8 , 10 , 7 , 11 , 9 ]
letters =  ["a", "g" , "b", "c" ,"d" ,"f" ,"s"]

result = min(numbers)
result = max(numbers)
result= min(letters)
result = max(letters)

result = numbers[2:5]

#numbers[2]= 15
result= numbers

# numbers.append(49)
# numbers.insert(3,78)
# numbers.insert(-1, 52)
# numbers.pop()
# numbers.remove(52)

numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()




print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(5))
print(letters.count("a"))

numbers.clear()
print(numbers)

