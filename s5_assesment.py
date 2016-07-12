#Question 1
st = 'Print only the words that start with s in this sentence'
split_st = st.split()
for word in split_st:
	if word[0] == 's':
		print word

#Question 2
lst = range(0,11,2)
print lst

#Question 3
lst = [x for x in range(1,51) if x % 3 == 0]
print lst

#Question 4
st = 'print every word in this sentence that has an even number of letters'
split_st = st.split()

for word in split_st:
	if len(word) % 2 == 0:
		print word

#Question 5
for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print 'FizzBuzz'
	elif num % 3 == 0:
		print 'Fizz'
	elif num % 5 == 0:
		print 'Buzz'
	else:
		print num

#Question 6
st = 'Create a list of the first letters of every word in this string'
lst = [ x[0] for x in st.split()]
print lst