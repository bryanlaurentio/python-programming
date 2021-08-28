# Capital indexes

# Write a function named capital_indexes. The function takes a single parameter, which is a string. 
# Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(a):
    temp = []
    index = 0
    for x in a:
        if x == x.upper(): 
            temp.append(index)
        index += 1
    return(temp)

print(capital_indexes("HeLlo"))
