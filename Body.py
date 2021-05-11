import numpy as np
import random
import math


class Body :
    Liste_Body = []
    def __init__(self,Mass,X,Y,Z,Vx,Vy,Vz):
        self.Mass = Mass
        self.pos = np.array([X,Y,Z])
        self.speed = np.array([Vx,Vy,Vz])
        self.force = np.array([0.,0.,0.])
        Body.Liste_Body.append(self)

    
    def compute_force(self,other,G,epsilon):
        p=self.pos-other.pos
        distance = np.linalg.norm(p)
        if distance < epsilon :
            return 0
        force = ((G*self.Mass*other.Mass*p)/((distance+epsilon)**1.5))
        self.force+=force
        other.force+=-force

    
    def new_pos(self,dt):
        acceleration = self.force/self.Mass
        self.speed += acceleration*dt
        self.pos += self.speed*dt
        self.force = np.array([0.,0.,0.])
        with open("gravity.cvs", "ab") as f:
            np.savetxt(f,[self.pos],delimiter=',',fmt='%f')
        

        
        
        
    
    def update(G,EPSILON,dt):
        for i in range(0,len(Body.Liste_Body)):
            for j in range(i+1,len(Body.Liste_Body)):
                Body.Liste_Body[i].compute_force(Body.Liste_Body[j],G,EPSILON)
        
            Body.Liste_Body[i].new_pos(dt)


    
    def create_body(size,N):
        for i in range(N):
            x=random.uniform(-size/2,size/2)
            y=random.uniform(-size/2,size/2)
            z=random.uniform(-size/2,size/2)
            mass = random.uniform(10,20)
            Body(mass,x,y,z,0.,0.,0.)





    def generate_ring(number_of_body,distance_centre,largeur_aneau,vt,epaiseur):
        angle=(2*math.pi/number_of_body)
        for i in range(number_of_body):
            cos=math.cos(angle*i)
            sin=math.sin(angle*i)
            x1=cos*distance_centre
            x2=cos*(distance_centre+largeur_aneau)
            y1=sin*distance_centre
            y2=sin*(distance_centre+largeur_aneau)

            x=random.uniform(x1,x2)
            y=random.uniform(y1,y2)
            z=random.uniform(-epaiseur/2,epaiseur/2)
            masse=random.uniform(10,20)
            vx=sin*-vt
            vy=cos*vt
            vz=0

            Body(masse,x,z,y,vx,vy,vz)
            
        
#python setup.py build_ext --inplace