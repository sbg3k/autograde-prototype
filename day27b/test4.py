test = {
	"name": "test3",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'Square' in dir()
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
					>>> error(Square, '7') == 1 # 3 points
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

