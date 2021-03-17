import math


# Z1
def area(radius):
    return radius**2 * math.pi

radius = int(input().strip())
print(area(radius))


# Z2
def bond_greeting(name):
    names = name.split()
    if len(names) == 2:
        return "{}. {} {}".format(names[1], names[0], names[1])
    return "{}. {} {} {}".format(names[2], names[0], names[1], names[2])


print(bond_greeting("Marijan Smetko"))
print(bond_greeting("Kolinda Grabar Kitarović"))


# Z3
def remove_extension(filename):
    start = filename.rfind("/")
    end = filename.rfind(".")
    if end == -1:
        print("Nema ekstenzije.")
    else:
        return filename[start+1:end]

print(remove_extension("sibirski_plavac.prvi_dio.mp4"))
print(remove_extension("/home/User/Desktop/homework/sibirski_plavac.prvi_dio.mp4"))


# Z4
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_palindrome_stupid(s):
    s = s.replace(" ", "").lower()
    i = 0
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True

print(is_palindrome("aba"))
print(is_palindrome("A mene tu ni minute nema"))
print(is_palindrome("Ana voli Milovana"))
print(is_palindrome("Ana voli Milovane"))
print(is_palindrome_stupid("aba"))
print(is_palindrome_stupid("A mene tu ni minute nema"))
print(is_palindrome_stupid("Ana voli Milovana"))
print(is_palindrome_stupid("Ana voli Milovane"))


# Z5
def is_leap_year(year):
    year = int(year)
    x = year % 4
    y = year % 100
    z = year % 400
    if x == 0 and (y != 0 or z == 0):
        return True
    return False

print(is_leap_year("2020"))
print(is_leap_year("2000"))
print(is_leap_year("1900"))


# Z6
def easter(year):
    year = int(year)

    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8*b + 13) // 25
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 19*l) // 433
    month = (h + l - 7*m + 90) // 25
    day = (h + l - 7*m + 33*month + 19) % 32

    return "{}.{}.{}".format(day, month, year)

print(easter(1998))
print(easter(2009))
print(easter(2020))


# Z7
def read_write(fileR, fileW):
    lista = []
    with open(fileR, "r") as file:
        for line in file:
            lista.append(line.replace("\n", ""))
    
    with open(fileW, "w") as file:
        for s in lista:
            file.write(s + " ")

read_write("a.txt", "b.txt")


# Z8
def find_max(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def most_appearances(fileR, fileW):
    words = {}
    with open(fileR, "r") as file:
        for line in file:
            line = line.strip()
            if line in words.keys():
                words[line] = words[line] + 1
            else:
                words[line] = 1
    top_words = {}
    x = len(words) if len(words) < 5 else 5
    for i in range(x):
        s = find_max(words)
        top_words[s] = words[s]
        words.pop(s)
    
    with open(fileW, "w") as file:
        for word, count in top_words.items():
            file.write("{} {}\n".format(word, count))

most_appearances("a.txt", "b.txt")


# Z9
def fermat(n):
    return 2**(2**int(n))-1

print(fermat(1))
print(fermat(2))
print(fermat(3))


# Z10
def is_prime(n):
    n = int(n)
    if n <= 1:
        return False
    i = 2
    while (i <= n/2):
        if (n % i == 0):
            return False
        i += 1
    return True

print(is_prime(1))
print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(13))
print(is_prime(37))
print(is_prime(101))
print(is_prime(4))
print(is_prime(25024))


# Z11
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def coprime(a, b):
    return gcd(a, b) == 1

def cezar_encrypt(word, a, b):
    if coprime(a,26) == False:
        print("Coefficient a of the affine encryption function must be coprime with the alphabet size (26)!")
        return
    word = word.upper()
    result = ""
    for letter in word:
        code = (a*(ord(letter)-65)+b)%26 + 65
        result += chr(code)
    return result

def cezar_decrypt(word, a, b):
    if coprime(a,26) == False:
        print("Coefficient a of the affine encryption function must be coprime with the alphabet size (26)!")
        return
    word = word.upper()
    result = ""
    for letter in word:
        code = pow(a, -1, 26)*((ord(letter)-65-b))%26 + 65
        result += chr(code)
    return result

#x = cezar_encrypt("ZADAR", 1, 3)
#y = cezar_encrypt("INCOGNITO", 1, 3)
#z = cezar_decrypt(x, 1, 3)
#w = cezar_decrypt(y, 1, 3)
x = cezar_encrypt("ZADAR", 3, 1)
y = cezar_encrypt("INCOGNITO", 3, 1)
z = cezar_decrypt(x, 3, 1)
w = cezar_decrypt(y, 3, 1)
print("ZADAR->{}->{}".format(x, z))
print("INCOGNITO->{}->{}".format(y, w))
