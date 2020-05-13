test = {
    "name": "test8",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'wedding_chow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
					>>> wedding_chow.__doc__ != None
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
