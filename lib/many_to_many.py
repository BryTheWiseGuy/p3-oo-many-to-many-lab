class Author:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    def contracts_by_date():
        return sorted(Contract.all, key=lambda contract: contract.date)