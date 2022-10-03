numbers = [100000]
for _ in range(int(12.5*(10**3)) - 2):
    numbers.append(1)
numbers.append(2)

with open('input12,5K.txt', 'w') as f:
    for num in numbers:
        f.write(str(num) + ' ')
    f.write("\n")