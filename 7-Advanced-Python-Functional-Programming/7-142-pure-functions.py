def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# Pure functions
# 1st rule: Given the same input, it will always return the same output
# 2nd rule: produces no side effects