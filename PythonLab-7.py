#pythonlab7
def count(s):
    upper_count=0
    lower_count=0
    for i in s:
        if i.isupper():
            upper_count+= 1
        elif i.islower():
            lower_count+=1
    return upper_count, lower_count
s=input("Enter string:")
upper_count, lower_count= count(s)
print(f"Count of lowercases: {lower_count}")
print(f"Count of uppercases: {upper_count}")
            
