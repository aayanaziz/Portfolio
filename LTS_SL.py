#Just some contants that can be changed later
#Point mass sim,
# All units are SI
m = 320
mu = 1.6
cl = None
cd = 0.267
ar = 1.3
g = 9.81
r = 0.226
rho = 1.23
s = 1
u = 0
T = 0
t = 0
S = 0






# straight line loop
while  S<80 :
    Fxt = mu*m*g
    #print(Fxt)
    Fxd = 0.5*rho*ar*(u**2)*cd
    #print(Fxd)
    acc = (Fxt-Fxd)/m
    #print (acc)

    #s = s + ((u*t)+(0.5*(acc*(t**2))))

    #u = u + (acc*t)
    #T =  T+t

    v = (((2*acc*s)+(u**2))**0.5)
    #print(v)
    t = (v-u)/acc
    print(t)

    S = S+s
    T = T+t

    u = v

print("Dist:",S,"Time :",T,u)
