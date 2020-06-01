test = {
    "name": "test4",
    "points": 3 ,
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
                    >>> ArrayOperation().threeSum([-25, -10, -7, -3, 2, 4, 8, 10])==[[-10, 2, 8], [-7, -3, 10]] #3 points
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
