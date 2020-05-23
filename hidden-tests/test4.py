test = {
    "name": "test4",
    "points": 2,
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
                    >>> matrix = [[0, 1, 1, 0, 0, 0, 0, 1], 
					... 	[1, 1, 0, 0, 1, 0, 1, 1], 
					... 	[1, 0, 1, 0, 0, 1, 0, 1], 
					... 	[1, 0, 0, min(2,1), 0, 1, 0, 1], 
					... 	[0, 1, 1, 0, 0, 0, 1, 0], 
					... 	[1, 0, 1, 0, 1, 1, 0, 1], 
					... 	[1, 0, 1, 1, 1, 0, 1, 1]]
                    >>> errorr(matrix)
                    1
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
