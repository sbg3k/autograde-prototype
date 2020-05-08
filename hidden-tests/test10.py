test = {
    "name": "test10",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import inspect
                    >>> xx = ['//','hex(','bin(','%']
                    >>> to_base.__doc__ != None and  sum([i not in inspect.getsource(to_base) for i in xx])==4
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