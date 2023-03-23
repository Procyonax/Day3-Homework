def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

month = {
        "1": 'January',
        "2": 'February',
        "3": 'March',
        "4": 'April',
        "5": 'May',
        "6": 'June',
        "7": 'July',
        "8": 'August',
        "9": 'September',
        "10": 'October',
        "11": 'November',
        "12": 'December',
        }
     
shortmonth = {
        "1": 'Jan',
        "2": 'Feb',
        "3": 'Mar',
        "4": 'Apr',
        "5": 'May',
        "6": 'Jun',
        "7": 'Jul',
        "8": 'Aug',
        "9": 'Sep',
        "10": 'Oct',
        "11": 'Nov',
        "12": 'Dec',
        }  
   
def number_to_full_month_name(num):
    return month[str(num)]

def number_to_short_month_name(num):
    return shortmonth[str(num)]

## Further

def volume_of_cube(length_of_side):
    return length_of_side ** 3

def string_reverse(str):
    string_reversed = ''
    index = len(str)
    while index > 0:
        string_reversed += str[ index - 1 ]
        index = index - 1
    return string_reversed

## ALTNERNATIVE
# def string_reverse(str):
#     ''.join(reversed(str))

def fahrenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * (5.0/9.0)
    return round(celsius, 2)