#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author : Prakash Abraham
#
# This file is part of Potter kata created as part of
# MEDNAX Code Exercises
#
# Potter class to handle the calculation of optimum
# discounts for the set of items with weighted discount
#
#
#

class Potter:

    # Following are constants defined
    # The dictionary of available books and their values
    BOOKS = {'BOOK1':1.0,'BOOK2':2.0, 'BOOK3':3.0, 'BOOK4':4.0, 'BOOK5':5.0}
    PRICE = 8.0
    DISCOUNT = {5:10.0, 4:6.4, 3:2.4, 2:0.8, 1:0}


    # The main init class entrypoint
    def __init__(self):
        self.booksadded = {}

    # The main init class entrypoint
    # providing the list of books and count
    def __init__(self,books):
        self.booksadded = books

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
                returnprice = self.PRICE
        elif type(book) == list:
            returnprice = len(book) * self.PRICE
        else:
            print("Unknown or unexpected Datatype")
        return returnprice


    # Discount for distintive count of items provided
    # for 5 items discount is 10 i.e. 25%
    # for 4 items discount is 6.4 i.e. 20%
    # for 3 items discount is 2.4 i.e. 10%
    # for 2 items discount is 1.6 i.e. 5%
    # for 1 item the discount is 0
    #
    def getDiscount(self, count):
        return self.DISCOUNT[count]

    # Get the discounted price for the books
    # passed to the method
    def getDiscountedPrice(self, books):
        totalPrice = 0.0
        if (len(books) == len(set(books))):
            return (len(books) * self.PRICE) - self.getDiscount(len(books))
        else:
            arrangedSetList = self.getArrangedSets(books)
            return self.getDiscountedPriceForList(arrangedSetList)


    # Need to split the provided list into unique sets
    # for that we hve to iterate through the passed book list
    # and create a new book list with multiple unique sets included
    def getArrangedSets(self, books):
        arrangedSetList = []
        for item in books:
            if len(arrangedSetList) == 0 :
                arrangedSetList.append([item])
            else:
                self.updatedArrangedList(item, arrangedSetList)
        return arrangedSetList


    # place the passed item in correct set so that
    # there wont be any duplicates
    def updatedArrangedList(self, item, arrangedSetList):
        itemArranged = False
        discountDict = {}
        for setitem in arrangedSetList:
            if not (item in setitem):
                setitem.append(item)
                discountDict[self.getDiscountedPriceForList(arrangedSetList)] = setitem
                setitem.remove(item)
                itemArranged = True
        if itemArranged :
            minval = min(discountDict.keys())
            setItem = discountDict.get(minval)
            setItem.append(item)

        if not itemArranged:
            arrangedSetList.append([item])
        return  arrangedSetList


    # Get the total price for the passed list of sets
    # This list is created for finding out optimized price
    def getDiscountedPriceForList(self,arrangedSetList):
        totalPrice = 0.0
        for setItem in arrangedSetList:
            totalPrice = totalPrice + self.getDiscountedPrice(setItem)
        if totalPrice <= 0.0:
            return len(books) * self.PRICE
        else:
            return totalPrice


