test = {
	"name": "test6",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "fibSum" in dir()
					True
					>>> fibSum.__doc__ != None
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