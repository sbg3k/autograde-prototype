test = {
    "name": "test6",
    "points": 2,
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
                    >>> import random
                    >>> arr=[random.randint(2,100) for i in range(20)]
                    >>> q=Queue()
                    >>> for i in arr:
                    ...     q.enqueue(i)
                    ...     
	
                    >>> q.count()
                    20
                    >>> q.front()==arr[0]
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
