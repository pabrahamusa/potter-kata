# Potter kata in Python

This is a Python based TDD driven solution to the Potter katka.

Author : Prakash Abraham

This project tried to cover the best practices for Python project
development as a whole. The development tool used is PyCharm and the test unit is PyTest (pytest-4.4.1). This is developed in Python3 (Python 3.7.3) VirtualEnvironment
installed on MacOS Mojave


Problem Description
-------------
Once upon a time there was a series of 5 books about a very English hero called Harry. (At least when this Kata was invented, there were only 5. Since then they have multiplied) Children all over the world thought he was fantastic, and, of course, so did the publisher. So in a gesture of immense generosity to mankind, (and to increase sales) they set up the following pricing model to take advantage of Harry’s magical powers.

One copy of any of the five books costs 8 EUR. If, however, you buy two different books from the series, you get a 5% discount on those two books. If you buy 3 different books, you get a 10% discount. With 4 different books, you get a 20% discount. If you go the whole hog, and buy all 5, you get a huge 25% discount.

Note that if you buy, say, four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs 8 EUR.

Potter mania is sweeping the country and parents of teenagers everywhere are queueing up with shopping baskets overflowing with Potter books. Your mission is to write a piece of code to calculate the price of any conceivable shopping basket, giving as big a discount as possible.





#### TestCases covered:

    |           Test Cases Scenarios          | Implemented |
    | --------------------------------------- | ------------- |
    | Can create an instance of Potter class  |      Y        |
    | Can add the book, its count & price     |      Y        |
    | Can check basic price                   |      Y        |
    | Can get discount for items              |      Y        |
    | Can calculate simple discounts          |      Y        |
    | Can calculate Multiple discounts        |      Y        |
    | Can calculate discount for Edge cases   |      Y        |

#### The Discounts based on item count 


    For 5 books there will be 25% off i.e. $10
    For 4 books there will be 20% off i.e. $6.4
    For 3 books there will be 10% off i.e. $2.4
    For 2 books there will be 5% off  i.e. $1.6
    For 1 book there will be 0% off i.e.  $0





    

#Executing the code

Environment Setup
-------------

Make sure Python environment is setup on you Mac


####Setup Python3 

```javascript
a) Install python pip

    sudo easy_install pip
    sudo pip install --upgrade pip


b) Install python3 on MacOS (laptop)

    brew install python3
    Python has been installed at
    /usr/local/bin/python3
    Add the following line to your ~/.profile file
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH

c) Virtualenv for python 3
    python3 -m venv pytest_3_prakashvenv
    source ./pytest_3_prakashvenv/bin/activate
    pip install pytest

```

#### Using the Potter Python class

 ```javascript
 a) git checkout https://github.com/pabrahamusa/potter-kata
 b) go to potter-kata/ folder
 c) run command "Python usage_potter.py"
 d) To enter new value for the books list array change it inside the script
    and execute the script again
     
     books = [1,1,2,2,3,3,4,5] 
     books = [1,1,2,2,3,3,4,5,5,5] 

```

#### Execute Python Tests 

```javascript
 a) Go to potter-kata/tests
 b) execute command "pytest -vs"


```


####Python Tests Results from PyTest

```javascript
================================================================================================== test session starts ==================================================================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- /Users/prakashabraham/MEDNAX/python3/pytest_3_prakashvenv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/prakashabraham/MEDNAX/python3/pytest_3_prakashvenv/pytest_work/potter/tests
collected 6 items                                                                                                                                                                                                       

test_potter.py::test_canAddBook PASSED
test_potter.py::test_basicsPrice PASSED
test_potter.py::test_getDiscountItems PASSED
test_potter.py::test_simpleDiscounts PASSED
test_potter.py::test_severalDiscounts PASSED
test_potter.py::test_edgeCasesDiscounts PASSED

=============================================================================================== 6 passed in 0.03 seconds ================================================================================================
(pytest_3_prakashvenv) Prakashs-MacBook-Pro-2:tests prakashabraham$ 


```


