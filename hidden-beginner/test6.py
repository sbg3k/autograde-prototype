test = {
    "name": "test6",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'make_car' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def error(f, ma, mo, **mgk):
                    ... 	try:
                    ... 		return f(ma, mo, **mgk)
                    ... 	except AssertionError:
                    ... 		return 1
                    ... 	except:
                    ... 		return 2
                    >>> error(make_car, 1, 1, new=True)==1 # 3 points
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
