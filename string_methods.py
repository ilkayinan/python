
yazi ="benim adım ilkay inan. izmir'de yaşıyorum."

sonuc = yazi.upper() # bütün harfleri büyük yapar
sonuc = yazi.lower() # bütün harfleri küçük yapar
sonuc = yazi.title() # kelimelerin ilk harflerini büyütür
sonuc = yazi.capitalize() # cümlenin ilk harfini büyük harf olarak değiştirir
sonuc = yazi.islower() # bütün harfleri küçük mü
sonuc = yazi.isupper() # bütün harfleri büyük mü
sonuc = yazi.strip() # başındaki ve sonundaki boşlukları ortadan kaldırır
sonuc = yazi.split() # boşlukları baz alarak bölme işlemi yapar dizi döndürür
sonuc = yazi.split(".") # noktaları baz alarak bölme işlemi yapar dizi döndürür

sonuc = "-".join(yazi) # her karakterin arasına - koyar herhangi bir şey koyabilirsin
sonuc = yazi.index("ilkay") # karakterin geçip geçmediğini kontrol eder kaçıncı indexten itibaren olduğunu döndürür
sonuc = yazi.startswith("b") # o karakterle mi başlıyor diye sorar büyük küçük harfe duyarlı
sonuc = yazi.startswith("a")
sonuc = yazi.endswith(".")

sonuc = yazi.replace("izmir","ankara") # değiştirir
sonuc = yazi.replace("ı","i").replace("ş","s")

print(sonuc)
# w3school kullanabilirsin