test = {
	"name": "test7",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "fibonacci" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> try:
					...	 a = False
					...	 x = fibonacci(-5)
					...	 a = True
					...	 if isinstance(x, str) or isinstance(x, bool):
					...		 a = False
					... except:
					...	 a == True
					False
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
