test = {
    "name": "test8",
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
                    >>> my_cars([97, 94, 5, 51, 45, 53, 70, 6, 15, 20, 80, 64, 2, 71, 51, 63, 3, 19, 33, 73])==539
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
