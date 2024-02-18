# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def is_unique(s): 
	check = [0] * 26
	for letter in s:
		check[ord('a') - ord(letter.lower())] += 1 
		if check[ord('a') - ord(letter)] > 1:
			return False
	return True


def replace_spaces(s, sep):
	string_array = [*s]
	for i in range(len(string_array)):
		if string_array[i] == " ":
			string_array[i] = sep

	return "".join(string_array)

def palindrome_permutation(s):
	freq = [0] * 26
	for letter in s:
		if letter not in [' ']:
			freq[ord('a') - ord(letter.lower())] += 1
	check = False
	for letter in s:
		if letter not in [' ']:
			if freq[ord('a') - ord(letter.lower())] % 2: 
				if check:
					return False
				else: 
					check = True	
	return True

def compress_string(s):
	
	count = 1
	prev_character = s[0]
	i = 1
	ret = []
	while i < len(s): 
		if s[i] == prev_character:
			count += 1
		else:
			ret.append(prev_character)
			ret.append(str(count))
			count = 1 
		prev_character = s[i]
		i += 1
	
	ret.append(prev_character)
	ret.append(str(count))

	return ''.join(ret)

	

if __name__ == "__main__":
	print("is_unique")
	print(is_unique("Sad"))
	print(is_unique("Saad"))
	print("replace_spaces")
	print(replace_spaces("Mr John Smith", "xxx"))
	print("palindrome_permutations")
	print(palindrome_permutation("Tact Coa"))
	print(palindrome_permutation("Tact CCoa"))
	print('compress_string')
	print(compress_string('aaabccd'))
	print(compress_string('abcd'))

