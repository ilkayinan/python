name = "ilkay"
surname = "inan"
age = "36"

print(name+surname)
text = "Benim adım "+name+" ve soyadım "+surname+". Yaşım ise "+age+"."
print(text)

print(text[0]) # B
print(text[1]) # e
print(text[-1]) #.

print(text[0:7]) # 0 dan 7 ye kadar 0 ve 7 dahil alır
print(text[6:17])
print(text[:10]) # 0 dan başlar 10 dahil alır
print(text[10:]) # 10 dan başlar sonuna kadar gider

print(text[-20:-1])
print(text[0:30:2]) # 3. parametre artış miktarı

print(text[::2]) # başan sona kadar 2şer atlayarak
print(text[::-1])