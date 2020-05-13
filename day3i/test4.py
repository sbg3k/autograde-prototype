test = {
	"name": "test4",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'stof' in dir() and 'stoi' in dir() and 'ftos' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
				{
					"code": r"""
					>>> def error(i):
					...	 try:
					...		 ftos(i)
					...	 except:
					...		 return True
					...	 return False
					>>> error('12345')
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
