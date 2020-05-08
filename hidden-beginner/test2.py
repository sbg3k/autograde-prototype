test = {
	"name": "test2",
	"points": 2,
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
					...     return fastSum(1_000_000_000)
					... 
					>>> run_with_limited_time(fastSum, (1_000_000_000,), {}, 5) == 500000000500000000
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
