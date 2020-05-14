test = {
    "name": "test5",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'Node' in dir() and 'Queue' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> q=Queue()
                    >>> arr=[1,2,3,4,5,6,7,8,9,10]
                    >>> for i in arr:
                    ...     q.enqueue(i)
                    ...     
                    >>> while q.front():
                    ...     q.dequeue()
                    ...
                    1
                    2
                    3
                    4
                    5
                    6
                    7
                    8
                    9
                    10
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
