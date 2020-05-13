test = {
	"name": "test7",
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
					>>> k_largest([1, 59, 38, 248, 4,45, 54234, 456, 35,6233, 25, 6578, 222225, 65, 1123,344,5678,99087,12345], 12)==65
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
