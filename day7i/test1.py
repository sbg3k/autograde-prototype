test = {
    "name": "test1",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "my_cars" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> my_cars([2,4,6,8])==12
                    True
                    >>> def errorr(s):
                    ...     try:
                    ...         x=my_cars(s)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> errorr(())==0
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
