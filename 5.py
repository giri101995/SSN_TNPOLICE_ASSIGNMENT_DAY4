##################################Dictionary#########################################
m=int(input('Enter the number of emplyees'))
n=int(input('Enter the number of infomation fields'))
emp_list=[]
emp_list1=[]
for i in range(m):
    print('Enter the details of next employee with each entry followed by enter in the following order #Name #Age #Designation #Salary')
    for j in range(n):
        str1=input()
        emp_list.append(str1)
print(emp_list)
emp_list1=[emp_list[i:i+n] for i in range(0,len(emp_list),n)]
print(emp_list1)

############################################################################
emp_dic={}
for k in range(m):
    key1=input('Enter the complaint number')
    emp_dic[key1]=emp_list1[i]
print(emp_dic)