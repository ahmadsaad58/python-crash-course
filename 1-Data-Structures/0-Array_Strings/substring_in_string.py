def find_substring(string: str, substring: str) -> int:
	for i in range(len(string) - len(substring) + 1): 
		if string[i : i + len(substring)] == substring:
			return i
	return -1

def main():
	print(find_substring('hello world', 'world'))
	print(find_substring('hello world', 'hello'))
	print(find_substring('hello world', 'hell'))
	print(find_substring('hello world', 'word'))



if __name__ == '__main__':
	main()
