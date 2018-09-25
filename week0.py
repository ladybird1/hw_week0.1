
#Task 2.
#1
task_wto_list = list(range(1, 20, 2))
print(task_wto_list)
#2 
elements = [1, 5, 13, 20]
task_three_list = (task_wto_list + elements)
print(task_three_list)
#3
task_four_set = set(task_three_list)
print(task_four_set)
#4
def copmpare_elements(a:list, b:set):
	if ( len(a) > len(b) ):
	 	return 'List is bigger'
	return 'Set is bigger'

print(copmpare_elements(task_three_list,task_four_set))

#Task 3
def get_value_from_list(data:list, index:int):
	try:
		print(data[index])
	except:
		print(None)

get_value_from_list([1,2,3], 1)

#Task 4 
dictionary = {}
def create_dict(name:str, age:int, hobby:str):
		dictionary['Name'] = name
		dictionary['Age'] = age 
		dictionary['Hobby'] = hobby
		return dictionary
print(create_dict('Denis', '26', 'Books'))

#Task 5
def calculate_fibo(n:int):
	fibo = []
	n1 = n2 = 1
	count = 0
	if n <= 0: 
		return 'Please enter positive integer'
	elif n == 1 : 
		return 1 
	else:
		while count < n:
			print(n1, end = ',')
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count +=1 

calculate_fibo(5)
