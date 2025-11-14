list1 = input().split()
list1 = [int(x) for x in list1]

list2 = input().split()
list2 = [int(x) for x in list2]

print(len(list1) == len(list2))         # (a) same length
print(sum(list1) == sum(list2))         # (b) same sum
print(any(x in list2 for x in list1))   # (c) any common value
