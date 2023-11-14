isError=int(input("好きな数字を入力してください。"))

if isError==False and isError<100:
    
    print('何か入力してください、100以下の数字でお願いいたします。')
    
    isError=int(input("100以下の数字を入力してください。"))

elif isError%2==0:
    print(f'あなたの番号は{isError}の偶数で間違いないですか？')
elif isError%2==1:
    print(f'あなたの番号は{isError}の奇数で間違いないですか？')

greeting= str(input("なにか入力してください"))
if 'こんにちは'in greeting:
    print('ようこそ')
elif '景気は？'in greeting:
    print('ぼちぼちです')
elif'さようなら'in greeting:
    print('お元気で！')
else:
    print('どうしました？')

