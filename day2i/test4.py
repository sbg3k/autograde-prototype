test = {
	"name": "test4",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'termino' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> termino('(((())()(()((((((())())())((()()(())(())())()((()(())()(((())))(((())()(()(()((()((())))))(()((()()(')
					50
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
