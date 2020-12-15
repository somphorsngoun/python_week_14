def splitBySpace(theString) :
    # Write your code here !
    result = []
    String = ""
    for n in range(len(theString)):
        if theString[n] != " ":
            String += theString[n]
        else:
            result.append(String)
            String = ""
    result.append(String)
    return result

# MAIN CODE 
word = input()

# Write your code here !
print(splitBySpace(word))
