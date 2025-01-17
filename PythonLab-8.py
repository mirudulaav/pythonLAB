#8 PALINDROME
text = input("Enter a string: ")
reversed_text = text[::-1]

if text == reversed_text:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")

print("Reversed string: ", reversed_text)
