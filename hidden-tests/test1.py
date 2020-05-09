test = {
	"name": "test1",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> x = sparsify({"A": {"B":1}, "B":{"C":2}, "C":{"A":1, "D":1}, "D":{}})
					>>> x[0][2]+ x[1][0]+ x[2][1]+x[3][2] == 5
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
