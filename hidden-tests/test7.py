test = {
    "name": "test7",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> from memory_profiler import memory_usage
                    >>> x = 'rsdmfrsdfmrsdfrsfsdmfrmfsdrfmsdfrdmsdsfrmddfrrmsdffdmmmdfrsrdfffmsdfr'
                    >>> def chow(supplies):
                    ...     food = 'rsmfd'
                    ...     ounje = ''.join(filter(lambda x: x in food, supplies))
                    ...     v = min([ounje.count(i) for i in 'rsmfd'])
                    ...     for i in food:
                    ...         ounje = ounje.replace(i, '', v)
                    ...     return v, ''.join(sorted(ounje, key=food.index))
                    >>> bound = memory_usage((chow,(x,)))[0]//1 +1
                    >>> def avg(numbers):
                    ...     return float(sum(numbers)) / max(len(numbers), 1)
                    >>> avg(memory_usage((wedding_chow,(x,)))) < bound
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
