### Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

a = "Osman" #string: metinler için kullanılır.
b = 123 #int: tam sayılar için kullanılır.
c = 12.5 #float: ondalıklı sayılar için kullanılır.
d = 1j #complex: karmaşık sayılar için kullanılır.
e = ["Osman", "Kagan", "Kurnaz"]  # list: verileri listelemek için kullanılır.
f = (
    "Osman",
    "Kagan",
    "Kurnaz",
) #tuple: verileri listelemek için kullanılır fakat değiştirilemez.
g = {
    "name": "Osman",
    "surname": "Kurnaz",
} #dictionary: anahtar - değer yapısında verileri kullanmamızı sağlar.
h = True #boolean: true ve false değerlerini alabilen bir veri türüdür.


### Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#Sitede bulunan tüm metinsel ifadeler string veri tipinde olabilir.
#Navigation barda bulunan itemlar bir listeden döndürülüyor olabilir.
#Sık sorulan sorular bölümündeki soruların ve cevapların verileri dictionaryde tutuluyor olabilir.

### Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#Giriş yaparken veri tabanında bulunan eposta - şifre çiftleri sorgulanıyor. Sorgulama sonucu giriş yapmaya çalışan kişinin girdiği bilgiler doğruysa giriş yapabiliyor.

mail = "osman"
password = "111"

while True:

    user_mail = input("Email adresinizi giriniz:")
    user_password = input("Sifrenizi giriniz:")

    if user_mail == mail and user_password == password:

        print("Giris basarili...")
        break

    else:
        
        print("Girdiginiz bilgiler hatalidir. Tekrar giriş yapmayı deneyiniz...")