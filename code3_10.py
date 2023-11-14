print('すべての質問にyまたはnで答えてください')

request=input('お金に余裕はありますか？')
if request=='y':
    hungry_question=input('お腹がすごく空いてますか＞')
    drinking_question=input('ビールは飲みたいですか？')
    if hungry_question=='y'and drinking_question=='y':
        print('焼き肉はいかがでしょうか。')
    elif hungry_question=='y':
        print('カレーはいかがでしょうか。')
    elif drinking_question=='y':
        print('焼き鳥はいかがでしょうか。')
    else:
        print('パスタはいかがでしょうか。')
    midnight_snack=input('夜食は必要ですか？')
    if midnight_snack=='y':
        print('コンビニのチキンはいかがでしょうか。')
else:
    print('家で食べましょう')    