test = {
	"name": "test1",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "fibSum" in dir()
					True
					>>> fibSum(10) == 10
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
