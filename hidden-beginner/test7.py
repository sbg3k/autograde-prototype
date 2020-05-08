test = {
	"name": "q2",
	"points": 8,
	"hidden": False,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> from multiprocessing import Process
					>>> from time import sleep
					>>> def run_with_limited_time(func, args, kwargs, time):
					...     p = Process(target=func, args=args, kwargs=kwargs)
					...     p.start()
					...     p.join(time)
					...     if p.is_alive():
					...         p.terminate()
					...         return False
					...     return True
					... 
					>>> run_with_limited_time(main, (123433400, 25002342456), {}, 1.0) and main(123433400, 25002342456) == 8
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
