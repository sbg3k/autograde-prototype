test = {
	"name": "test7",
	"points": 3,
	"hidden": False,
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
                    >>> fastSum(121344566)==7362251909536461 # 3 points
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
