## Star Program

# a = "*"
# for item in range(1,6):
#     item = item * a
#     print(item)

## Reverse Star Progam
# n = 5
# for i in range (n, 0, -1):
#     print((n-i) * ' ' +  i * '*')

# # Star Program like kite
# num = 5
# for item in range(1, 10, 2):
#     print(num*' ' + item * '*')
#     num = num - 1
# # Reverse Star Program

# for item in range (num, 0, -1):
#     print((num-item)* ' ' + 2 * item * '*')

# ## Print the list of squars of first 100 number
# sq =[]
# for i in range(1, 100):
#     sq.append(i**2)
# print(sq)

## Print the list of squars of first 100 number Using list Comprehension
squar = [i**2 for i in range(1, 100)]
print(squar)