test = {
    "name": "test5",
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
                    >>> arr=[1,2,3,4,5,6,7,8]
                    >>> a=combo(arr,4)
                    >>> len(a)
                    70
                    >>> a[0]
                    [1, 2, 3, 4]
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
