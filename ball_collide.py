import math
def ball_collide(t1,t2):
   d=math.sqrt((t2[0]-t1[0])**2 + (t2[1]-t1[1])**2)
   if d<=(t1[2]+t2[2]):
       return True
   else:
       return False

print("Enter ball1 (x,y,r):")
#b1=tuple(map(int,input().split()))
b1=tuple(int(i) for i in input().split())
print(b1)
print("Enter ball2 (x,y,r):")
b2=tuple(int(i) for i in input().split())
print(b2)

if ball_collide(b1,b2):
    print("balls are colliding")
else:
    print("balls are not colliding")

#print("ball are colliding ?",ball_collide(b1,b2))
