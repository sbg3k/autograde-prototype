test = {
	"name": "test3",
	"points": 3,
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
					>>> def errorr(n):
					...	 try:
					...		 return fibSum(n)
					...	 except AssertionError:
					...		 return True
					>>> errorr('a') == True
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
