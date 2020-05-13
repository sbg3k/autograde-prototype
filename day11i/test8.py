test = {
    "name": "test8",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'bin' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def b(l, b):
                    ...     assert type(l)==list and type(b)==list, 'Wrong input'
                    ...     bins = [len([j for j in l if j in range(b[i],b[i+1])]) for i in range(len(b)-1)]
                    ...     last = [i for i in l if i>=b[-1]]
                    ...     bins+=[len(last)]
                    ...     return bins
                    >>> from memory_profiler import memory_usage
                    >>> d = list(range(10))
                    >>> bound = memory_usage((b,(d,d)))[0]+0.2
                    >>> memory_usage((resolve,(d,d)))[0] < bound
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(s,b):
                    ...     try:
                    ...         x=bin(s,b)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> errorr(range(128), ['1', '2', '4', '8', '16', '32', '64']) and errorr([],[])[0]==0
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
