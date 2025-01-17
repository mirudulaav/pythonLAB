#9
my_dict = {'a': 10, 'b': 20, 'c': 30}
total_sum=sum(my_dict.values())
print("Sum of all items:", total_sum)

#10
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
