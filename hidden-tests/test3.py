test = {
    "name": "test3",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'overflow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(i,c,f,p):
                    ...     try:
                    ...         x=overflow(i,c,f,p)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> image2 = [[1, 1, 2, 3, 1],
                    ...  [1, 2, 3, 1, 2],
                    ...  [3, 1, 2, 1, 1],
                    ...  [3, 1, 1, 1, 2],
                    ...  [2, 1, 1, 3, 1],
                    ...  [2, 3, 1, 2, 2],
                    ...  [3, 2, 1, 1, 3],
                    ...  [1, 2, 1, 1, 2],
                    ...  [3, 3, 3, 3, 2],
                    ...  [2, 2, 1, 1, 1]]
                    >>> result = [[1, 1, 2, 3, 1],
                    ...  [1, 2, 3, 0, 2],
                    ...  [3, 0, 2, 0, 0],
                    ...  [3, 0, 0, 0, 2],
                    ...  [2, 0, 0, 3, 1],
                    ...  [2, 3, 0, 2, 2],
                    ...  [3, 2, 0, 0, 3],
                    ...  [1, 2, 0, 0, 2],
                    ...  [3, 3, 3, 3, 2],
                    ...  [2, 2, 1, 1, 1]]
                    >>> errorr(image2,(5,2),0,1) == result
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
