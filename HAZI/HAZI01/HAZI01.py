# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index):
    return input_list[start_index:end_index]

list = [0,1,2,3,4,5,6,7,8,9]
subset(list,2,5)


# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    return input_list[::step_size]

list = [0,1,2,3,4,5,6,7,8,9]
every_nth(list,2)

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    return len(input_list) == len(set(input_list))

list_without_duplicates = [0,1,2,3,4]
print(unique(list_without_duplicates))

list_with_duplicates = [0,1,1,2,2,3,4,]
print(unique(list_with_duplicates))

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    
    flattened_list = []
    for item in input_list:
        if isinstance(item, type(list)):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list

nested_list = [[0,1, 2], [3, [4, 5]], 6,7,[8,9]]
flatten(nested_list)

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    merged_list = []
    for list in args:
        merged_list.extend(list)
    return merged_list

list1 = [0,1,2]
list2 = [3,4,5]
list3 = [6,7,8,9]

merge_lists(list1,list2,list3)

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    reversed_list = []
    for tpl in input_list:
        reversed_tuple = tuple(reversed(tpl))
        reversed_list.append(reversed_tuple)
    return reversed_list

tuple_list = [(0,1),(2,3),(4,5),(6,7),(8,9)]
reverse_tuples(tuple_list)

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_duplicates(input_list):
    list_without_duplicates = []
    for item in input_list:
        if item not in list_without_duplicates:
            list_without_duplicates.append(item)
    return list_without_duplicates

listWithDuplicate = [0,1,1,2,3,4,5,6,6,7,8,9,9]
remove_duplicates(listWithDuplicate)

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    number_of_rows = len(input_list)
    number_of_columns = len(input_list[0])

    output = [[0 for j in range(number_of_rows)] for i in range(number_of_columns)]

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            output[j][i] = input_list[i][j]

    return output

matrix = [[1,2,3], [4,5,6], [7,8,9]]
transpose(matrix)

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list, chunk_size):
    chunks = []

    for i in range(0,len(input_list),chunk_size):
        chunk = input_list[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

list = [[0,1,2], [3,4,5], [6,7,8], [9,10,11],[12,13,14]]
split_into_chunks(list, 2)

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    merged_dictionaries = {}

    for d in dict:
        merged_dictionaries.update(d)

    return merged_dictionaries

dictionary1 = {'a' : 0, 'b' : 1, 'c':2}
dictionary2 = {'d': 3,'e': 4, 'f' : 5}
merge_dicts(dictionary1,dictionary2)

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    even = []
    odd = []
    for num in input_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return {"even": sorted(even), "odd": sorted(odd)}

list = [0,1,2,3,4,5,6,7,8,9]
by_parity(list)

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    output = {}
    for key,value in input_dict.items():
        output[key] = sum(value) / len(value)
    return output

dictionary1 = {"some_key":[1,2,3,4],"another_key":[1,2,3,4],"third_key":[5,5,5,5]}

mean_key_value(dictionary1)

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


