# MAIN CODE 
array2D = eval(input())

# Write your code here !
for n in range(len(array2D)):
    for r in range(len(array2D[n])):
        if array2D[n][r] == 7:
            array2D[n].pop(r)
            array2D[n].insert(r,8)
print(array2D)