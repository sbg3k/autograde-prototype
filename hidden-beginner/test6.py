test = {
	"name": "test6",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'Bcalculator' in dir()
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
					>>> error(Bcalculator, -12)==1
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

