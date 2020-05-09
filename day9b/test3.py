test = {
	"name": "test3",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "fibSum" in dir()
					True
					>>> def errorr(n):
					...	 try:
					...		 x=fibSum(n)
					...	 except:
					...		 return True
					...	 else:
					...		 return type(x) == str or x == 0
					>>> errorr('a')
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
