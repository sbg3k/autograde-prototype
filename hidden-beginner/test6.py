test = {
	"name": "test6",
	"points": 3,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "fastSum" in dir()
					True
					>>> from multiprocessing import Process
					>>> def run_with_limited_time(func, args, kwargs, time):
					...     p = Process(target=func, args=args, kwargs=kwargs)
					...     p.start()
					...     p.join(time)
					...     if p.is_alive():
					...         p.terminate()
					...         return False
					...     return fastSum(999_999_999_999_999)
					... 
					>>> run_with_limited_time(fastSum, (999_999_999_999_999,), {}, 5) == 499999999999999500000000000000
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
