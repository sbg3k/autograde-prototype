test = {
	"name": "test4",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "Student" in dir() and "average" in dir()
					True
					>>> a=[40,22,15,43,39]
					>>> w=[22.45,45.67,44.90,67.29,74.08]
					>>> h=[3.5,6.7,2.8,5.6,8,7]
					>>> h=[3.5,6.7,2.8,5.6,8.7]
					>>> for i in range(5):
					...	 New=Student(a[i],w[i],h[i])
					...	 New.info()
					(40, 1.83)
					(22, 1.02)
					(15, 5.73)
					(43, 2.15)
					(39, 0.98)
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
