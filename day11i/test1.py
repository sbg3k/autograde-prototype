test = {
    "name": "test1",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'bin' in dir() and 'resolve' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> bin.__doc__ !=None and resolve.__doc__ != None
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
