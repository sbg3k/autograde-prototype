test = {
    "name": "test7",
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
                    >>> arr=[random.randint(2,100) for i in range(50)]
                    >>> q=Queue()
                    >>> for i in arr:
                    ...     q.enqueue(i)
                    ...
	
                    >>> check=[]
                    >>> for i in range(10):
                    ...     check.append(arr[i]==q.dequeue())
                    ...
	
                    >>> all(check)
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
