test = {
    "name": "test3",
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
                    >>> def errorr(l,thresh=None):
                    ...     try:
                    ...         x=my_exes(l,thresh=thresh)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> matrix = [
                    ...     [1, 1, 1, 0, 0, 0, 0, 1],
                    ...     [1, 1, 0, 0, 1, 0, 1, 1],
                    ...     [1, 0, 1, 0, 0, 1, 1, 1],
                    ...     [1, 0, 0, 1, 0, 1, 0, 1],
                    ...     [0, 1, 1, 0, 0, 0, 1, 0],
                    ...     [1, 1, 1, 0, 1, 1, 0, 1],
                    ...     [1, 0, 1, 1, 1, 0, 1, 1]]
                    >>> errorr(matrix)==6
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