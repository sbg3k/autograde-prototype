test = {
    "name": "test4",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'make_car' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> make_car('Toyota', 'Bb188', age=30, color='black', mileage='50miles')=={'manufacturer':'Toyota', 'model': 'Bb188', 'age':30, 'color':'black', 'mileage': '50miles'}) # 2 points
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
