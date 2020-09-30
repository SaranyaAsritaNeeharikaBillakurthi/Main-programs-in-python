##ARMSTRONG NUMBER(sum of individual cubes of a given number)

n=int(input('enter a number'))
s=0
a=n
while n>0:
	rem=n%10
	s+=rem*rem*rem
	n=n//10
if a==s:
	print(a,' is armstrong number')
else:
	print(a,' is not armstrong number')

#####

n=int(input('enter a number'))
s=0
a=n
while n>0:
	rem=n%10
	print(rem,'rem value')
	s+=rem*rem*rem
	print(s,'s value')
	n=n//10
	print(n,'n valur')
if a==s:
	print(a,' is  armstrong number')
else:
	print(a,' is not armstrong number')