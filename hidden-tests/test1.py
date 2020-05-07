test = {
	"name": "test1",
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
					>>> errorr((100,1,2,3,21,22,23,200,31,32,33,4))
					(4, [21, 22, 23, 31, 32, 33, 100, 200])
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