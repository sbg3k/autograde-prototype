test = {
	"name": "test3",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> a=[str(i) for i in range(100)]
					>>> b=[i for i in range(100)]
					>>> a=' '.join(a)
					>>> round(average(a),2)==round(sum(b)/len(b),2)
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
