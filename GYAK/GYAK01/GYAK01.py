# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list):
    for num in input_list:
        if num%2 != 0:
            return True
    return False

list = [0,1,2,3,4,5,6,7,8,9]
contains_odd(list)

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
    output_list = []
    for num in input_list:
        if num % 2 == 0:
            output_list.append(False)
        else:
            output_list.append(True)
    return output_list

list = [0,1,2,3,4,5,6,7,8,9]
is_odd(list)

# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list1, input_list2):
    if len(input_list1) == len(input_list2):
        return [input_list1[i] + input_list2[i] for i in range(len(input_list1))]
    else:
        return []
    
list1 = [0,1,2,3]
list2 = [4,5,6,7]

element_wise_sum(list1,list2)

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    output_list = []
    for key,value in input_dict.items():
        output_list.append(tuple([key,value]))
    return output_list

dictionary = {'a':1, 'b':2, 'c':3}
dict_to_list(dictionary)

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


