def insert_value_front(input_tuple, value_to_insert):
    return (value_to_insert,)+input_tuple
input_tuple = (2, 3, 4)
value_to_insert = 1
print(insert_value_front(input_tuple, value_to_insert))


#2nd Approach.
def insert_value_front(input_tuple, value_to_insert):
    List=list(input_tuple)
    List.insert(0,value_to_insert)
    input_tuple=tuple(List)
    return input_tuple
input_tuple = (2, 3, 4)
value_to_insert = 1
print(insert_value_front(input_tuple, value_to_insert))