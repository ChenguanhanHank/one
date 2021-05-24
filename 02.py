classmate = []
while True:
    student = input('請輸入學生姓名: ')
    if student == 'q':
        break
    gradge = input('請輸入學生成績: ')
    gender = input('請輸入學生性別: ')
    classmate.append([student,gradge,gender])

print(classmate)