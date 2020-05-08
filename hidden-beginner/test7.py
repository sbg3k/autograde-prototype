test = {
    "name": "test7",
    "points": 3,
    "hidden": True,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> "fastSum" in dir()
                    True
                    >>> def time_checker(fastSum):
                    ...     import time
                    ...     a = time.time()
                    ...     fastSum(8_192_892_819_891_112_282_728_282)
                    ...     a = time.time() - a
                    ...     return a
                    >>> time_checker(fastSum) < 4.000000000000e-06
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