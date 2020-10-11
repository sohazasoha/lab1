import re

3points=0
symbols=0
spaces=0
punctuation=0

words=0
sentences=0

with open("steam_description_data.csv", encoding='utf-8', newline='')as f:
    for s in f:
        symbols+=len(s)
        
        3points+=s.count('...')
        
        spaces+=s.count(' ')

        punctuation+=s.count(',')+s.count('"')+s.count('-')+s.count('.')+s.count("'")+s.count(':')+s.count(';')+s.count('!')

        punctuation+=s.count('?')+s.count('...')+s.count('(')+s.count(')')+s.count('[')+s.count(']')

        words+=len(re.findall(r'\w+',s))

        if '.!?' in s:
            sentences+=1



print("Количество символов:",symbols)
print("Количество символов без пробелов:",symbols-spaces)
print("Количество символов без знаков препинания:",symbols-punctuation)
print("Количество слов:",words)
print("Количество предложений:",sentences-2*3points)

        
