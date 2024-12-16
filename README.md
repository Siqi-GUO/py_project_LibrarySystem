_Python Project Code for "Python Programming for Beginners (1002) (Dr. Alexander VASILYEV) [Semester 1 of 2024-2025]"_

_personal_info_

`student_name = "Siqi GUO"`

`student_ID = "2330006046"`


# Final Project
This is your final project. It accounts for a maximum of 20% of the final grade. Read the following instructions carefully.

## Instructions

You should work on this project either individually or in a team of 2 students.
Both students of the team need to submit the project online.

This project will be partially manually graded.
You have a limited time to submit: Monday, 16 December 2023, at 23:59 PM. After the deadline, submission is not possible. Only your last submission counts.

Copying the solution of another student is forbidden. Plagiarized solutions (copied from other sources or other teams) will receive 0 points.

## Project Goal
The goal of this project is to program a Python class that manages a library system for a public library. The class must contain:

- 1 constructor (`__init__`)
- 1 destructor (`__del__`)
- 5 methods
- 2 class attributes
- 5 instance attributes

## Specific Requirements
Create a Python class named LibrarySystem that has the following:

### Constructor

```
def __init__(self, library_id, branch_name, librarian_name, total_books, max_borrow_limit):
    pass
```

### Destructor
```
def __del__(self):
    pass
```

### Class Attributes
```
TotalBranches = 50
TotalBooksAvailable = 1000000
Instance Attributes
library_id
branch_name
librarian_name
total_books
max_borrow_limit
Class Methods
```

You should implement a minimum of 5 methods. Below are some example methods to get you started (you are free to choose your own ideas and method names):

```
def borrow_book(self, book_title, borrower_name):
    pass
```

```
def return_book(self, book_title, borrower_name):
    pass
```

```
def search_book(self, book_title):
    pass
```

```
def display_library_info(self):
    pass
```

```
def manage_inventory(self, book_title, action, quantity):
    pass
```

## Optional (for better points)
To improve your score, you can include the following features:

Add additional instance attributes, such as opening_hours, is_open, borrowed_books, etc.
Add more class attributes, such as LateFeeRate, MaxBookLimitPerCustomer, etc.

Implement error handling:
Raise exceptions when a borrower tries to borrow more books than allowed.

Raise exceptions if a book is not available in the library's collection.

Add meaningful string documentation (docstrings) for your class and methods.

Include detailed return messages for every method, even if the method doesn't necessarily need to return anything.

## Example Requirements
- A method for borrowing books should check availability and update the inventory.
- A method for returning books should update the inventory and calculate any late fees.
- A method for searching books should return the book's availability status.
- A method for managing inventory should let the administrator add or remove books.
- A method for displaying library information should print branch details and book statistics.

## Rules
- The total number of program lines should be above 100.
- You should test your class thoroughly with multiple scenarios.
- Ensure proper formatting, indentation, and readability of the code.

## Dataset Example
The dataset for this project involves a library system. Below is the description of the dataset:

`library_id`: A unique identifier for each library branch (e.g., "L001").

`branch_name`: The name of the library branch (e.g., "Downtown Library").

`librarian_name`: The name of the librarian in charge (e.g., "Alice Johnson").

`total_books`: The total number of books in the library's inventory (e.g., 10,000).

`max_borrow_limit`: The maximum number of books a single customer can borrow at once (e.g., 5).

## Example Class Structure

```
class LibrarySystem:
    
    def __init__(self, library_id, branch_name, librarian_name, total_books, max_borrow_limit):
        """Initializes the LibrarySystem class with library details."""
        pass
    
    def __del__(self):
        """Destructor for the LibrarySystem class."""
        pass
    
    def borrow_book(self, book_title, borrower_name):
        """Allows a customer to borrow a book from the library."""
        pass
    
    def return_book(self, book_title, borrower_name):
        """Allows a customer to return a borrowed book."""
        pass
    
    def search_book(self, book_title):
        """Searches for a book in the library's collection."""
        pass
    
    def display_library_info(self):
        """Displays the library's details and current inventory."""
        pass
    
    def manage_inventory(self, book_title, action, quantity):
        """Allows the administrator to add or remove books from the inventory."""
        pass
```
