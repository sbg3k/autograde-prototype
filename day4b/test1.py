## DAY 1 TEST CASE
is_perfect_square(9) == True # 3 points <br>
is_perfect_square(100) ==True # 3 points<br>
is_perfect_square(225)==True # 3 points<br>
is_perfect_square(500)==False # 3 points<br>
is_perfect_square.__doc__ != None  # 2 points<br>

## DAY 2 TEST CASE
missing_numbers([1,2,3,4,6,7,10]) ==[5, 8, 9] # 3 points
missing_numbers([10,11,12,14,17])==[13, 15, 16] # 3 points
missing_numbers([2, 3, 5, 1, 6, 4, 12, 8, 20])==[7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19] # 3 points<br>
missing_numbers([2, 6, 10, 4, 11, 15, 19])==[3, 5, 7, 8, 9, 12, 13, 14, 16, 17, 18] # 3 points<br>
missing_numbers.__doc__ != None # 2 points<br>
                                
## DAY3 TEST CASE
even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18])=='number of even numbers is 6\nnumber of odd numbers is 5' # 4 points<br>
even_odd(range(10, 35))=='number of even numbers is 13\nnumber of odd numbers is 12' # 4 points<br>
even_odd.__doc__ != None # 2 points<br>
even_odd([5, 6, 1, 3, 9])=='number of even numbers is 1\nnumber of odd numbers is 4' # 4 points<br>


## DAY 4 TEST CASE
string_test('The quick Brown Fox')=='Number of Lowercase letters is 13.\nNumber of Uppercase letters is 3.' # 4 points<br>
string_test('My name is Sodiq Agunbiade, I am your tutor for this cohort')=='Number of Lowercase letters is 43.\nNumber of Uppercase letters is 4.' # 4 points<br>
string_test('You are a Student of 30daysofcode'=='Number of Lowercase letters is 24.\nNumber of Uppercase letters is 2.' # 4 points<br>
string_test.__doc__ != None # 2 points<br>

## DAY 5 TEST CASE
unique([1,2,3,3,3,3,4,5])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5]\nUnique List: [1, 2, 3, 4, 5]' # 4 points<br>
unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44]\nUnique List: [1, 2, 3, 4, 5, 6, 11, 22, 33, 44]' # 4 points<br>
unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 5, 3, 3, 3, 3, 4, 5, 6, 6, 110, 20, 19, 34]\nUnique List: [1, 2, 3, 4, 5, 6, 19, 20, 34, 110]' # 4 points<br>
unique.__doc__ != None # 2 points<br>
