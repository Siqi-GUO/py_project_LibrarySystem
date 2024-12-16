class LibrarySystem:
    InstanceMemoryAddress = []
    TotalBranches = 0
    TotalBooksAvailable = 0

    def __init__(self, library_id, branch_name, librarian_name=None, max_borrow_limit=3,
                 book_dic={}):
        """Initializes the LibrarySystem class with library details."""
        if book_dic is None:
            book_dic = {}
        self.library_id = library_id  # id of library
        self.branch_name = branch_name  # name of library
        self.librarian_name = librarian_name  # name of librarian
        self.total_books = len(book_dic)  # total num of books
        self.max_borrow_limit = max_borrow_limit  # borrower max borrow limit at the same time
        self.book_dic = book_dic  # book storage dictionary = (name: num)
        self.borrow_dic = {}  # borrower dictionary
        LibrarySystem.InstanceMemoryAddress.append(self)  # add instance address to recall
        LibrarySystem.TotalBranches += 1  # add 1 branch
        LibrarySystem.TotalBooksAvailable += self.total_books  # add total books num
        print(f'Success: Operation "initialize library" successfully')
        self.display_library_info()  # recall function: display information

    def __del__(self):
        """Destructor for the LibrarySystem class."""
        LibrarySystem.InstanceMemoryAddress.remove(self) # remove instance from InstanceMemoryAddress
        LibrarySystem.TotalBranches -= 1  # del the total number of branches
        LibrarySystem.TotalBooksAvailable -= self.total_books # del the number of books from the total available books
        print(f'Done: Library "{self.branch_name}" (ID: {self.library_id}) has been deleted.')


    def borrow_book(self, book_title, borrower_name):
        """Allows a customer to borrow a book from the library."""
        if book_title not in self.book_dic:  # if book is not in this library
            print(
                f'Error: Operation "borrow book" failed!\nBook "{book_title}" does not exist in library "{self.branch_name}".')
            self.search_book(book_title=book_title)  # find other libraries
        elif self.book_dic[book_title] == 0:  # library have no remain
            print(f'Error: Operation "borrow book" failed!\nAll of "{book_title}" have been borrowed.')
            self.search_book(book_title=book_title)
        elif borrower_name in self.borrow_dic and len(self.borrow_dic[borrower_name]) == 3:  # if exceed borrow limit
            print(
                f'Error: Operation "borrow book" failed!\nYou have reached the maximum borrow limit: {self.max_borrow_limit}.')
        else:  # have book & below limit
            self.book_dic[book_title] -= 1  # borrow successfully
            LibrarySystem.TotalBooksAvailable -= 1  # del 1 total availability
            print(f'Done: Operation "borrow book" successfully. ')
            if borrower_name not in self.borrow_dic:  # if borrower not in dic
                self.borrow_dic[borrower_name] = [book_title]  # create borrower key
            else:
                self.borrow_dic[borrower_name].append(book_title)  # add borrow num
            print(
                f'You can borrow {self.max_borrow_limit - len(self.borrow_dic[borrower_name])} more books before you borrow.')

    def return_book(self, book_title, borrower_name):
        """Allows a customer to return a borrowed book."""
        if len(self.borrow_dic[borrower_name]) == 0 or book_title not in self.borrow_dic[borrower_name]:  # borrow is 0
            print(f'Error: Operation "return book" failed! You have not borrowed this!')
        else:  # borrow is not 0
            self.book_dic[book_title] += 1  # add 1 book
            LibrarySystem.TotalBooksAvailable += 1  # add 1 total availability
            del self.borrow_dic[borrower_name][self.borrow_dic[borrower_name].index(book_title)]
            print(f'Done: Operation "return book" successfully.')
            print(
            f"You've just released 1 quota, and you can borrow {self.max_borrow_limit - len(self.borrow_dic[borrower_name])} more books now.")

    def search_book(self, book_title):
        """Searches for a book in the library's collection."""
        if book_title not in self.book_dic or self.book_dic[book_title] == 0:  # if book not in dic or num is 0
            print(f'Sorry! This book is unavailable at this library!')
            result = {index.branch_name: index.book_dic[book_title] for index in LibrarySystem.InstanceMemoryAddress
                      if (book_title in getattr(index, "book_dic") and getattr(index, "book_dic")[book_title] > 0)}  # search the other library
            if len(result) > 0:  # have result
                print(f'However, you can find this book at:')
                for name, num in result.items():
                    print(f'Library: {name}, there is/are {num} book(s) you want.')
                print(f'Would you like to go there?')
                return True
            else:  # no result
                print(f'This book is also unavailable at any libraries.')
                return False
        else:  # book in dic and num is greater than 0
            print(f'This book is available at this library. There is/are {self.book_dic[book_title]} of them.')

    def display_library_info(self):
        """Displays the library's details and current inventory."""
        print(f'Success: Operation "display library information" successfully.')
        print(f'Library ID: {self.library_id}')
        print(f'Library Name: {self.branch_name}')
        print(f'Librarian Name: {self.librarian_name}')
        print(f'Total Book Number of Library: {self.total_books}')
        print(f'Maximum Borrow Quota at the Same Time: {self.max_borrow_limit}')

    def manage_inventory(self, book_title, action, quantity):
        """Allows the administrator to add or remove books from the inventory."""
        if action == "set":  # set mode: set quantity
            if book_title not in self.book_dic:
                LibrarySystem.TotalBooksAvailable += quantity  # add total quantity
            else:
                LibrarySystem.TotalBooksAvailable += quantity - self.book_dic[book_title]  # update total quantity
            self.book_dic[book_title] = quantity
            print(f'Done: Operation "manage inventory" successfully. Set {book_title} quantity: {quantity}')
        elif action == "add":  # add mode: add book num
            if book_title not in self.book_dic:  # if book is not in dic
                self.book_dic[book_title] = quantity  # add key & value
            else:  # book is in dic
                self.book_dic[book_title] += quantity  # add dic num
            LibrarySystem.TotalBooksAvailable += quantity  # add total availability
            print(f'Done: Operation "manage inventory" successfully. Add {book_title} quantity: {quantity}. Now have: {self.book_dic[book_title]}')
        elif action == "del":  # del mode: delete book num
            if book_title not in self.book_dic:  # book not in dic
                print(f'Error: Operation "manage inventory" failed. No book {book_title}.')
            elif self.book_dic[book_title] <= quantity:  # num less than del quantity
                print(f'Error: Operation "manage inventory" failed. This book only have {self.book_dic[book_title]}.')
            else:  # book in dic & higher than del quantity
                self.book_dic[book_title] -= quantity  # del dic num
                LibrarySystem.TotalBooksAvailable -= quantity  # del total availability
                print(f'Done: Operation "manage inventory" successfully. Delete {book_title} quantity: {quantity}. Now have: {self.book_dic[book_title]}')
