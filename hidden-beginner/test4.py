test = {
	"name": "test4",
	"points": 3 ,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> "Complex" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> Complex(1, 3).div(Complex(2, 4)).dict=={'real': -1.17, 'imaginary': -0.17} #3 points
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