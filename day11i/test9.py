test = {
    "name": "test9",
    "points": 2,
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
                    >>> def resol(d, l):
                    ...     lamb = lambda i: i.isalpha() or (type(i)==int and i>0)
                    ...     assert all((map(lamb,list(d.keys())+list(d.values())+l))),'Follow instructions'
                    ...     resol = []
                    ...     for a in range(len(l)):
                    ...         i = l[a]
                    ...         while i in d.keys():
                    ...             i=d[i]
                    ...             if l[a] ==i:
                    ...                 break
                    ...         resol.append(i)
                    ...     return resol
                    ...
                    >>> from memory_profiler import memory_usage
                    >>> d = {'a': 'b', 'b': 'c', 'p': 'q', 'z': 'a', 'n': 'm', 'm': 'o', 'o': 'n'}
                    >>> l = ['a', 'b', 'c', 'd', 'e', 'p', 'q', 'n', 'm', 'o', 'y', 'z']
                    >>> bound = memory_usage((resol,(d,l)))[0]+0.2
                    >>> memory_usage((resolve,(d,l)))[0] < bound
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
                    >>> errorr(tuple(range(128)), (1, 2, 4, 8, 16, 32, 64))
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
