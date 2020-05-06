test = {
	"name": "test1",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> even_odd(range(10, 35))=='number of even numbers is 13.\n number of odd numbers is 12.'
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
