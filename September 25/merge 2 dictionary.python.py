# write a python program to merge python dictionaries using copy() and update()..

print("MERGING OF 2 DICTIONARY")

dict1={"name":"sandra","age":20,"place":"kkm"}
print(dict1)
dict2={"studying":"mca","college":"mes"}
print(dict2)

dict3=dict1.copy()
dict3.update(dict2)
print("Dictionaries after merging:",dict3)
