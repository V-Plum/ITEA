# Import libs to work with date and time
import datetime
from datetime import date
from datetime import timedelta
import calendar

# Switch locale to Ukrainian to get Ukrainian days from Calendar. Do not switch if there are no Ukrainian locale in system
try:
    import locale
    locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')
except locale.Error:
    print("\nSorry, you have no Ukrainian locale on this PC, so you will see English days\n")

# Create empty lists
days_list = []
wake_time = []

# Set start data
my_date = date.today()
current_wake_time = 480  # 8:00 in minutes

# Run a loop for 21 days
for day in range(0, 21):
    # Write 21 days names to list, starting from tomorrow
    next_day = my_date + datetime.timedelta(days=day+1)
    day_name = calendar.day_name[next_day.weekday()]
    days_list.insert(day, day_name)

    # Check if it's weekend, if not -- set wake time to -15 mins
    if day_name == "Saturday" or day_name == "Sunday" or day_name == "субота" or day_name == "неділя":
        next_day_time = current_wake_time
    else:
        next_day_time = current_wake_time - 15

    # Write time to array in H:MM format
    wake_time_delta = str(timedelta(minutes=next_day_time))[:-3]
    wake_time.insert(day, wake_time_delta)
    current_wake_time = next_day_time

    print(days_list[day], wake_time[day])
