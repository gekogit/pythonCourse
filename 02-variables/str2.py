#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "Computer"
s2 = "Human"
s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]

print("\ns1:", s1)
print("s2:", s2)
print("s3 --> s2 inside s1:", s3)
