text = input("Give me string: ")
s = text.replace(" ", "")
i = 0
x = len(s)
print("Reversed: "+ s[::-1])

if s[0:] == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")