test = {
	"name": "test6",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "averageMultiple" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> round(averageMultiple(198), 5) == 98.57143
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
