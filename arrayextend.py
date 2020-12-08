import array as arr
numbers = arr.array('i',[1, 8, 5, 10, 12])
numbers.append(4)
print(numbers)
numbers.extend([5, 6, 7])
print(numbers)
numbers.remove(10)
print(numbers)
