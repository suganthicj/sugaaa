#python program to find the number of digits in a given number 
def count(num):
    n = str(num)
    count = 0
    for e in n:
        count = count + 1
    print("Number of digits in the given number "+n)
    return count

print(count(1234))
