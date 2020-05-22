test = {
    "name": "test6",
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
                    >>> a=[3, 30, 7, 30, 44, 16, 32, 15, 25, 21, 4, 11, 18, 46, 49, 43, 13, 38, 30, 8]
                    >>> root=insert_to_tree(a)
                    >>> root.right.left.right.left.value
                    16
                    >>> root.right.left.right.left.left.value
                    15
                    >>> root.left==None
                    True
                    >>> max_height(root)
                    8
                    >>> root.right==root.right.left.right==root.right.right.left-2
                    False
                    >>> root.right.value==root.right.left.right.value==root.right.right.left.value-2
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
