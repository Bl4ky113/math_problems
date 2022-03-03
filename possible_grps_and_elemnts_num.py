from num_possible_groups import find_possible_groups
import plotly.express as px

def main ():
    DATA_RANGE = 100
    len_possible_groups = []
    len_element_arr = []
    num_per_group = 2

    for i in range(DATA_RANGE):
        element_arr = [j + 1 for j in range((num_per_group + 1) + i)]
        possible_groups_arr = []

        find_possible_groups(num_per_group, element_arr, possible_groups_arr)

        len_possible_groups.append(len(possible_groups_arr))
        len_element_arr.append(len(element_arr))

    fig = px.scatter(
        x=len_element_arr,
        y=len_possible_groups
    )
    
    print("Init figure")

    fig.show()

    print("Show Figure")

if __name__ == "__main__":
    main()
