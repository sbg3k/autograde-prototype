test = {
    "name": "test7",
    "points": 2,
    "hidden": True,
    "suites": [
        {
            "cases": [
                {
                    "code": r"""
                    >>> 'Node' in dir() and 'append' in dir() and 'pop' in dir() 
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> arr=[1,2,3,4,5]
                    >>> a=Node(arr[0])
                    >>> for i in arr[1:]:
                    ...     append(a,i)
                    ...
                    >>> def count(head):
                    ...     ans=0
                    ...     while head:
                    ...         ans+=1
                    ...         head=head.next
                    ...     return ans
                    ...
                    >>> count(a)
                    5
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
