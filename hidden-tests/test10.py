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
                    >>> arr=[i for i in range(1,1001)]
                    >>> bubble_sort(arr)==0
                    True
                    """
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
