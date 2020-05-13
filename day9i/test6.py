test = {
	"name": "test6",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> 'sparsify' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def errorr(n):
					...	 try:
					...		 x=sparsify(n)
					...	 except AssertionError:
					...		 return True
					...	 except:
					...		 return False
					...	 else:
					...		 return x
					>>> errorr({'0': {'1':1}, '1':{'2':2}, '2':{'0':1}, '3':{}})
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
