import random
start = int(input('請輸入最小數字範圍: '))
end = int(input('請輸入最大數字範圍: '))
r = random.randint(start, end)
count = 0
while True:#屬於執行
    count+=1
    user = input('請猜猜看數字:')
    user = int(user)
    
    if user == r:#三而一的if
        print('你猜中了')
        print('這是你猜的第',count,'次')
        break
    elif user<r:
        print('比答案小')
    elif user>r:
       print('比答案大')
    print('這是你猜的第',count,'次')







1


