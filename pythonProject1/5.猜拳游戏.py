# 随机数
import random

player = int(input('0 -- 石头； 1 -- 剪刀； 2 -- 布：'))
computer = random.randint(0,2) # 0 - 2之间的随机数
print(f'computer = {computer}')

if ((player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0)):
    print('player success!')
elif player == computer:
    print("equal")
else:
    print('computer success!')