test = {
	"name": "test3",
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
					>>> Bcalculator("10111" ,"10011")==42
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
