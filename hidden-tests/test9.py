test = {
    "name": "test9",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'overflow' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> image = [[1, 1, 2, 3, 1],
                    ...  [1, 2, 3, 1, 2],
                    ...  [3, 1, 2, 1, 1],
                    ...  [3, 1, 1, 1, 2],
                    ...  [2, 1, 1, 3, 1],
                    ...  [2, 3, 1, 2, 2],
                    ...  [3, 2, 1, 1, 3],
                    ...  [1, 2, 1, 1, 2],
                    ...  [3, 3, 3, 3, 2],
                    ...  [2, 2, 1, 1, 1]]
                    >>> from  memory_profiler import memory_usage
                    >>> def over(image,start,filler,pivot,debug = True):
                    ...     assert type(start[0]) == type(start[1])== type(filler)==type(pivot)==int
                    ...     x,y = start
                    ...     r = len(image)
                    ...     c = len(image[0])
                    ...     if x-1>=0:
                    ...         if image[x-1][y]==pivot and image[x-1][y] != filler:
                    ...             assert type(image[x-1][y])==int
                    ...             image[x-1][y] = filler
                    ...             over(image,(x-1,y),filler,pivot,debug)
                    ...     if x+1<r:
                    ...         if image[x+1][y]==pivot and image[x+1][y] != filler:
                    ...             assert type(image[x+1][y])==int
                    ...             image[x+1][y] = filler
                    ...             over(image,(x+1,y),filler,pivot,debug)
                    ...     if y-1>=0:
                    ...         if image[x][y-1]==pivot and image[x][y-1] != filler:
                    ...             assert type(image[x][y-1])==int
                    ...             image[x][y-1] = filler
                    ...             over(image,(x,y-1),filler,pivot,debug)
                    ...     if y+1<c:
                    ...         if image[x][y+1]==pivot and image[x][y+1] != filler:
                    ...             assert type(image[x][y+1])==int
                    ...             image[x][y+1] = filler
                    ...             over(image,(x,y+1),filler,pivot,debug)
                    ...     image[x][y]= filler
                    ...     return image
                    >>> bound = memory_usage((over,(image,(5,2),0,1)))[0]
                    >>> image = [[1, 1, 2, 3, 1],
                    ...  [1, 2, 3, 1, 2],
                    ...  [3, 1, 2, 1, 1],
                    ...  [3, 1, 1, 1, 2],
                    ...  [2, 1, 1, 3, 1],
                    ...  [2, 3, 1, 2, 2],
                    ...  [3, 2, 1, 1, 3],
                    ...  [1, 2, 1, 1, 2],
                    ...  [3, 3, 3, 3, 2],
                    ...  [2, 2, 1, 1, 1]]
                    >>> value = memory_usage((overflow,(image,(5,2),0,1)))[0]
                    >>> value<=bound
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
