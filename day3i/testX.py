test = {
	"name": "testX",
	"points": 3,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'stof' in dir() and 'stoi' in dir() and 'itos' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> stoi('12345679')-stof('-345.679')+stoi(itos(123456789))
					135802813.679
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
