test = {
	"name": "test5",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "Triangle_no" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def error(num):
					...     try:
					...             Triangle_no(num)
					...     except AssertionError:
					...             return 1
					>>> error(-199)==1 # 3 points
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