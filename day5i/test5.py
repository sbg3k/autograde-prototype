test = {
	"name": "test5",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'wedding_chow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> wedding_chow('rsmdffdmrsdmrsf')) == (3, '')
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

