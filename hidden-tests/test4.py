test = {
    "name": "test4",
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
                    >>> a=Node.__doc__!=None
                    >>> b=Queue.__doc__!=None
                    >>> c=Queue.enqueue.__doc__!=None
                    >>> d=Queue.dequeue.__doc__!=None
                    >>> e=Queue.count.__doc__!=None
                    >>> f=Queue.front.__doc__!=None
                    >>> a&b&c&d&e&f
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
