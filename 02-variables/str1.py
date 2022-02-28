#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych
# znaków danego ciągu.

myStr = "012345678"
center = len(myStr)//2

print("\nTest string: ", myStr)
print("Middle three:", myStr[center-1:center+2])
