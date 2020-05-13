test = {
	"name": "test5",
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
					>>> errorr({"A": (("B",1)), "B":(("C",2)), "C":(("A",1), ("D",1)), "D":()})
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
