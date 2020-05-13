test = {
    "name": "test6",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'resolve' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(d,l):
                    ...     try:
                    ...         x=resolve(d,l)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> d = {'alpha':1,'b':'B','cab':'drive','drive':1,'B':'Ball'}
                    >>> l = ['alpha', 'b', 'cab', 'd', 'e',]
                    >>> errorr(d,l)
                    [1, 'Ball', 1, 'd', 'e']
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
