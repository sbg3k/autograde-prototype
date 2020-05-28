test = {
	"name": "test3",
	"points":  3 ,
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
                    >>> Complex(1, 3).mul(Complex(2, 4)).dict=={'real': -10, 'imaginary': 10} # 3 points
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