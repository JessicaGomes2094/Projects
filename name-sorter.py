# Name-Sorter Program
# Program to sort alphabetically last names, then by any given names and print to file 'sorted-names.txt'
# Import string
# Import os Library
import os
path = str(os.getcwd()+'/')


def getData(filename):

    read = open(path+filename, 'r+').readlines()

    data = [row.replace('\n', '') for row in read]

    return data


def sortData(list_data):

    list_data.sort(key=lambda x: x.split()[-1])  # Sort By Last Element Of List

    # Sort By Last Element And Then The Next (TEST)
    # List_data.sort(key=lambda element: (element[-1], element[0]))

    return list_data


def saveValue(sort_value):

    if sort_value:

        with open('sorted-names-list.txt', 'w') as f:

            for item in sort_value:

                f.write("%s\n" % item) #Write to file

        message = 'List of sorted names has been saved.'

    return message

# Get List of Data Values and Print Unsorted Names On A New Line


list_data = getData('unsorted-names-list.txt')

print('Unsorted Names : ', list_data, '\n')


# Sort Data Values and Print Sorted Names On A New Line

sort_value = sortData(list_data)

print('Sorted Names : ', sort_value, '\n')


# Save List Of Data Values

save_data = saveValue(sort_value)

print(save_data)
