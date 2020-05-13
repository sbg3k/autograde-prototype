test = {
	"name": "test10",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> 'sparsify' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def sparsiffy(adj):
					...	 '''This function takes in an adjacency dictionary and return'''
					...	 sparse = [0]*len(adj)**2
					...	 q=[i for i in range(len(sparse)+1) if i%len(adj)==0]
					...	 ee = sorted(adj.keys())
					...	 mapper = {ee[m]:m for m in range(len(ee))}
					...	 tupp = [(mapper[i],mapper[k],j) for k,v in adj.items() for i,j in v.items()]
					...	 for a,b,c in tupp:
					...		 s= b + a*len(adj)
					...		 sparse[s]=c
					...	 return [sparse[q[i]:q[i+1]] for i in range(len(q)-1)]
					>>> import time
					>>> start = time.time()
					>>> x = sparsiffy({"A": {"B":1,'E':2}, "B":{"C":2},'E':{'C':2}, "C":{"A":1, "D":1}, "D":{}})
					>>> end = time.time()
					>>> bound = end-start+0.0005
					>>> alpha = time.time()
					>>> x = sparsify({"A": {"B":1,'E':2}, "B":{"C":2},'E':{'C':2}, "C":{"A":1, "D":1}, "D":{}})
					>>> omega = time.time()
					>>> diff = omega - alpha
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
