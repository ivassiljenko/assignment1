#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
The python code in this file is original work written by
Ivan Vassiljenko. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Ivan Vassiljenko
Semester: Fall 2024
Description: Assignment #1, Version C, OPS445NCC
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    # Divide the date string into day, month, and year
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    # Change the year for January and February based on Sakamoto's algorithm
    if month < 3:
        year -= 1
    # Using Sakamoto's algorithm to get the day of the week
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    # Verify if the year can be divided by 4
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Return 2 if the month is February and if it's a leap year
    if month == 2 and leap_year(year):
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    # String is divided by day, month, year
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    leap_flag = leap_year(year)  # Verify if it's a leap year

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Update the maximum number of days for February, if the result is a leap year
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    # If the next day is greater than the maximum days for the month
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    # Divide the date string into day, month, year
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    leap_flag = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap_flag = True
    # Dictionary showing the maximum number of days for each month
    mon_dict= {1:31,2:28,3: 31,4: 30,5:31,6:30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # Update the maximum number of days for February if it's a leap year
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict [mon]
    # Adjust the month and year if the day is less than 1
    if day < 1:
        mon -= 1
        if mon < 1:
            year -= 1
            mon = 12
        day = mon_dict[mon]  
        # If it's February and a leap year, update the day
        if mon == 2 and leap_flag:
            day = 29
     
    return f"{day:02}/{mon:02}/{year}"


def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    try:
       # Divide the date string into day, month, year
       day, mon, year = (int(x) for x in date.split('/'))
       # Verify if month is between 1 and 12, day is between 1 and the total number of days for the month, and year is positive
       if 1 <= mon <= 12 and 1 <= day <= mon_max(mon, year) and year > 0:
            return True
    except (ValueError, KeyError) :
        pass # Ignore errors caused by invalid input format
    return False

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    date = start_date # Set the current date to the start date
    if num > 0: # Move forward in time, if number is positive
        for _ in range(num):
            date = after(date) # 'After' function sets the next date
    elif num < 0: # Move back in time if the number is positive
        for _ in range(num, 0):
            date = before(date) # 'Before' function is used to set the previous date
    return date


if __name__ == "__main__":
   #  check length of arguments
   if len(sys.argv) != 3:
       usage()
    # check first arg is a valid date
   start_date = sys.argv[1]
   try:
       num = int(sys.argv[2])
   except ValueError:
       usage()
  # check that second arg is a valid number (+/-)
   if not valid_date(start_date):
       usage()
  # call day_iter function to get end date, save to x
   end_date = day_iter(start_date, num)
   # print(f'The end date is {day_of_week(x)}, {x}.')
   print(f"The end date is {day_of_week(end_date)}, {end_date}.")
   pass

