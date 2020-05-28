test = {
	"name": "test6",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'Point' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
					>>> round((Point(1, 2).__add__(Point(3, 5))).distance(Point(100, 4.6).__sub__(Point(1, 50))), 1)==108.5
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
