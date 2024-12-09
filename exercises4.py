def reverse_string(text):
    reversed_text = []              # 空のリストを作成
    for char in text:              # 文字列を1文字ずつ処理
        reversed_text.append(char)  # 各文字をリストに追加
    reversed_text = list(reversed(reversed_text))  # リストを反転（reversedを使用）
    result = ''.join(reversed_text)  # リストの文字を結合して文字列に変換
    return result                    # 反転した文字列を返す

print(reverse_string("Hello World")) # "dlroW olleH"
print(reverse_string("Python")) # "nohtyP"