test = {
	"name": "test1",
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
					>>>  fastSum(134930284)==9103090837625470 # 3 points
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
