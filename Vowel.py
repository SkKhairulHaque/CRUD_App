# Vowel Or Consonat:
x=(input("Enter a character:"))
if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
else:
        print("Consonant")
if((x>='A'and x<='Z') or (x>='a' and x<='z')):
    if x in "aeiouAEIOU":
        print("It's a Vowel")
    else:
        print("It's a consonanat")
else:
    print("Others")