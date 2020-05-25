test = {
    "name": "test10",
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
                    >>> A=Vector(2,-5,7)
                    >>> B=Vector(1,2,3)
                    >>> A.info()
                    '2i-5j+7k'
                    >>> B.info()
                    '1i+2j+3k'
                    >>> C=(A**B)+((A+B)*(A*B))-(B*3)
                    >>> C==Vector(44,130,7)
                    True
                    >>> C.info()=='7i-44j+130k'
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
