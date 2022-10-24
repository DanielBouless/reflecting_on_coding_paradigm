


def flatten(array):
    flattened_array = []
    for i in array:
        for x in i:
            flattened_array.append(x)
    return sorted(flattened_array)


# Questions

# HOW DOES THIS SOLUTION ENSURE DATA IMMUTABILITY?

#     The data being sent through never changes. The function takes in data and outputs other data that is seperate from the original.

# IS THIS SOLUTION PURE FUNCTION? WHY OR WHY NOT?

#     This is a pure function because it requires nothing else but being invoked with parameters as required.

# IS THIS SOLUTION HIGHER ORDER FUNCTION? WHY OR WHY NOT?
    
#     No.

# WOULD IT HAVE BEEN EASIER TO SOLVE THIS PROBLEM USING A DIFFERENT PROGRAMMING STYLE?

#     This is the simplest way to flatten any array multiple times.

# WHY IN PARTICULAR IS FUNCTIONAL PROGRAMMING A HELPFUL PARADIGM WHEN SOLVING THIS PROBLEM?

#     It can be used to manipulate existing data without saving data to an object.

