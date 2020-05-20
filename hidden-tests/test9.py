test = {
    "name": "test9",
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
                    >>> e=[[1, 2, 3, 4, 5, 6, 7], [5, 6, 8, 7, 9, 8, 0], [0, 9, 1, 2, 8, 6, 7], [2, 2, 3, 5, 8, 0, 2], [6, 8, 0, 7, 6, 4, 7]]
                    >>> loop_read(e)
                    '1 2 3 4 5 6 7 0 7 2 7 4 6 7 0 8 6 2 0 5 6 8 7 9 8 6 0 8 5 3 2 9 1 2 8'
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
