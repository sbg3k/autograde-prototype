test = {
	"name": "test2",
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
                    >>> Complex(1, 8).sub(Complex(-2, 4)).dict=={'real': 3, 'imaginary': 4} # 3 points
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