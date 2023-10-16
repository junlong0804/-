import random
from itertools import permutations

# 产生随机的五个数字
random_numbers = random.sample(range(10), 5)

# 产生所有可以排列成五位数的数字序列
permutations_list = list(permutations(random_numbers, 5))

# 转换为整数
five_digit_numbers = [int(''.join(map(str, p)) ) for p in permutations_list]

# 找出最大值和最小值
max_value = max(five_digit_numbers)
min_value = min(five_digit_numbers)

print("隨機抓出五位數:", random_numbers)
print("所有可以排成五位數數字的數列:")

# 输出每行最多10个数字
for i, num in enumerate(sorted(five_digit_numbers), start=1):
    print(num, end="\t")  # 使用制表符分隔数字
    if i % 10 == 0:
        print()

print(f"\n最大值: {max_value}")
print(f"最小值: {min_value}")
# 判断哪些数字是质数
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

prime_numbers = [num for num in five_digit_numbers if is_prime(num)]

if prime_numbers:
    print("五位數中的質數有:")
    for i, prime in enumerate(sorted(prime_numbers), start=1):
        print(prime, end="\t")
        if i % 10 == 0:
            print()
else:
    print("五位數中没有質數。")
