test = {
	"name": "test6",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> assert "fibonacci" in dir()
					>>> try:
					...	 a = False
					...	 x = fibonacci('a')
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
