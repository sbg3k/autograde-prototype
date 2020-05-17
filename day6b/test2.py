test = {
	"name": "test2",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "primeSum" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> len(primeSum.__doc__) > 15
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
