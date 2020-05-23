test = {
    "name": "test10",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'my_exes' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(l,n):
                    ...     try:
                    ...         x=my_exes(l,n)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> matrix = [[1, 1, 1, 0, 0, 0, 0, 1],
                    ...     [1, 1, 0, 0, 1, 0, 1, 1],
                    ...     [1, 0, 1, 0, 0, 1, 1, 1],
                    ...     [1, 0, 0, 2, 0, 1, 0, 1],
                    ...     [0, 1, 1, 0, 0, 0, 1, 0],
                    ...     [1, 1, 1, 0, 1, 1, 0, 1],
                    ...     [1, 0, 1, 1, 1, 0, 1, 1]]
                    >>> errorr(matrix)
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

	
