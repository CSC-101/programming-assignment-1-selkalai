import data
import math
from data import Price
from data import Point
from data import Rectangle
from data import Book
from data import Circle
from data import Employee

# Write your functions for each part in the space below.

# Part 1

#function vowel_count takes a string and returns an integer representing the count of the
# number of vowels that are in the string

def vowel_count(x:str)->int:
    x = x.lower()
    vowel_list = ["a", "e", "i", "o", "u"]
    vowel_tally = 0
    for i in x:
        if i in vowel_list:
            vowel_tally += 1
    return vowel_tally

# Part 2

#function short_lists takes argument list[list[int]] and returns a new list with only the elements
# of the input list that have a length of 2 - in the same order.

def short_lists(initial:list[list[int]])->list:
    new_list = []
    for i in initial:
        if len(i) == 2:
            new_list.append(i)
    return new_list

# Part 3

#function ascending_pairs takes argument list[list[int]] and returns a new list with the same
# order of elements but sorts the nested elements in ascending order only if those
# elements have a length of 2

def ascending_pairs(initial:list[list[int]])->list:
    new_list = []
    for i in initial:
        if len(i) != 2:
            new_list.append(i)
        else:
            if i[0] > i[1]:
                new_list.append([i[1], i[0]])
            else:
                new_list.append(i)
    return new_list
# Part 4

#function add_prices takes 2 parameters of type Price(dollars, cents) and returns the sum of these parameters with
# the number of cents being below 100

def add_prices(x:Price,y:Price)->Price:
    cents_sum = x.dollars * 100 + y.dollars * 100 + x.cents + y.cents
    cents = cents_sum % 100
    dollars = cents_sum // 100
    return Price(dollars,cents)


# Part 5

#function rectangle_area takes one parameter of type Rectangle(top_left:Point, right_bottom:Point),
# and returns the area of the rectangle

def rectangle_area(rect:Rectangle)->int:
    top_right_x = rect.bottom_right.x
    top_right_y = rect.top_left.y
    width = top_right_x - rect.top_left.x
    length = top_right_y - rect.bottom_right.y
    area = width * length
    return area

# Part 6

#fuction book_by_author takes in 2 parameters: a str of an authors name and a list of books of type list[Book]
# and then returns a list of all books in the list of books that are written by the input author.

def books_by_author(intended_name:str, book_list:list[Book])->list[Book]:
    correct_author_list = []
    for book in book_list:
        if intended_name in book.authors:
            correct_author_list.append(book)
    return correct_author_list

# Part 7

#function circle_bound takes one parameter of type Rectangle and returns a Circle(center:Point, radius:float)
# that represents the smallest possible bounding circle for the input rectangle

def circle_bound(rect:Rectangle)->Circle:
    top_right_x = rect.bottom_right.x
    top_right_y = rect.top_left.y
    width = top_right_x - rect.top_left.x
    length = top_right_y - rect.bottom_right.y
    diameter = math.sqrt((width**2) + (length**2))
    circle_radius = diameter/2
    x_coord = (rect.top_left.x + rect.bottom_right.x)/2
    y_coord = (rect.top_left.y + rect.bottom_right.y)/2
    center_point = Point(x_coord, y_coord)
    return Circle(center_point, circle_radius)

# Part 8

#function below_pay_average takes one parameter of type list[Employee(name:str, pay_rate:int)] and returns a
# list of names of employees being payed less than the average pay rate of all employees.

def below_pay_average(employee_list:list[Employee])->list[str]:
    below_ave_list = []
    pay_sum = 0
    if len(employee_list) == 0:
        return []
    else:
        for i in employee_list:
            pay_sum += i.pay_rate
        pay_ave = pay_sum/len(employee_list)
        for i in employee_list:
            if i.pay_rate < pay_ave:
                below_ave_list.append(i.name)
        return below_ave_list
