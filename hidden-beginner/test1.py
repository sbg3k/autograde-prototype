test = {
	"name": "test1",
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
					>>> error(var_sort, ('old', 10, 12), ('Old', 10, 12), ('name', 17, 20))==[('Old', 10, 12), ('name', 17, 20), ('old', 10, 12)] # 2 pointss
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

