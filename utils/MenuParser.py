import json
import calendar
from datetime import datetime
def parse_month(month_name):
    months_mapping = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    return months_mapping.get(month_name.capitalize(), None)

def parseJsonMenu(json_Data_Str,month=None):
    current_date = datetime.now()

    menu_data = json.loads(json_Data_Str)
    if month is None:
        current_month = current_date.month
    else:
        current_month = parse_month(month.capitalize())

    current_year = current_date.year

    # Get the day of the week for the first day of the current month
    first_day_of_month = datetime(current_year, current_month, 1)
    first_day_of_week = calendar.day_name[first_day_of_month.weekday()]
    print(first_day_of_week)

    # Define days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Define the days of the month based on the current month
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    month_days = range(1, days_in_month + 1)

    # Generate menu string for each day of the month
    menu_strings = []
    for day in month_days:
        day_of_week = days_of_week[(days_of_week.index(first_day_of_week) + day - 1) % 7]
        menu_item = menu_data.get(str(day), "Error")
        menu_strings.append(f"{day_of_week} {day} {menu_item}")

    # Join menu strings with newlines
    menu_result = '\n'.join(menu_strings)

    
    return menu_result
