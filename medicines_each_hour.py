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

def calc_date(current_date=1, range_date=1, restart_count=24):
    date = current_date

    for i in range(range_date):
        if date > restart_count:
            date = 0

        date += 1

    return date

def main():
    current_day_index =  4 - 1
    current_hour = 15
    person = "Juan"

    medicines_count = [1 for i in range(len(medicines))]
    iterations = 0

    while True:
        breake_loop = False
        takes_medicine = [False for i in range(len(medicines))]
        iterations += 1

        for i in range(len(medicines)):
            if iterations % medicines[i]["each_hour"] == 0:
                medicines_count[i] += 1
                takes_medicine[i] = True
        
        all_true = True
        for take in takes_medicine:
            if take == False:
                all_true = False
        
        if iterations == 1000 or all_true:
            break

    days_passed = iterations // 24
    hours_passed = iterations % 24

    hours_date = calc_date(current_hour, hours_passed, 24)
    index_day_date = calc_date(current_day_index, days_passed, 6)
    
    for i in range(int(hours_passed)):
        if current_hour == 24:
            current_hour = 0
            break

        current_hour += 1

    for i in range(int(days_passed + 1)):
        if current_day_index == 6:
            current_day_index = 0
            break

        current_day_index += 1

    print(f"In {days_passed} days and {hours_passed} hours on {name_days[index_day_date]} {hours_date}, {person} will take the {len(medicines)} medicines")

if __name__ == "__main__":
    main()

