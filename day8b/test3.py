test = {
	"name": "test3",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "fastSum" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
                    "code": r"""
					>>> fastSum.__doc__ != None
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
