import random
num = int(input())
test_set = [random.randint(1,100) for _ in range(9)]
test_set.append(num)
random.shuffle(test_set)
print(test_set)
