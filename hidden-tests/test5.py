test = {
    "name": "test5",
    "points": 3,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'pathfinder' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(m,s,d):
                    ...     try:
                    ...         x=pathfinder(m,s,d)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    >>> matrix= [
                    ...     [1, 1, 1, 0, 0, 1, 1, 1],
                    ...     [1, 0, 0, 0, 0, 1, 1, 1],
                    ...     [1, 1, 1, 1, 1, 1, 0, 1],
                    ...     [0, 1, 0, 0, 0, 1, 1, 1],
                    ...     [0, 1, 0, 0, 1, 1, 1, 0],
                    ...     [1, 1, 1, 1, 1, 0, 1, 0],
                    ...     [0, 0, 0, 0, 0, 0, 0, 1],
                    ...     [1, 1, 0, 0, 1, 1, 0, 1]]
                    >>> errorr(matrix,(4,0),(3,7))
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
