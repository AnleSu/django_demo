# while循环
i = 1
result = 0
while i <= 100:
    result += i
    i += 1

print(f'{result}')

i = 1
result = 0
while i <= 100:
    if i % 2 == 0: # 加偶数
        result += i
    i += 1
print(f'{result}')

i = 0
result = 0
while i <= 100:
    result += i
    i += 2 # 计数器控制加偶数
print(f'{result}')

'''
*
**
***
****
*****
'''
j = 0
while j < 5:
    i = 0
    while i < j + 1:
        print('*', end='\t')
        i += 1
    print()
    j += 1

# 99乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i * j}', end='\t') #用\t对齐
        i += 1
    print()
    j += 1


# for循环
str1 = 'itheima'
for i in str1:
    print(i)