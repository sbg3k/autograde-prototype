test = {
	"name": "test7",
	"points": 11,
	"hidden": False,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> assert "fastSum" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
                    "code": r"""
                    >>> import time	
                    >>> fastSumm = lambda n: int((n/2)*(1+n))
                    >>> alpha = time.time()
                    >>> y = fastSumm(10_000_000_000)
                    >>> omega = time.time()
                    >>> bound=round(omega-alpha,4)+0.0032
                    >>> start = time.time()
                    >>> x = fastSum(10_000_000_000)
                    >>> end = time.time()
                    >>> diff= end-start
                    >>> diff < bound
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
