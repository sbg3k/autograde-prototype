test = {
	"name": "test2",
	"points": 3,
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
					>>>  fastSum(12330900)==76025553570450 # 3 points
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
