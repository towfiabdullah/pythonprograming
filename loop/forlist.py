# list = [1,2,3]
# for el in list :
#     print(el)
# for i in range(10):
#     print(i)  

# for i in range(2,10,2):
#     print(i)
n=7
sum = 0
for i in range(1,n+1):
    sum +=i
    
print(sum) 
for i in range(1, 6):  # Outer loop (for each row)
    for j in range(1, 6):  # Inner loop (for each column)
        print(i * j, end="\t")  # Print the product and stay on the same line
    print()  # Print a newline after each row
    

 