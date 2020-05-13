test = {
    "name": "test6",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "my_cars" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> my_cars([2,4,6,8])==12
                    True
                    >>> my_cars([8, 12, 2, 7, 10, 12, 14, 8, 3, 7, 10, 6, 18, 18, 9])==76
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
