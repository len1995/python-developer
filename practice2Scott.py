#first_name='Scott'
#last_name='Burton'

#output=f'Your name is {last_name}, {first_name} {last_name}.'
#print(output)

outputf=input('What is your first name?')
outputln=input('What is your last name?')

#print('Your name is'+' '+outputf.lower()+' '+outputln.upper())
#print(f'Your name is {outputf.title()} {outputln.title()}')
print('Your name is {}, {} {}.'.format(outputln, outputf, outputln))