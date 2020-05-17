test = {
    "name": "test0",
    "points": 1,
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
                    >>> combo.__doc__!=None and my_money.__doc__!=None
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
