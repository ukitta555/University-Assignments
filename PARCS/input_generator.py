numbers = [100000]
for _ in range(int(2.5*(10**3)) - 2):
    numbers.append(1)
numbers.append(2)

with open('input2,5K.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + ' ')
    f.write("\n")
    f.write("100002")