test = {
	"name": "test3",
	"points": 3,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'missing_numbers' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> missing_numbers([2, 3, 5, 1, 6, 4, 12, 8, 20]) == [7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19] # 3 points
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
