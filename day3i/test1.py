test = {
	"name": "test1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'stof' in dir() and 'stoi' in dir() and 'itos' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def error(s):
					...	 try:
					...		 a=stoi(s)
					...	 except:
					...		 return True
					...	 return False		 		
					>>> error(123)==True
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
