test = {
	"name": "test7",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "to_base" in dir()
					True
					>>> def errorr(n,b):
					...	 try:
					...		 x=to_base(n,b)
					...	 except AssertionError:
					...		 return True
					...	 except:
					...		 return False
					...	 else:
					...		 return x
					>>> import inspect
					>>> errorr('2',6) and '%' not in inspect.getsource(to_base)
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