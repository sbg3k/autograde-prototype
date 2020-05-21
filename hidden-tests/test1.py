test = {
    "name": "test1",
    "points": 1,
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
                    ...         x=overflow(i,c,p,f)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> image = [
                    ...     [0,1,1],
                    ...     [1,0,0],
                    ...     [1,0,1]
                    ... ]
                    >>> errorr(image,(1,1),2,0) == [[0, 1, 1], [1, 2, 2], [1, 2, 1]]
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
