test = {
	"name": "test3",
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
					>>> ''.join(bits_of_gray(2)) == '00011110'
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
