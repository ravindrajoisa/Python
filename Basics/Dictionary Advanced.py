#Python 3.7.3 Shell

dictionary1 = {'a':1, 'b':2, 'c':3, 'd':4}
dictionary1

double_dictionary1= {k:v*2 for (k,v) in dictionary1.items()}
double_dictionary1

dictionary1_keys = {k*2: v for (k,v) in dictionary1.items()}
dictionary1_keys

new_dictionary = {}
for n in numbers:
	if n%2 == 0:
		new_dictionary[n] = n**2
new_dictionary

new_dictionary_2 = {n:n**2 for n in numbers if n%2 == 0}
new_dictionary_2

new_dictionary == new_dictionary_2
