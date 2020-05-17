test = {
	"name": "test2",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'single2stupor' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
					>>> single2stupor(783)== 4
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
