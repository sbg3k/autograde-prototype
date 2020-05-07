test = {
	"name": "test4",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> "order" in dir()
					True
					>>> order([1, 4, 2]) == (2, [4])
					True
					>>> def orderr(arr):
					...	 assert type(arr) in [list,tuple,set],'Not an array'
					...	 arr=list(arr)
					...	 arr=sorted(arr)
					...	 diff = [(arr[i]) for i in range(1,len(arr)) if arr[i]-arr[i-1]==1]
					...	 diff.insert(0,diff[0]-1)
					...	 one=[i[0] for i in enumerate([diff[i+1]-diff[i] for i in range(len(diff)-1)]) if i[1]!=1]
					...	 lcs = diff[:one[0]+1]
					...	 return len(lcs),[i for i in arr if i not in lcs ]
					>>> alpha = time.time()
					>>> y = orderr([100,1,2,3,21,22,23,200,31,32,33,4])
					>>> omega = time.time()
					>>> bound=round(omega-alpha,3)+0.0005
					>>> start = time.time()
					>>> x = order([100,1,2,3,21,22,23,200,31,32,33,4])
					>>> end = time.time()
					>>> diff= end-start
					>>> diff < bound
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