test = {
    "name": "test7",
    "points": 2,
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
                    >>> A=Vector(3,4,-2)
                    >>> B=Vector(-1,-2,-3)
                    >>> A.info()
                    '3i+4j-2k'
                    >>> B.info()
                    '-1i-2j-3k'
                    >>> (A+B)+(A-B)==A*2
                    True
                    """,
                    "hidden": False,                    "locked": False,
                },
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
