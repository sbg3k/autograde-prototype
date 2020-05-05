test = {
	"name": "test2",
	"points": 3,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> def errorr(s):
					...     try:
					...         wedding_chow(s)
					...     except AssertionError:
					...         return 1
					>>> errorr(['r','s','d','m','f'])==1
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

