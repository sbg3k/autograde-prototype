test = {
    "name": "test4",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'match' in dir() and 'isBalanced' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> los=['code','edoc','fedoc','doc','d','ad']
                    >>> set(match(los))
                    {(0, 1), (4, 5), (1, 0), (0, 2), (0, 3)}
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
