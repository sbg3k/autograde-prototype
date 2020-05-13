test = {
	"name": "test3",
	"points": 3,
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
					>>> k_largest([2, 1, -1, 0, 99, 100, 1000, 67, 45, 23, 89, 4, 777, 567, 12,], 8)==45
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
