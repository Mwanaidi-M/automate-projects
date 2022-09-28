import datetime
import time

# The time.time() function returns the number of seconds as a float value. This number is
# called an epoch timestamp.
curr_time = time.time()

# If you need to pause your program for a while, call the time.sleep() function
# and pass it the number of seconds you want your program to stay paused.
# for num in range(1, 6):
#     print("Tick...")
#     time.sleep(2)
#     print("Tock...")
#     time.sleep(2)


# print(f"Current time: {curr_time}")
# print(f"Current time rounded to 2 d.p: {round(curr_time, 3)}")
# print(f"Current time rounded to a whole integer: {round(curr_time)}")

# The datetime module has its own datetime data type whose values represent a specific moment in time.
# Calling datetime.datetime.now() returns a datetime object for the current date and time, according
# to your computer’s clock. This object includes the year, month, day, hour, minute, second,
# and microsecond of the current moment.
now = datetime.datetime.now()

# print(f"Now: {now}")
#
# print(f"Year: {now.year}")
# print(f"Month: {now.month}")
# print(f"Day: {now.day}")
#
# print(f"Hour: {now.hour}")
# print(f"Minute: {now.minute}")
# print(f"Seconds: {now.second}")

# A Unix epoch timestamp can be converted to a datetime object with the
# datetime.datetime.fromtimestamp() function.

time_stamp = datetime.datetime.fromtimestamp(450000955)
# time_stamp = datetime.datetime.fromtimestamp(curr_time)

# print(time_stamp)

# datetime objects can be compared with each other using comparison operators to find out which
# one precedes the other.

# The datetime module also provides a timedelta data type, which represents a duration of time
# rather than a moment in time. The datetime.timedelta() function takes keyword arguments weeks,
# days, hours, minutes, seconds, milliseconds, and microseconds. There is no month or year keyword
# argument because “a month” or “a year” is a variable amount of time depending on the particular
# month or year.

days_10_future = datetime.timedelta(days=10)

# The total_seconds() method will return the duration in number of seconds alone.
# print(days_10_future.total_seconds())

# Passing a timedelta object to str() will return a nicely formatted, human-readable string
# representation of the object.
# print(str(days_10_future))

# The arithmetic operators can be used to perform date arithmetic on datetime values.
future_10 = now + days_10_future
# print(f"10 days from now the date will be: {future_10.date()}")

# timedelta objects can be added or subtracted with datetime objects or other timedelta objects
# using the + and - operators. A timedelta object can be multiplied or divided by integer or
# float values with the * and / operators.
years_30_future = datetime.timedelta(days=365*30) + now
# print(f"In about 30 years, we will be in the year: {years_30_future.year}")

# Epoch timestamps and datetime objects aren’t very friendly to the human eye. Use the strftime()
# method to display a datetime object as a string. (The f in the name of the strftime() function
# stands for format.) Pass strrftime() a custom format string containing formatting directives
# (along with any desired slashes, colons, and so on), and strftime() will
# return the datetime object’s information as a formatted string.
# print(f"In about 30 years, the date will be: {years_30_future.strftime('%Y-%b-%d [%j]')}")


# The strptime() function is the inverse of the strftime() method. It converts a string to a
# datetime object. A custom format string using the same directives as strftime() must be passed
# so that strptime() knows how to parse and understand the string. (The p in the name of the
# strptime() function stands for parse.)

sample_date = '2015/10/21 16:29:00'
sample_date_obj = datetime.datetime.strptime(sample_date, "%Y/%m/%d %H:%M:%S")

# print(type(sample_date))
# print(type(sample_date_obj))

