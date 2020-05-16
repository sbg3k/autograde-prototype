test = {
    "name": "test6",
    "points": 2,
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
                    >>> b=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
                    >>> bubble_sort(b)
                    45
                    >>> b
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
