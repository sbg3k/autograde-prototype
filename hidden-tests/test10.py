test = {
    "name": "test10",
    "points": 1,
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
                    >>> order([1,2,3,4,7,8,9])
                    (4, [7, 8, 9])
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
