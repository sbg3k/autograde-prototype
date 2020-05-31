test = {
	"name": "test2",
	"points":  3 ,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> "k_largest" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> k_largest([3, 555, 2, 11, 444, 12, 24, 42, 244], 5)==24 # 3 points
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