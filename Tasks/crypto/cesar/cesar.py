
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
#���������: ��� ���� ����� ��������
#��� ����������� ����� ��������� ���� ��������� 988 ��� � �� ���������(0.0.0.0:5555) �������� ��� ����
#���� ��� ������� ���� �.�. "���������" ���������� (Svyatoslav) ����� ����� ��� ������ ����
#���� ������ �� �� ����� �� ������ ���� � ��������� �������� ����