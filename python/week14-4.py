# MAIN CODE 
persons = eval(input())
age = int(input())

# Write your code here !
for n in range(len(persons)):
    if persons[n][2] == age:
        print(persons[n][0])