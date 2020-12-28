import random

r = random.randint(1,100)

while True:#屬於執行
    user = input('')
    user = int(user)
    
    if user == r:
        print('你猜中了')
        break
    elif user<r:
        print('比答案小')
    elif user>r:
       print('比答案大')









