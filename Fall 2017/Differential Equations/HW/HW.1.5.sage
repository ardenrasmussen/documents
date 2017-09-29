var('y')
f(y) = y^3
y0=1
deltaT=0.5
steps=2
eulerData = [[k*deltaT,y0] for k in range(0,steps+1)]
for k in [1..steps]:
    eulerData[k][1] = eulerData[k-1][1] + deltaT*f(eulerData[k-1][1])

table(eulerData)
