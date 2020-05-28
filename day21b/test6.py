test = {
	"name": "test6",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'var_sort' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
				{
					"code": r"""
					>>> def error(f, *num):
					...     try:
					...             return f(*num)
					...     except AssertionError:
					...             return 1
					>>> error(var_sort, ('Jane', 11, 2),  ('Bame', 12, 34), ('Tom', 12, 22))==[('Bame', 12, 34), ('Jane', 11, 2), ('Tom', 12, 22)]
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

