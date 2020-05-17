test = {
    "name": "test5",
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
                    >>> c=[9, 10, 6, 2, 3, 5, 4, 8, 7, 1]
                    >>> bubble_sort(c)
                    29
                    >>> c
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
