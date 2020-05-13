test = {
	"name": "test4",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> "fibSum" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> fibSum(100) == 44
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
