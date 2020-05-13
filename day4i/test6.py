test = {
	"name": "test6",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'bits_of_gray' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> bits_of_gray.__doc__ !=None
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
