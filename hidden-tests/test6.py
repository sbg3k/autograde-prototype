test = {
    "name": "test6",
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
                    >>> arr=[i for i in range(100)]
                    >>> len(combo(arr,1))==len(arr)
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
