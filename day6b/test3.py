test = {
	"name": "test3",
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
					>>> primeSum(30) == 129
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
