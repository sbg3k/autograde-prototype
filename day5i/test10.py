test = {
    "name": "test10",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'wedding_chow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> wedding_chow('rrrrssssffffmmmmdddd') == (4, '')
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
