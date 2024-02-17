# should print hello world
print("hello world")

# variable assignment
x = "name"
y = "my name"
a, b = 1, x
# will print with spaces and end new line
print(x, y, a, b)
# will print with new lines and no end character
print(x, y, a, b, sep='\n', end="")
# override all variables
x = y = a = b = "hello"
print()
print(x, y, a, b)

# can unpack collections
collection = (1, 2, 3)
x, y, z = collection
print(x, y, z)

# random number
import random
print(random.randrange(1, 10))

# strings
a = "hello world"
print(len(a))
for i in a:
	print(i)
print()
for i in range(len(a)):
	print(a[i])
print()
for i, letter in enumerate(a):
	print(f"index={i} letter={letter}")
print()
if "hello" in a:
	print("yes")


def reverse_code(x: int) -> int:
        ret = []
        if neg := x * -1 > 0: 
            x = x * -1 

        print(neg)
        while x > 0: 
            ret.append(str(x % 10))
            x = x // 10
        print(ret)
        return int("".join(ret)) * -1 if neg else int("".join(ret))

print(reverse_code(102))
