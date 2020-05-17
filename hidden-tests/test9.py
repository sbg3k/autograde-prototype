test = {
    "name": "test9",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> a=True
                    >>> for i in dir():
                    ...     try:
                    ...         exec('import '+i)
                    ...         a=False
                    ...         break
                    ...     except:
                    ...         pass
                    ...
                    >>> a
                    True
                    >>> 'combo' in dir() and 'my_money' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> arr=[10]
                    >>> my_money(arr)
                    False
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
