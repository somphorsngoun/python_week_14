# MAIN CODE 
array = eval(input())

# Write your code here !
result = []
for co in range(len(array[0])):
    sum = 0
    for row in range(len(array)):
        sum += array[row][co]
    result.append(sum)
print(result)