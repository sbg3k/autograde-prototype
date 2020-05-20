test = {
    "name": "test6",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'loop_read' in dir() and 'rotate' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> e=[[1, 2, 3, 4, 5], [5, 6, 8, 7, 9], [0, 9, 1, 2, 8], [2, 2, 3, 5, 8], [6, 8, 0, 7, 6]]
                    >>> rotate(e)
                    >>> e
                    [[6, 2, 0, 5, 1], [8, 2, 9, 6, 2], [0, 3, 1, 8, 3], [7, 5, 2, 7, 4], [6, 8, 8, 9, 5]]
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
