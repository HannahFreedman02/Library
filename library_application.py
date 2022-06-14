from library_definitions import Book
from library_definitions import Customer
from library_definitions import Library


class Application:

    '''
    '''
    def __init__(self):
        
        self.library = Library()

        while True:
            print('\n')
            print('Welcome to the Library!')
            print('What would you like to do? Press a corresponding number: ')
            print('1 Add a new book')
            print('2 Add a new customer')
            print('3 Print all books')
            print('4 Print all customers')
            print('5 Find a book by name')
            print('6 Find a book by name of author')
            print('7 Find a customer')
            print('8 Add a book to a customers account')
            print('9 Print all books for a customer')
            print('-1 Leave Library')
            print('\n')



            userInput = input()
            if userInput == '-1':
                break

            elif userInput == '1':
                self.library.addNewBook()

            elif userInput == '2':
                self.library.addNewCustomer()

            elif userInput == '3':
                self.library.printAllBooks()
            
            elif userInput == '4':
                self.library.printAllCustomers()

            elif userInput == '5':
                book = self.library.findBookByName()
                if book == None:
                    print('Book not found!')
                else:
                    print(book.bookName)

            elif userInput == '6':
                book = self.library.findBookByAuthor()
                if book == None:
                    print('Book not found!')
                else:
                    print(book.authorName)

            elif userInput == '7':
                customer = self.library.findCustomer()
                if customer == None:
                    print('Customer not found!')

            elif userInput == '8':
                self.library.addBookToCustomer()


           