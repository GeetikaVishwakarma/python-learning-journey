##Take a character and check if it is a vowel or consonant.

ch=input("enter a character :")
if ch.lower() in "aeiou":
    print("vowel")
else: print("consonant")