test = {
	"name": "test2",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'average' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> a=''
					>>> for i in range(11):
					...  a+=(str(2**i)+' ')
					>>> round(average(a),2)
					186.09
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
