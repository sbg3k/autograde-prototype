test = {
	"name": "test2",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'string_test' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> string_test('My name is Sodiq Agunbiade, I am your tutor for this cohort')=='Number of Lowercase letters is 43.\nNumber of Uppercase letters is 4.' # 4 points
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
