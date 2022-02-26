
from random import randint

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
    num_group = randint(3, 3)
    num_arr = [i for i in range(randint(5, 5))]
    possible_groups_arr = []

    print(num_arr)
    print(num_group)

    for num_i in num_arr:
        used_index = [num_arr.index(num_i)]

        for num in num_arr:
            group = create_group(num_arr, num_group, used_index)
            check_group(possible_groups_arr, group)

            print("i: ", used_index)
            print("g: ", group)

    print(possible_groups_arr)
            

if __name__ == "__main__":
    main()
