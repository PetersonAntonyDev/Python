frase = str(input('Digite uma frase ou uma palavra qualquer: '))
''.join(frase)
v = frase.count('a')
va = frase.count('á')
va2 = frase.count('à')
va3 = frase.count('ã')
va4 = frase.count('â')
v2 = frase.count('e')
ve = frase.count('é')
ve2 = frase.count('ê')
v3 = frase.count('i')
vi = frase.count('í')
v4 = frase.count('o')
vo = frase.count('ó')
vo2 = frase.count('ô')
vo3 = frase.count('õ')
v5 = frase.count('u')
vu = frase.count('ú')
totalv = v + v2 + v3 + v4 + v5 + va + va2 + va3 + va4 + ve + vi + vo + vo2 + vo3 + vu
print(f'A frase possui {totalv} vogal/vogais.')
a = frase.split()
b = ''.join(a)
c = len(b)
totalc = c - totalv
print(f'A frase possui {totalc} consoate(s).')