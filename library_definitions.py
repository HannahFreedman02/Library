
'''
'''
class Library:


    '''
    '''
    def __init__(self) -> None:
        self.listOfBooks = []
        self.listOfCustomers = []


    '''
    '''
    def startNewLibrary(self):
        self.listOfBooks.clear()

    
    
    '''
    '''
    def addNewBook(self):
        print('\nPlease enter the title of the new book:')
        bookName = input()
    
        print('\nPlease enter the author name:')
        authorFullName = input()
        authorFullName = authorFullName.split(' ')
        authorFirstName = authorFullName[0]
        authorLastName = authorFullName[1]

        author = Author(authorFirstName, authorLastName)
        book = Book(bookName, author)
        self.listOfBooks.append(book)
        


    '''
    '''
    def addNewCustomer(self):
        print('\nPlease enter the customers full name:')
        customerFullName = input()
       
        
        names = customerFullName.split(' ')
        firstName = names[0]
        lastName = names[1]
    
        self.listOfCustomers.append(Customer(firstName, lastName))


    '''
    '''
    def printAllBooks(self):
        for book in self.listOfBooks:
            print(book.bookName)

    

    '''
    '''
    def printAllCustomers(self):
        for customer in self.listOfCustomers:
            print(customer.customerFullName)



    '''
    '''
    def findBookByName(self, p_bookName):
        for book in self.listOfBooks:
            if p_bookName == book.bookName:
                return book
        return None

    
    '''
    '''
    def findBookByAuthor(self, p_authorFullName):
        for book in self.listOfBooks:
            if p_authorFullName == book.author.authorFullName:
                return book
        return None


    '''
    '''
    def findCustomer(self, p_customerFullName):
        for customer in self.listOfCustomers:
            if p_customerFullName == customer.customerFullName:
                return customer
        return None


'''
'''
class Book:


    '''
    '''
    def __init__(self, p_bookName, p_authorObject):
        self.bookName = p_bookName
        self.author = p_authorObject
        


'''
'''
class Author:


    '''
    '''
    def __init__(self, p_authorFirstName, p_authorLastName):
        self.authorFirstName = p_authorFirstName
        self.authorLastName = p_authorLastName
        self.authorFullName = self.authorFirstName + ' ' + self.authorLastName
       

'''
'''
class Customer:


    '''
    '''
    def __init__(self, p_firstName, p_lastName):
        self.firstName = p_firstName
        self.lastName = p_lastName
        self.customerFullName = self.firstName + ' ' + self.lastName
        self.listOfBooks = []
    

    '''
    '''
    def addBookToCustomer(self, p_book):
        self.listOfBooks.append(p_book)


    '''
    '''
    def getListOfBooks(self):
        return self.listOfBooks

