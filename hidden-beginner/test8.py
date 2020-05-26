test = {
	"name": "test8",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> 1 == 1
					True
					""",
					"hidden": False,
					"locked": False,
				},
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}
[5/6, 7:15 AM]TEST CASE For day1

is_perfect_square(1000)==False # 2 points
is_perfect_square(500)==False # 2 points
is_perfect_square(9801)==True # 3 points
is_perfect_square(10201)==True # 3 points
is_perfect_square(10203)==True # 3 points
len(is_perfect_square.__doc__) > 15 # 2 points
[5/6, 7:15 AM]TEST CASE For day3

even_odd(range(10, 35))=='number of even numbers is 13.\n number of odd numbers is 12.' # 4 points
even_odd([5, 6, 9, 10, 12, 105, 999, 46])=='number of even numbers is 4.\n number of odd numbers is 4.' # 4 points
even_odd([1, 3, 5, 7, 9])=='number of even numbers is 0.\n number of odd numbers is 5.' # 4 points
len(even_odd.__doc__) > 30 # 2 points
even_odd.__doc__ != None # 1 point
[5/6, 7:16 AM]TEST CASE For day 4
string_test('akdks @2 cbd Nsjswnq QWE e 45')== 'Number of Lowercase letters is 15.\n Number of Uppercase letters is 4. # 4 points
string_test('hjsfdKLDSKGkjdkj3498320vkml ew;m;bt3')=='Number of Lowercase letters is 19.\n Number of Uppercase letters is 6. # 4 points
string_test('dlafa qwfh ioefi   KJASkdkjfre qwiofbv AR25632')==Number of Lowercase letters is 28.\n Number of Uppercase letters is 6. # 4 points
len(string_test.__doc__) > 30 # 2 points
string_test.__doc__ != None #  1 point
[5/6, 7:35 AM]TEST CASE For day5

unique([1, 3, 5, 6, 2, 5, 1, 4, 6, 1, 4, 3, 2, 1]) == Sample List: [1, 3, 5, 6, 2, 5, 1, 4, 6, 1, 4, 3, 2, 1] \n Unique List: [1, 2, 3, 4, 5, 6] # 5 points
unique([67, 34, 56, 34, 56, 23, 12, 67, 34, 89, 65, 12, 23, 34, 12, 23]) == Sample List: [67, 34, 56, 34, 56, 23, 12, 67, 34, 89, 65, 12, 23, 34, 12, 23] \n Unique List: [12, 23, 34, 56, 65, 67, 89] # 5 points
unique.__doc__ != None # 1 point
len(unique.__doc__) > 30 # 2 points
Add extra two points, so anyone that submits get two points automaticall.
