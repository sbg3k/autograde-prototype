test = {
    "name": "test2",
    "points": 1,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> import inspect
                    >>> 'Vector' in dir()
                    True
                    >>> a=inspect.getsource(Vector)
                    >>> 'magnitude(' in a
                    True
                    >>> 'info(' in a
                    True
                    >>> '__add__(' in a
                    True
                    >>> '__sub__(' in a
                    True
                    >>> '__mul__(' in a
                    True
                    >>> '__pow__(' in a
                    True
                    >>> '__eq__(' in a
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def errorr(a,b,c):
                    ...     try:
                    ...         x=Vector(a,b,c)
                    ...     except AssertionError:
                    ...         return True
                    ...     except:
                    ...         return False
                    ...     else:
                    ...         return x
                    ...
                    >>> errorr(1.0,3.2,4.6)
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
