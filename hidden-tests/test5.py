test = {
    "name": "test5",
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
                    >>> d = {'a': 'b', 'b': 'c', 'p': 'q', 'z': 'a', 'n': 'm', 'm': 'o', 'o': 'n'}
                    >>> l = ['a', 'b', 'c', 'd', 'e', 'p', 'q', 'n', 'm', 'o', 'y', 'z']
                    >>> errorr(d,l)
                    ['c', 'c', 'c', 'd', 'e', 'q', 'q', 'n', 'm', 'o', 'y', 'c']
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
