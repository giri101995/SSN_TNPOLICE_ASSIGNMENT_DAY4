######################################################################################
list1=[]
list2=[]
for i in range(5):
    print('Enter the name of 5 Employees in list1')
    str1=input()
    list1.append(str1)
print(list1)

for i in range(5):
    print('Enter the name of 5 Employees in list2')
    str2=input()
    list2.append(str2)
print(list2)

list_new=list1+list2

print(list_new)

emp_dic={}
for k in range(10):
    key1=k
    emp_dic[key1]=list_new[k]
print(emp_dic)