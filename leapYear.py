def checkLeap(year):
	'''
	Objective: To check whether the given year is leap year or not
	Input parameter:
			year: the user entered year
	Return Value: Boolean value whether it is leap year or not
	'''
	#Approach: Check whether user entered year  is divisible by 4(not 100),and 400(and 100)
	      #if yes then it is a leap year
	      #if not then it is not a leap year
	leap = False
	if ((year%4)==0 and (year%100!=0)):
		leap = True
	elif ((year%100)==0 and (year%400==0)):
		leap = True
	else:
		leap = False
	return leap

def main():
	'''
	Objective: To take input from user an call cheakLeap() function
	Input parameter:none
	Return Value: none
	'''
	
	year = int(input('Enter an year : '))
	leapYear = checkLeap(year)

	if leapYear==True:
		print(year,' is a leap year.')
	else:
		print(year,' is not a leap year.')

if __name__ == '__main__':
	main()
