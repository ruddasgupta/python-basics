lis = ["Even number" if i % 2 == 0
	else "Odd number" for i in range(8)]
print(lis)

lis1 = [num for num in range(100)
	if num % 5 == 0 if num % 10 == 0]
print(lis1)

# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
 
# Display list
print(List)


# Explicit function
def digit_sum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
 
 
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
 
# Using the function on odd elements of the list
newList = [digit_sum(i) for i in List if i & 1]
 
# Displaying new list
print(newList)