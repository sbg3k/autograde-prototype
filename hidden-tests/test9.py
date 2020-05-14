test = {
    "name": "test9",
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
                    >>> arr=[random.randint(1,100) for i in range(1000)]
                    >>> q=Queue()
                    >>> for i in arr:
                    ...     q.enqueue(i)
                    ...
                    
                    >>> arr3=[q.dequeue() for i in range(1000)]
                    >>> arr3==arr
                    True
                    >>> q.front()==None
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
