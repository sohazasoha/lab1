symbols=0
simv=0
probely=0
zn_prep=0
slova=0
predlozheniya=0
mnogotoch=0
import csv
import re
with open("steam_description_data.csv", encoding='utf-8', newline='')as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        s=','.join(row)
        simv+=len(s)
        mnogotoch+=s.count('...')
        probely+=s.count(' ')
        zn_prep+=s.count(',')+s.count('"')+s.count('-')+s.count('.')+s.count("'")+s.count(':')+s.count(';')+s.count('!')
        zn_prep+=s.count('?')+s.count('...')+s.count('(')+s.count(')')+s.count('[')+s.count(']')
        slova+=len(re.findall(r'\w+',s))
        for i in range(len(s)):       
            if s[i]=='.' or s[i]=='!' or s[i]=='?':
                predlozheniya+=1
print("Количество символов:",simv)
print("Количество символов без пробелов:",simv-probely)
print("Количество символов без знаков препинания:",simv-zn_prep)
print("Количество слов:",slova)
print("Количество предложений:",predlozheniya-2*mnogotoch)

        
