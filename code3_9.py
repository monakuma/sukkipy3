score=int(input('試験の点数を入力してください'))
if score<0 or score>100:
    print('異常な得点です')
    print('入力しなおして下さい')
elif score>=60:
    print('合格！')
    print('よくがんばりました')

else:
    print('残念ながら不合格です')
    print('追試をうけてください')
# day=[28,30,31]
#     initial=='k'
#     80<=point and point<256

#     bmi<20 or bmi>25
#     year%4==0
#     not(day in day)