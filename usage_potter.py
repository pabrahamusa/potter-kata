#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author : Prakash Abraham
#
# This file is part of Potter kata created as part of
# MEDNAX Code Exercises
#
# This is just a temporary simple class to shows
# that Potter class can be integrated with other classes
#
#
from potter.Potter import Potter


books = [1,1,2,2,3,3,4,5]

potter_obj = Potter(books)

print(potter_obj.getDiscountedPrice(None))