test = {
    "name": "test7",
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
                    >>> imagge1 =[[0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
                    ...  [1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                    ...  [0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                    ...  [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                    ...  [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                    ...  [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                    ...  [1, 0, 0, 0, 0, 'a', 1, 1, 0, 1],
                    ...  [1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
                    ...  [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                    ...  [1, 0, 0, 1, 1, 1, 0, 0, 1, 1]]
                    >>> errorr(imagge1,(6,5),3,1)
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