test = {
    "name": "test5",
    "points": 5 ,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> "ArrayOperation" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> ArrayOperation().threeSum([-25, -10, -7, -3, 2, 4, 8, 10, 6, -9, 4, -10, 7, 65, -55])==[[-55, -10, 65], [-10, 2, 8], [-10, 4, 6], [-9, 2, 7], [-7, -3, 10]] #5 points
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
