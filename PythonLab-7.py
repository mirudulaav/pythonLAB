#pythonlab7
a=input("Enter the required string:")
a.count(a)
def count(a):
    upper=0
    lower=0
    for i in a:
        if i.isupper():
            upper+= 1
        elif i.islower():
            lower+=1
            
print(f"Count of lowercases: {lower}")
print(f"Count of uppercases: {upper}")
            
