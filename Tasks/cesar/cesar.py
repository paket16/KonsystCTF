
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLow = alphabet.lower()

text = "ncspacekelaeepaketdotruspaceportspacefivefivefivefive"
result =[]
chifer = [9, 8, 8]
j = 0

for i in range(len(text)):
    index = alphabetLow.index(text[i])
    Newindex = index + chifer[j]
    result.append(alphabetLow[Newindex])
    j += 1
    if j > 2: j = 0
    
    
print(result)
#подсказка: имя отца этого человека
#при расшифровке этого сообщения надо загуглить 988 год и на сервервер(0.0.0.0:5555) написать имя отца
#того кто крестил русь т.е. "Святослав" ТРАНСЛИТОМ (Svyatoslav) после этого нам выдаст флаг
#если ввести не то слово то выдаст флаг с рандомным наобором букв