"""
A function named add_time that takes in two required parameters and one optional parameter.
"""


def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


def add_time(start_time, end_time, day=False):
    # Create constants
    hours_per_day = 24
    half_day_hours = 12
    week_days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    days_later = 0
    hours, mins = start_time.split(":")
    mins, period = mins.split(" ")
    end_time_hrs, end_time_mins = end_time.split(":")

    # Typecasting
    hours = int(hours)  # --> start time hours
    mins = int(mins)  # --> start time minutes
    end_time_hrs = int(end_time_hrs)  # --> end time hours
    end_time_mins = int(end_time_mins)  # --> end time minutes
    period = period.strip().lower()  # --> AM or PM

    # Adding start and end time
    total_mins = mins + end_time_mins
    total_hours = hours + end_time_hrs

    # Converting minutes to hours if minutes > 60
    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if end_time_hrs or end_time_mins:
        # Change period
        if period == 'pm' and total_hours > half_day_hours:
            # Checking if hours > 24
            if total_hours % hours_per_day >= 1.0:
                days_later += 1

        if total_hours >= half_day_hours:
            # 66hrs / 24 = 2.75days ==> Add 2 days to 'days_later'
            hours_left = total_hours / hours_per_day
            days_later += int(hours_left)

        temp_hours = total_hours
        while True:
            # Reversing period constantly until total_hours are less than half a day.
            if temp_hours < half_day_hours:
                break
            if period == "am":
                period = "pm"
            else:
                period = "am"
            temp_hours -= half_day_hours

    """
    Now calculating remaining hours after calculating days.
    Attained by subtracting remaining days (convert in hours) from the total hours remaining.
    i.e., 66hrs % 24 --> 18 ==> 18 hours remaining
    """

    remaining_hours = int(total_hours % half_day_hours) or hours + 1
    remaining_mins = int(total_mins % 60)

    # String formatting
    results = f"{remaining_hours}:{str(remaining_mins).zfill(2)} {period.upper()}"
    if day:  # --> Adding week-day
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f", {current_day.title()} {get_days_later(days_later)}"

    else:
        # -- add the later days
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
