test = {
	"name": "test6",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'Person' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
				{
					"code": r"""
					>>> def error(f, num):
					...     try:
					...             f(num)
					...     except AssertionError:
					...             return 1
					>>> error(Person('name', 12).addAge, 12)
					>>> error(Person('name', 12).addAge, 12) == 'name will be 24 in the next 12 years'
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

