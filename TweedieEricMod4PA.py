# Eric Tweedie Mod 4 Project Assignment
# The limit of the optimal solution is expressed by the volume in cubic inches (in3) and the program has to maximize the value within the cubic limit
# Program that reads a text file with one item per line with the information separated by a comma
# Program should capture the overall limit of the package/knapsack from the user
# Should read any file with the format (name, value, height, width, depth) per line
# program must print out the best distribution with a string

# opening and reading the file
def read_file(filename):
    items = []          # empty list for each item from the file
    with open(filename, 'r') as file:           # open the file
        for line in file:
            name, value, height, width, depth = line.strip().split(',')     # strip the whitespace and split on the commas
            items.append({                                                  # assigning the values from the file into a list
                'name': name,
                'value': int(value),
                'height': int(height),
                'width': int(width),
                'depth': int(depth),
                'volume': int(height) * int(width) * int(depth)
            })
    return items

# knapsack function
def knapsack(value, volume, cap, name):
    rvv = []                        # triple ratio, volume, value, index, name
    for i in range(len(value)):
        rvv.append([value[i]/volume[i], volume[i], value[i], i, name[i]])
    rvv.sort(reverse=True)          # sort from high to low
    ans = []                        # list of added items
    tw = 0                          # total weight
    found = True
    item_count, other, total_volume, price = 0, 0, 0, 0 # counters for items that are the same, not the same, total volume and price
    names = [] # list of names
    name2 = []  # list of names of items that are not the same as the first item in ans list
    while (found):                  # until no found item is found
        found = False
        for t in rvv:               # search an item to add
            if (t[1] + tw) <= cap:  # if the item fits add it
                ans.append(t[3])
                tw += t[1]
                total_volume += t[1]
                price += t[2]
                names.append(t[4])
                found = True
                break
                
    for i in range(len(ans)):       # checking if items in ans are the same and counting how many
        if ans[i] == ans[i-1]:
            item_count += 1
        else:
            other += 1
                
    for j in range(len(names)):     # checking the names in the list to see if there is an additional name in list
        for k in range(len(names)):
            if names[j] != names[k]:
                name2.append(names[k])
            else:
                continue
            
    space = cap - total_volume   # getting total volume used
    for i in range(len(ans)):
        if ans[i] == ans[i-1]:
            return f"The suggested items are: {item_count} {names[0]} with a total value of ${price}. There was {space} cubic inches left over."
        else:
            return f"The suggested items are: {item_count} {names[0]} and {other} {name2[0]} with a total value of ${price}. There was {space} cubic inches left over."

#  main function
def main():
    try:
        filename = input("Enter the name of the file you want to use: ")
    except FileNotFoundError:
        print("File not found.")
    read_file(filename)
    print("Please enter the overall limit of the package/knapsack in cubic inches (in3).")
    try:
        cap = int(input("Please enter the limit of the package/knapsack: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    volume = []     # list to hold the volume value from items
    value = []      # list to hold the value value from items
    name = []       # list to hold the name values from items
    for item in read_file(filename):
        volume.append(item['volume'])
        value.append(item['value'])
        name.append(item['name'])
    
    print(knapsack(value, volume, cap, name))

main()