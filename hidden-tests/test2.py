test = {
    "name": "test2",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "my_cars" in dir()
                    True
                    >>> my_cars([17, 8, 14, 12, 10, 2, 7, 17])==58
                    True
                    >>> my_cars([10, 14,  5, 12, 17, 11, 1, 9, 3, 5])==51
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
