test = {
	"name": "test1",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'even_odd' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18])=='number of even numbers is 6\nnumber of odd numbers is 5' # 4 points
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