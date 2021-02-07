print("hi world")

# 注释内容

"""
    多行注释
"""

'''
    多行注释
'''

# 变量 命名规则 大小驼峰 下划线 关键词
my_name = 'Tom' # 解释器解释出'Tom'的类型
print(my_name)

# 数据类型
num1 = 1 # Int
num2 = 1.1 # float
print(type(num2))
print(type(my_name)) # str

b = True
print(type(b)) # bool

c = [10, 40, 50] # list
print(type(c))

d = (10, 20, 30) # tuple
print(type(d))

e = {10, 20, 30} # set
print(type(e))

f = {'name':'tom', 'address':'beijin'} # dict
print(type(f))

# 输出  格式化符号
age = 10
name = 'tom'
weight = 60.9
stu_id = 12

# %连接变量 有没有空格都可以
print('age is %d' % age)
print('name is %s' % name)
print('weight is %.2f' % weight)
# %06d 整数6位不够补零 超出的原样输出
print('id is %03d' % stu_id) # id is 012
print('age is %d name is %s' % (age, name)) # 输出两个变量

print('明年 age is %d name is %s'% (age + 1, name))

# %s 功能比较强大
print('明年 age is %s name is %s weight is %s' % (name, age, weight))

# f'{}'  语法更简洁高效 python3.6新增
print(f'明年 age is {age} name is {name} weight is {weight}')

# 转义字符

# 结束符号
print('hello', end="\t")
print('python', end="...")

