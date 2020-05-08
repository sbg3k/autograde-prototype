test = {
    "name": "test7",
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
					...     return True
					... 
					>>> run_with_limited_time(fastSum, (8_192_892_819_891_112_282_728_282), {}, 0.0004)
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
