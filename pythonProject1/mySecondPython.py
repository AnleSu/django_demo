password = input('请输入密码：')
print(f'password is {password}')
print(type(password)) # <class 'str'>


# 数据类型转换
print(type(int(password))) # <class 'int'>
num1 = 1
print(float(num1))

list1 = [10, 20]
print(tuple(list1))

t1 = (10, 30, 50)
print(list(t1))

# eval() 字符串中有效的python表达式 并返回一个对应的对象 转换成原本的类型
str1 = '1'
print(type(eval(str1))) # <class 'int'>

# 交互式开发环境 Python Console IDE左下角

