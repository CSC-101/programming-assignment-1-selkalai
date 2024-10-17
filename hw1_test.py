import data
import hw1
import unittest
from data import Price
from data import Point
from data import Rectangle
from data import Book
from data import Circle
from data import Employee



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "hello, how are you"
        result = hw1.vowel_count(input)
        expected = 7
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "aeiou"
        result = hw1.vowel_count(input)
        expected = 5
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1,2], [3,4,5], [6,7]]
        result = hw1.short_lists(input)
        expected = [[1,2], [6,7]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[2], [97, 6], [-3, -4], []]
        result = hw1.short_lists(input)
        expected = [[97,6], [-3,-4]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs__1(self):
        input = [[3,2], [3,4,5], [90,7]]
        result = hw1.ascending_pairs(input)
        expected = [[2,3], [3,4,5],[7,90]]
        self.assertEqual(expected, result)

    def test_ascending_pairs__2(self):
        input = [[3,-10], [8,10,7], [], [6,7], [9]]
        result = hw1.ascending_pairs(input)
        expected = [[-10,3], [8,10,7], [], [6,7], [9]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        price_1 = Price(3,80)
        price_2 = Price(4, 50)
        result = hw1.add_prices(price_1, price_2)
        expected = Price(8, 30)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        price_1 = Price(10,99)
        price_2 = Price(1, 25)
        result = hw1.add_prices(price_1, price_2)
        expected = Price(12, 24)
        self.assertEqual(expected, result)

    def test_add_prices_3(self):
        price_1 = Price(7, 99)
        price_2 = Price(1, 0)
        result = hw1.add_prices(price_1, price_2)
        expected = Price(8, 99)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        top_left_coord = Point(6,4)
        bottom_right_coord = Point(10,0)
        input = Rectangle(top_left_coord, bottom_right_coord)
        result = hw1.rectangle_area(input)
        expected = 16
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        top_left_coord = Point(17,9)
        bottom_right_coord = Point(25,6)
        input = Rectangle(top_left_coord, bottom_right_coord)
        result = hw1.rectangle_area(input)
        expected = 24
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        book_one = Book(["J.K Rowling"], "Harry Potter and the Chamber of Secrets")
        book_two = Book(["Suzanne Collins"], "The Hunger Games")
        book_three = Book(["Suzanne Collins"], "Catching Fire")
        list_of_books = book_one, book_two, book_three
        result = hw1.books_by_author("Suzanne Collins", list_of_books)
        expected = [Book(['Suzanne Collins'], 'The Hunger Games'), Book(['Suzanne Collins'], 'Catching Fire')]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        book_one = Book(["J.K Rowling"], "Harry Potter and the Chamber of Secrets")
        book_two = Book(["J.K Rowling"], "Harry Potter and the Half-Blood Prince")
        book_three = Book(["Suzanne Collins"], "Catching Fire")
        list_of_books = book_one, book_two, book_three
        result = hw1.books_by_author("J.K Rowling", list_of_books)
        expected = [Book(['J.K Rowling'], 'Harry Potter and the Chamber of Secrets'), Book(['J.K Rowling'], 'Harry Potter and the Half-Blood Prince')]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        top_left_coord = Point(2, 10)
        bottom_right_coord = Point(6, 7)
        input = Rectangle(top_left_coord, bottom_right_coord)
        result = hw1.circle_bound(input)
        expected = Circle(Point(4, 8.5), 2.5)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        top_left_coord = Point(5, 20)
        bottom_right_coord = Point(10, 8)
        input = Rectangle(top_left_coord, bottom_right_coord)
        result = hw1.circle_bound(input)
        expected = Circle(Point(7.5, 14), 6.5)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        employee_one = Employee("Sam", 100000)
        employee_two = Employee("Alex", 300000)
        employee_three = Employee("Sarah", 90000)
        employee_four = Employee("Jess", 200000)
        list_of_employees = [employee_one, employee_two, employee_three, employee_four]
        result = hw1.below_pay_average(list_of_employees)
        expected = ['Sam', 'Sarah']
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        employee_one = Employee("Sam", 1000000)
        employee_two = Employee("Alex", 300000)
        employee_three = Employee("Sarah", 90000)
        employee_four = Employee("Jess", 200000)
        list_of_employees = [employee_one, employee_two, employee_three, employee_four]
        result = hw1.below_pay_average(list_of_employees)
        expected = ['Alex', 'Sarah', 'Jess']
        self.assertEqual(expected, result)

    def test_below_pay_average_3(self):
        list_of_employees = []
        result = hw1.below_pay_average(list_of_employees)
        expected = []
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
