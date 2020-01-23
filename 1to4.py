##################################Create list with salary############################
emp_list=[]
for i in range(0,10):
    sal=int(input('Enter the salary'))
    emp_list.append(sal)
print(emp_list)

##################################Update all income by 5%############################
emp_list1=[]
for j in range(0,10):
    emp_list1.append(emp_list[j]*1.05)
print(emp_list1)

##################################Largest income offered#############################
max_sal=max(emp_list)
print(max_sal)

##################################Total income of all employees######################
tot_sal=sum(emp_list)
print(tot_sal)
