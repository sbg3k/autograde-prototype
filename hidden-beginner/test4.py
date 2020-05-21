test = {
	"name": "test4",
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
					...             f(*num)
					...     except AssertionError:
					...             return 1
					>>> error(var_sort, ('ade', 11, 2), ('ade', 10, 12), ('ade', 11, 3))==[('ade', 10, 12), ('ade', 11, 2), ('ade', 11, 3)] # 2 points
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

