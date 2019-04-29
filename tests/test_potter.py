#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of Potter kata tests
#
# Unit testing the Potter class
#
#
######################################

import pytest
from ..potter.Potter import Potter

@pytest.fixture()
def potter():
    books = {}
    potter = Potter(books)
    return potter

# Test to check whether we can add
# books with price to the Potter object
def test_canAddBook(potter):
    potter.addBook(potter.BOOKS["BOOK1"],8)

# Test the actual price allocated for the book
# Each book is cost $8. The method can take single book parameter
# and a book of array also
def test_basicsPrice(potter):
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK1"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK2"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK3"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK4"])
  assert 8.0 == potter.getPrice(potter.BOOKS["BOOK5"])
  assert 8.0 * 3 == potter.getPrice([potter.BOOKS["BOOK5"], potter.BOOKS["BOOK4"],potter.BOOKS["BOOK3"]])

# Test the discount amount provided for the different sets of
# items based on the count
def test_getDiscountItems(potter):
    assert 10.0 == potter.getDiscount(5)
    assert 6.4 == potter.getDiscount(4)
    assert 2.4 == potter.getDiscount(3)
    assert 0.8 == potter.getDiscount(2)
    assert 0 == potter.getDiscount(1)

# Test the discount amount provided for the different sets of
# items based on the count. We should get the discounted price
# for the array passed
def test_simpleDiscounts(potter):
  assert 8 * 2 * 0.95 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK2"]])
  assert 8 * 3 * 0.9 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK3"] ,potter.BOOKS["BOOK5"]])
  assert 8 * 4 * 0.8 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"],potter.BOOKS["BOOK2"],potter.BOOKS["BOOK3"],potter.BOOKS["BOOK5"]])
  assert 8 * 5 * 0.75 == potter.getDiscountedPrice([potter.BOOKS["BOOK1"], potter.BOOKS["BOOK2"], potter.BOOKS["BOOK3"], potter.BOOKS["BOOK4"], potter.BOOKS["BOOK5"]])

