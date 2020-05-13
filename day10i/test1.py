test = {
	"name": "test1",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "Student" in dir() and "average" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def errorr():
					...	 try:
					...		 Fortune=Student(2,12,3.0)
					...	 except AssertionError:
					...		 return True
					...	 except:
					...		 return False
					...	 return False
					>>> errorr()
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
