test = {
	"name": "test2",
	"points": 4,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'unique' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44]\nUnique List: [1, 2, 3, 4, 5, 6, 11, 22, 33, 44]' # 4 points
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
