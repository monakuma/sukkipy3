print('すべての質問にyまたはnで答えてください')

has_money=input('お金に余裕はありますか？')
if has_money=='y':
    is_hangry=input('お腹がすごく空いてますか＞')
    is_drink=input('ビールは飲みたいですか？')
    if is_hangry=='y'and is_drink=='y':
        print('焼き肉はいかがでしょうか。')
    elif is_hangry=='y':
        print('カレーはいかがでしょうか。')
    elif is_drink=='y':
        print('焼き鳥はいかがでしょうか。')
    else:
        print('パスタはいかがでしょうか。')
    is_snack=input('夜食は必要ですか？')
    if is_snack=='y':
        print('コンビニのチキンはいかがでしょうか。')
else:
    print('家で食べましょう')    