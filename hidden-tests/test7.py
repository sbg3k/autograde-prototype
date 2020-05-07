test = {
	"name": "test7",
	"points": 2,
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
					>>> order([1,100,1000,1002])
					(0, [1, 100, 1000, 1002])
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