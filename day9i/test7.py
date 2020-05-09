test = {
	"name": "test7",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> sparsify({"A": {"B":1,'E':2}, "B":{"C":2},'E':{'C':2}, "C":{"A":1, "D":1}, "D":{}})
					[[0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 2, 0, 0, 2], [0, 0, 1, 0, 0], [2, 0, 0, 0, 0]]
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
