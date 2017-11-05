import numpy as np
arr=[0]*4
#-------------------------------
def distance(x1,y1,x2,y2):
	return np.abs(x1-x2)+np.abs(y1-y2)

def shortest_path(v,level,n,dist):
	global arr
	arr[v]=1
	sps=[]
	print arr
	if(level==1):
		return dist[0][v]
	for i in range(1,n+1):
		if(arr[i]!=1 and i!=v):
			print level-1,i,v
			print arr
			q=shortest_path(i,level-1,n,dist)+dist[i][v]
			
			sps.append(q)
	
	print 'level ',level,'v ',v		
	arr[v]=0
	return min(sps)
	
def shortest_path_util(dist):
	n=len(dist)-2
	sps=[]
	for i in range(1,n):
		sps.append(shortest_path(i,n,n,dist+dist[i][n+1]))
	return min(sps)
		


def inputs():
	n=3
	x=[0]*(n+2)
	y=[0]*(n+2)
	xq=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
	
	for i in range(len(xq)):
		if(i%2==0):
			print i//2
			x[i//2]=xq[i]
		else:
			print i//2
			y[i//2]=xq[i]
	dist=[[0]*(n+2)]*(n+2)
	for i in range(n+2):
		for q in range(n+2):
			dist[i][q]=distance(x[i],y[i],x[q],y[q])
	
	sp = shortest_path_util(dist)
	print sp
	
if __name__=='__main__':
	inputs()
