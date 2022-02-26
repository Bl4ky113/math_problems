
from random import randint

def find_possible_groups (num_element_per_group=2, element_arr=[], possible_elements_groups_arr=[]):
    for element_i in element_arr:
        used_index = [element_arr.index(element_i)]

        for num in element_arr:
            group = create_group(element_arr, num_element_per_group, used_index)
            check_group(possible_elements_groups_arr, group)

def create_group (element_arr=[], size_group=2, used_elements_index=[]):
    created_group = [element_arr[used_elements_index[0]]]

    for i in range(len(element_arr)):
        if i not in used_elements_index:
            created_group.append(element_arr[i])
            used_elements_index.append(i)

            if len(created_group) == size_group:
                return created_group

    return None

def check_group (checked_group=[], to_check_group=[]):
    if to_check_group == None:
        return

    to_check_group.sort()

    if to_check_group not in checked_group:
        checked_group.append(to_check_group)

def main ():
    num_group = randint(2, 5)
    num_arr = [i + 1 for i in range(randint(5, 12))]
    possible_groups_arr = []

    print(f'list: {num_arr}, l:{len(num_arr)}')
    print(f'group number: {num_group}')

    find_possible_groups(num_group, num_arr, possible_groups_arr)

    print(f'{possible_groups_arr}, l:{len(possible_groups_arr)}') 

if __name__ == "__main__":
    main()
