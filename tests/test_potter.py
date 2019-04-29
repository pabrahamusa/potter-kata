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