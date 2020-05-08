test = {
	"name": "test3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "fastSum" in dir()
					True
					>>> fastSum.doc != None
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
