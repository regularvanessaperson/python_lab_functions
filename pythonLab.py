# 1. 

# def sum_to(n):
#     sum= 0
#     for i in range(1, n+1):
#         sum+= i
#     print(sum)

# sum_to(6)
# sum_to(10)
    
# 2.

# def largest(list):
#     largest_num = 0
#     print(max(list))

# largest([10, 4, 2, 231, 91, 54])
# largest([1,2,3,4,0])

#3.

# def occurances(string, letter):
#     if x in string:
#         count = 0
#         if i == letter:
#             count += 1
#     print(count)

# this works
# def occurances(string, letters):
#     print(string.count(letters))

# occurances('fleep floop', 'e')   
# occurances('fleep floop', 'p')   
# occurances('fleep floop', 'ee')  
# occurances('fleep floop', 'fe')

#4.

def product(*vals):
    product = 1
    for val in vals: 
       product *= val
    print(product)

product(1,3,5,7)
