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
a=[]
t=tuple(emp_list1)
c=0
print(t)
for i in range(len(emp_list1)):
    for j in range(1,4):
        #print(c)
        a.append(emp_list1[i][j])
        r=a[c]
        c+=1
        print(r)