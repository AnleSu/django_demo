if True:
    print('true')
    print('true')
    print('true')
    print('true')
else:
    print('false')

age = 16
if age > 18:
    print('done')


age = input('age is: ')
if int(age) > 18:
    print('done')
else:
    print('haha')

# 多重判断 elif 就相当于else if
if int(age) > 18:
    print('done')
elif (age >= 18) and (age <= 30): # 18 <= age <= 30
    print('lili')
else:
    print('haha')

# if嵌套

# 猜拳游戏
