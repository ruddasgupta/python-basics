# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simple_generator():
	yield 1
	yield 2
	yield 3


if __name__ == '__main__':
    # Driver code to check above generator function
    for value in simple_generator():
        print(value)
