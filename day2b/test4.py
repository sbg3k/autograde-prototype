test = {
	"name": "test4",
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
					>>> missing_numbers([2, 6, 10, 4, 11, 15, 19]) == [3, 5, 7, 8, 9, 12, 13, 14, 16, 17, 18] # 3 points
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
