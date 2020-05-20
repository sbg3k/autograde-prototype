test = {
    "name": "test7",
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
                    a=[['1', '2', '3', '4'], ['5', '6', '7', '8'], ['0', '0', '9', '0'], ['1', '2', '1', '2']]
                    >>> loop_read(a)
                    '1 2 3 4 8 0 2 1 2 1 0 5 6 7 9 0'
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
