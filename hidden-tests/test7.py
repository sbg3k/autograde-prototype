test = {
	"name": "test7",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
                    "code": r"""
                    >>> 'pathfinder' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> matrix = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
					...           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
					...           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
					...           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
					...           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
					...           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
					...           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
					...           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
					...           [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
					>>> src = (0, 0)
					>>> dest = (3, 4)
					>>> pathfinder(matrix,src,dest)
					11
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
