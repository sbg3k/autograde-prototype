test = {
    "name": "test6",
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
                    ...         x=overflow(i,c,f,p)
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
                    >>> errorr(image,(1.0,1),2,0)
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
