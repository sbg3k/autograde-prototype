test = {
	"name": "test3",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> assert "Student" in dir() and "average" in dir()
					>>> Fortune=Student(20,45.50,6.7)
					>>> Joba=Student(19,43.28,8.4)
					>>> Fortune.info()
					(20, 1.01)
					>>> Joba.info()
					(19, 0.61)
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
