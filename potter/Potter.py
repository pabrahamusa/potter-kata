#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of Potter kata
#
# Potter class to handle the calculation of optimum
# discounts for the set of items with weighted discount
#
#
#

class Potter:
    pass

    #The dictionary of available books and their values
    BOOKS = {'BOOK1':1.0,'BOOK2':2.0, 'BOOK3':3.0, 'BOOK4':4.0, 'BOOK5':5.0}
    PRICE = 8.0


    # The main init class entrypoint
    def __init__(self):
        self.booksadded = {}

    # Add new book to the class with price
    # the discounts will be calculated on the
    # books added via this method
    def addBook(self, book, price):
        pass

    # Add new book to the class with price
    # the discounts will be calculated on the
    # books added via this method
    def getPrice(self, book):
        returnprice = 0.0
        if type(book) == float:
            if book in self.BOOKS.values():
                print(" book is " , book)
                returnprice = self.PRICE
        elif type(book) == list:
            print("doing list")
            returnprice = len(book) * self.PRICE
        else:
            print("Unknown or unexpected Datatype")
        return returnprice





