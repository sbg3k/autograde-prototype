test = {
	"name": "test6",
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
					...	 x = fibonacci('a')
					...	 a = True
					...	 if isinstance(x, str) or isinstance(x, bool):
					...		 a = False
					... except:
					...	 a = False
					>>> a == False
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
