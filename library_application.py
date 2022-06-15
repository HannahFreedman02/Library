from library_definitions import Book
from library_definitions import Customer
from library_definitions import Library

'''
'''
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
            print('9 Print all books of customer')
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
                print('\nPlease enter title of book: ')
                bookName = input()
                book = self.library.findBookByName(bookName)
                if book == None:
                    print('Book not found!')
                else:
                    print(book.bookName + ' by ' + book.author.authorFullName)

            elif userInput == '6':
                print('\nPlease enter name of author: ')
                authorFullName = input()
                book = self.library.findBookByAuthor(authorFullName)
                if book == None:
                    print('Book not found!')
                else:
                    print(book.bookName + ' by ' + book.author.authorFullName)

            elif userInput == '7':
                print('\nPlease enter customers full name: ')
                customerFullName = input()
                customer = self.library.findCustomer(customerFullName)
                if customer == None:
                    print('Customer not found!')
                else:
                    print(customer.customerFullName)

            elif userInput == '8':
                print('\nPlease enter the name of the book you would like to add: ')
                bookName = input()
                print('\nPlease enter the name of the cutomer you would like to add the book to: ')
                customerFullName = input()
                book = self.library.findBookByName(bookName)
                if book == None:
                    print('Book not found!')
                else:
                    customer = self.library.findCustomer(customerFullName)
                    if customer == None:
                        print('Customer not found!')
                    else:
                        customer.addBookToCustomer(book)                        
            
            elif userInput == '9':
                print('\nPlease enter name of customer: ')
                customerFullName = input()
                customer = self.library.findCustomer(customerFullName)
                if customer == None:
                    print('Customer not found!')
                else:
                    listOfBooks = customer.getListOfBooks()
                    self.printAllBooksOfCustomer(listOfBooks)

                    


    '''
    '''
    def printAllBooksOfCustomer(self, p_listOfBooks):
        print('Here are your list of books: ')
        for book in p_listOfBooks:
            print(book.bookName)

