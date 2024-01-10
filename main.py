
def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x,y: x + y, list1,list2))


list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = add_two_lists(list1,list2)