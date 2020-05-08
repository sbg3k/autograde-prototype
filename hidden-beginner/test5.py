test = {
	"name": "test5",
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
					...     return fastSum(50505050)
					... 
					>>> run_with_limited_time(fastSum, (50505050,), {}, 5) == 1275380063003775
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
