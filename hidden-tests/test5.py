test = {
    "name": "test5",
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
                    >>> order.__doc__ !=None
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
