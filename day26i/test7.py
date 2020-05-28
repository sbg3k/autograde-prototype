test = {
    "name": "test7",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'mergesort' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(array):
                    ...     try:
                    ...         x=  mergesort(array)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    >>> array = [91, 4, 88, 36, 24, 59, 39, 81, 52, 71, 40, 48, 21, 43, 19, 90, 66, 24, 1, 57, 30, 18, 41, 49, 80, 52, 27, 56, 81, 66, 28, 23]
                    >>> errorr(array) == [1, 4, 18, 19, 21, 23, 24, 24, 27, 28, 30, 36, 39, 40, 41, 43, 48, 49, 52, 52, 56, 57, 59, 66, 66, 71, 80, 81, 81, 88, 90, 91]
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
