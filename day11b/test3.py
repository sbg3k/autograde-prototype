test = {
    "name": "test3",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'squareSum' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> try:
                    ...	 x = squareSum(-19)
                    ...	 res = isinstance(x, str) or isinstance(x, bool)
                    ... except:
                    ...	 res = True
                    >>> res == True
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
