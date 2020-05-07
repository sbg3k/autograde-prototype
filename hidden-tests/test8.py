test = {
    "name": "test8",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "order" in dir()
                    True
                    >>> order([1, 1, 2]) == (2, [1])
                    True
                    >>> order([1,2,3,4,5,6,7,8,9])
                    (9, [])
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
