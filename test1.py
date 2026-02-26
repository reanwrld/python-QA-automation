#Author name: Reyan Heyar
#Test 1
#02/17/2026

start = int(input("Enter a number (lower bound): "))
stop = int(input("Enter a number (upper bound): "))
step = int(input("Enter a positive number: "))
    
if start >= stop:
    print("Error: start must be less than stop")
    exit()
if step <= 0:
    print("Error: step must be a positive number")
    exit()

count = 0    
countEven = 0
countOdd = 0
countDiv3 = 0

numbers = []
for n in range(start, stop +1, step):

    square = n**2
    cube = n**3
    if n % 2 == 0:
        parity = "Even"
        countEven += 1 
    else:
        parity = "Odd" 
        countOdd += 1
    if n % 3 == 0:
        div3 = "yes"
        countDiv3 += 1
    else:
        div3 = "No" 
    count += 1
    numbers.append(n)
    print("")
    print("%6d%12d%12d %-4s %-3s" % (n, square, cube, parity, div3))
    

print("")
print("Total Count of values produced:", count)
print("Min:", numbers[0])
print("max:", numbers[-1])
print("Sum of all n:", sum(numbers))
print("Mean of all n:", sum(numbers) / len(numbers))
print("Even counts:", countEven)
print("odd counts:", countOdd)
print("Multiple of 3:", countDiv3)
