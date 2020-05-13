test = {
	"name": "test6",
	"points": 1,
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
					>>> len(k_largest.__doc__) >= 15
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
