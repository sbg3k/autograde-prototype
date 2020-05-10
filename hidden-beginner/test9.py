test = {
	"name": "test9",
	"points": 3,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> assert "fibonacci" in dir()
					>>> evenFib = lambda n: (((5 * n**2+4)**0.5)%1==0 or ((5 * n**2-4)**0.5)%1==0)
					>>> import time
					>>> start = time.time()
					>>> x1 = evenFib(317811)
					>>> end = time.time()
					>>> bound = end-start+0.0005
					>>> alpha = time.time()
					>>> x2 = fibonacci(317811)
					>>> omega = time.time()
					>>> diff = omega - alpha
					>>> diff < bound and x1 == x2
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
