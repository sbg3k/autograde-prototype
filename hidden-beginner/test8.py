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
DAY 20 TEST CASE
1 point for submission
create_arr(3, 5)==[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] # 2 points
create_arr(1, 3)==[[0, 0, 0]] # 2 points
create_arr(4, 13)==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]] # 3 points
create_arr.__doc__ != # 1 point
def error(func, num, n):
   try:
       return func(num, n)
   except AssertionError:
       return 1
error(create_arr, 'a', -1)==1 # 3 points
error(create_arr, -1, -2) ==1 #3points
