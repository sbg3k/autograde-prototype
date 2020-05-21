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

def error(func, *args):
   try:
       return func(*args)
   except AssertionError:
       return 1
error(var_sort, ('Jane', 11, 2),  ('Bame', 12, 34), ('Tom', 12, 22))==[('Bame', 12, 34), ('Jane', 11, 2), ('Tom', 12, 22)] # 2 points
error(var_sort, (1, 1, 1))==1 # 2 points
error(var_sort, ('ade', 11, 2), ('ade', 10, 12), ('ade', 11, 3))==[('ade', 10, 12), ('ade', 11, 2), ('ade', 11, 3)] # 2 points
error(var_sort, ('ade', 2), ('ade', 3, 5)) == 1  # 2 points
error(var_sort, ('ade', 12, 11), ('John', -1, 2))==1 # 2 points
error(var_sort, ('old', 10, 12), ('Old', 10, 12), ('name', 17, 20))==[('Old', 10, 12), ('name', 17, 20), ('old', 10, 12)] # 2 points
error(var_sort, 1) == 1 # 2 points
var_sort.__doc__ != None # 1 point
