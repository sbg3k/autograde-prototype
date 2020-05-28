test = {
    "name": "test9",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'Node' in dir() and 'max_height' in dir() and 'insert_to_tree' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> a=[23, 60, 66, 46, 45, 74, 72, 36, 49, 35, 81, 76, 67, 14, 35, 1, 3, 16, 92, 69, 46, 90, 71, 12, 38, 27, 83, 84, 64, 34, 34, 28, 52, 70, 11, 13, 46, 38, 52, 28, 54, 91, 31, 95, 84, 67, 87, 47, 3, 36, 73, 85, 72, 47, 22, 36, 87, 32, 50, 71, 20, 86, 6, 26, 45, 18, 82, 23, 71, 6, 45, 10, 58, 70, 8, 92, 5, 69, 79, 84, 43, 29, 64, 5, 21, 47, 28, 9, 86, 82, 79, 51, 45, 93, 33, 17, 71, 37, 15, 29]
                    >>> max_height(insert_to_tree(a))
                    14
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
