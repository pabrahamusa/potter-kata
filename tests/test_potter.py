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
    potter = Potter()
    return potter

# Test to check whether we can instantiate the
# Main Potter Class
def test_canInstantiatePotter():
    potter = Potter()

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
