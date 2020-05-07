test = {
	"name": "test2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "order" in dir()
					True
					>>> order([1, 4, 2]) == (2, [4])
					True
					>>> def errorr(s):
					...	 try:
					...		 x=order(s)
					...	 except AssertionError:
					...		 return True
					...	 except:
					...		 return False
					...	 else:
					...		 return x
					...
					>>> errorr([1, 2, 3, 4, 7, 8, 9])
					(4, [7, 8, 9])
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