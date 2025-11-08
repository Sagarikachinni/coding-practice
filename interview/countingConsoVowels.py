'''#counting conso and vowels
s="hello i'm sagarika"
vowels="aeiouAEIOU"
vow=0
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
cons=0
for i in s:
    if i in vowels:
        vow+=1
    if i in consonants:
        cons+=1
print("the count of vowels  is :",vow)
print("the count of cons  is :",cons)'''