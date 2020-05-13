test = {
    "name": "test6",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'wedding_chow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import time	
                    >>> def chow(supplies):
                    ...     food = 'rsmfd'
                    ...     ounje = ''.join(filter(lambda x: x in food, supplies))
                    ...     v = min([ounje.count(i) for i in 'rsmfd'])
                    ...     for i in food:
                    ...         ounje = ounje.replace(i, '', v)
                    ...     return v, ''.join(sorted(ounje, key=food.index))
					>>> alpha = time.time()
                    >>> y = wedding_chow('rsdmfrsdfmrsdfrsfdmmmdfrsrdfffmsdfr')
                    >>> omega = time.time()
                    >>> bound=round(omega-alpha,3)+0.0005
                    >>> start = time.time()
                    >>> x = wedding_chow('rsdmfrsdfmrsdfrsfdmmmdfrsrdfffmsdfr')
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
