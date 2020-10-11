import re

points3 = 0
symbols = 0
spaces = 0
punctuation = 0
words = 0
sentences = 0
punct_symb = '\"-\'!.?\)\(,:;...]['

with open('steam_description_data.csv', encoding='utf-8', newline='')as f:
    for s in f:
        symbols += len(s)
        spaces += s.count(' ')
        for symb in punct_symb:
            punctuation+= s.count(symb)
        words += len(re.findall(r'\w+', s))
        sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", s))
        
print('Количество символов:', symbols)
print('Количество символов без пробелов:', symbols-spaces)
print('Количество символов без знаков препинания:', symbols-punctuation)
print('Количество слов:', words)
print('Количество предложений:', sentences)
