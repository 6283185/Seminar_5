# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


txt = "съешь абвещё этих мягких франабвцузских булок, даабв выпей чаю"

def del_some_words(txt):
    # txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    txt = [i for i in txt.split() if 'абв' not in i]
    return " ".join(txt)

txt = del_some_words(txt)
print(txt)