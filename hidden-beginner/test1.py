test = {
	"name": "test1",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> callable(k_largest)
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> k_largest([7, 4, 6, 3, 9, 1], 2) == 7 # 2 points
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
