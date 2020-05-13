test = {
	"name": "test5",
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
					>>> k_largest.__doc__ != None 
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
