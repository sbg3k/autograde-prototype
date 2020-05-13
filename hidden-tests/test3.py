test = {
    "name": "test3",
    "points": 3,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'pathfinder' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> def path(matrix,src,dest):
                    ...     assert all(all((map(lambda i: i in [0,1],row))) for row in matrix),'Invalid matrix'
                    ...     l=len(matrix)
                    ...     a,b = src
                    ...     assert matrix[a][b]==1,'you can\'t stand on an obstacle...'
                    ...     c,d = dest
                    ...     dist = 0
                    ...     crossed = ((a,b),)
                    ...     while a!=c or b!=d:
                    ...         pos = ()
                    ...         if 0 <= a+1<l:pos+=((a+1,b),)
                    ...         if 0 <= a - 1 < l: pos += ((a - 1, b),)
                    ...         if 0 <= b + 1 < l: pos += ((a, b+1),)
                    ...         if 0 <= b - 1 < l: pos += ((a, b-1),)
                    ...         line = lambda e,f: ((f[1]-e[1])**2 + (f[0]-e[0])**2)**0.5
                    ...         mat = {line((i,j),dest):(i,j) for i,j in pos if (i,j) not in crossed and matrix[i][j]==1}
                    ...         assert mat !={},'No pathway'
                    ...         a,b = mat[min(mat.keys())]
                    ...         crossed+=((a,b),)
                    ...         dist+=1
                    ...     return dist
                    >>> matrix= [
                    ...     [1, 1, 1, 0, 0, 1, 1, 1],
                    ...     [1, 0, 0, 0, 0, 1, 1, 1],
                    ...     [1, 1, 1, 1, 1, 1, 0, 1],
                    ...     [0, 1, 0, 0, 0, 1, 1, 1],
                    ...     [0, 1, 0, 0, 1, 1, 1, 0],
                    ...     [1, 1, 1, 1, 1, 0, 1, 0],
                    ...     [0, 0, 0, 0, 0, 0, 0, 1],
                    ...     [1, 1, 0, 0, 1, 1, 0, 1]]
                    >>> from memory_profiler import memory_usage
                    >>> bound = memory_usage((path,(matrix,(5,0),(3,7))))[0]+0.05
                    >>> memory_usage((path,(matrix,(5,0),(3,7))))[0]<bound
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
