import random
lst_employee_details=[]
lst_employee_result=[]
int_count=0
int_total_age=0
for x in range (100):
	lst_rst=[]
	str_name='Name'+ str(x)
	int_age=random.randint(21,61)
	int_salary=random.randint(1000,4001)
	#taking random values
	lst_rst=[str_name,int_age,int_salary]
	lst_employee_details.append(lst_rst)
print(lst_employee_details)
	#above 'for' initialising data
for result in lst_employee_details:
	
	if result[2]>3000:
	#checking age>3000
			int_count+=1
			lst_employee_result.append(result[0])
			int_total_age += result[1]
	else:
		     pass

	# finding mean age
flt_mean_age=int_total_age/int_count
print ('employees with salary > 3000 are\n')

for x in lst_employee_result :
	print (x)
print ('mean age is ',flt_mean_age)	
			
