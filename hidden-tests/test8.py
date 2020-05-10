test = {
	"name": "test8",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> assert "Student" in dir() and "average" in dir()
					>>> Fortune=Student(23,4.50,6.70)
					>>> Joba=Student(21,45.67,3.40)
					>>> average([Joba,Fortune])
					(32.0, 40.86, 6.16)
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
