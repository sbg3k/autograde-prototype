test = {
	"name": "test6",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "order" in dir()
					True
					>>> order([1, 4, 2]) == (2, [4])
					True
					>>> order.__doc__ != None
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