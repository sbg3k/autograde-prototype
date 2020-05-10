test = {
	"name": "test9",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> assert "Student" in dir() and "average" in dir()
					>>> a=[21, 42, 24, 34, 21, 21, 27, 35, 20, 20, 30, 37, 28, 45, 42, 29, 27, 25, 34, 41]
					>>> w=[51.48, 57.03, 51.96, 58.76, 41.68, 53.98, 41.34, 42.65, 41.04, 43.01, 43.01, 49.26, 48.09, 47.98, 52.71, 44.95, 56.7, 36.98, 54.85, 36.64]
					>>> h=[3.9, 5.0, 5.5, 7.8, 8.9, 4.1, 8.2, 7.5, 3.9, 6.8, 5.1, 8.5, 4.6, 5.2, 3.9, 7.8, 8.7, 5.1, 4.3, 9.0]
					>>> arr=[]
					>>> for i in range(20):
					...	 arr.append(Student(a[i],w[i],h[i]))
					>>> average(arr)
					(40.15, 77.71, 7.55)
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
