## List

# def shawaal_Reverse_Arr(arr):
#     print("Inside Reverse Function")
#     arr.reverse()
#     return arr

# my_arr = [1,2,3,4,5,6,7,8,9,10]
# print(shawaal_Reverse_Arr(my_arr))


# arr1 = [1,2,3,4,5]
# arr2 = [6,7,8,9,10]
# shawaal_concatenate_arr = arr1 + arr2
# print(shawaal_concatenate_arr)


# shawaal_arr = [1,1,2,3,4,5,5,6,7,7]
# print(list(set(shawaal_arr)))


# shawaal_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(max(shawaal_arr))


## Tuple

# shawaal_tuple = (1,2,3,4,5,6,7,8,9,10)
# print(shawaal_tuple[:3])
# print(shawaal_tuple[3:])


# shawaal_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(type(shawaal_tuple))
# list_tuple = list(shawaal_tuple)
# print(type(list_tuple))


# shawaal_tuple = ('S', 'H', 'A', 'W', 'A', 'L')
# print(type(shawaal_tuple))
# shawaal_string=''
# for i in shawaal_tuple:
#     print(i)
#     shawaal_string+=i

# print(shawaal_string)
# print(type(shawaal_string))


# def sort_dict_by_values_shawaal(input_dict):
#     sorted_dict_shawaal = dict(sorted(input_dict.items(), key=lambda item: item[1]))
#     return sorted_dict_shawaal

# my_dict_shawaal = {'b': 3, 'a': 1, 'c': 2}
# sorted_dict_shawaal = sort_dict_by_values_shawaal(my_dict_shawaal)
# print(sorted_dict_shawaal)


# def dict_length_shawaal(input_dict):
#     return len(input_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print("Length of dictionary:", dict_length_shawaal(my_dict))



# def merge_dicts_shawaal(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# print("Merged dictionary:", merge_dicts_shawaal(dict1, dict2))


# def remove_key_shawaal(input_dict, key_to_remove):
#     if key_to_remove in input_dict:
#         del input_dict[key_to_remove]
#     return input_dict

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# key_to_remove = 'b'
# print("Dictionary after removing key:", remove_key_shawaal(my_dict, key_to_remove))



## Set

# def union_of_sets_shawaal(set1, set2):
#     return set1.union(set2)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print("Union of sets:", union_of_sets_shawaal(set1, set2))



# shawaal_set = {1, 2, 3}
# shawaal_set.add(4)
# print("Set after adding element:", shawaal_set)


# shawaal_empty_set = {}
# print("Empty set :", shawaal_empty_set)



shawaal_set = {1, 2, 3}
shawaal_set.remove(2)
print("Set after removing element:", shawaal_set)

