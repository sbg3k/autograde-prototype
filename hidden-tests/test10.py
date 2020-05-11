test = {
    "name": "test10",
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
                    >>> d = {'a': '1', '1': 'c', 'p': '2', 'z': 'a', 'n': 'm', 'm': 'o', 'o': 'n'}
                    >>> l = ['a', '1', 'c', 'd', 'e', 'p', '2', 'n', 'm', 'o', 'y', 'z']
                    >>> errorr(d,l)
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
