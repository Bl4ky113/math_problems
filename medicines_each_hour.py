# Made By Bl4ky

def minimun_common_multiple_multiples(len_numbers=2, multiples=[]):
    iterations = 0

    while True:
        break_loop = True
        iteration_is_multiple = [False for i in range(len_numbers)]
        iterations += 1

        for i in range(len_numbers):
            if iterations % multiples[i] == 0:
                iteration_is_multiple[i] = True

        for iteration_multiple in iteration_is_multiple:
            if iteration_multiple == False:
                break_loop = False

        if iterations > 1000 or break_loop:
            return iterations


def calc_date(current_date=1, range_date=1, restart_count=24):
    date = current_date

    for i in range(range_date):
        if date > restart_count:
            date = 0

        date += 1

    return date

def convert_hour_to_AM_PM(hour=12):
    converted_hour = hour
    day_time = "AM"

    if hour > 12:
        converted_hour -= 12
        day_time = "PM"

    return f"{converted_hour} {day_time}"

def get_values_from_obj_in_arr(arr=[], key=""):
    values = []
    try:
        for obj in arr:
            values.append(obj[key])

        return values
    except KeyError:
        raise "This Array-List doesn't have objs with the given key"

def main():
    medicines = [
        {
            "grams": 500,
            "units": 30,
            "each_hour": 8
        },
        {
            "grams": 500,
            "units": 30,
            "each_hour": 10
        },
        {
            "grams": 500,
            "units": 30,
            "each_hour": 6
        }
    ]

    name_days = [
        "mon",
        "tue",
        "wed",
        "thu",
        "fri",
        "sat",
        "sun"
    ]

    current_day_index =  3
    current_hour = 15
    person = "Juan"

    multiples_arr = get_values_from_obj_in_arr(medicines, "each_hour")
    iterations = minimun_common_multiple_multiples(len(medicines), multiples_arr)

    days_passed = iterations // 24
    hours_passed = iterations % 24

    hours_date = convert_hour_to_AM_PM(calc_date(current_hour, hours_passed, 24))
    index_day_date = calc_date(current_day_index, days_passed, 6)

    print(f"In {days_passed} days and {hours_passed} hours on {name_days[index_day_date]} {hours_date}, {person} will take the {len(medicines)} medicines")

if __name__ == "__main__":
    main()

