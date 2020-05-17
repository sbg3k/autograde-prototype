test = {
    "name": "test4",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import inspect
                    >>> 'bubble_sort' in dir()
                    True
                    >>> check=inspect.getsource(bubble_sort)
                    >>> '.sort(' in check
                    False
                    >>> 'sorted(' in check
                    False
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    >>> bubble_sort(a)
                    0
                    >>> a
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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
