test = {
    "name": "test4",
    "points": 1,
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
                    >>> arr=[10, 14, 8, 16, 13, 9, 20, 17, 19, 18]
                    >>> root=insert_to_tree(arr)
                    >>> root.right.right.value+3==root.right.right.right.left.right.value
                    True
                    >>> max_height(root)
                    7
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
