sum = 0
while (num := int(input())) and num > 0:
    sum += num if num > 0 else 0
    if sum > 23:
        print(sum)
        break
else:
    print(num)
