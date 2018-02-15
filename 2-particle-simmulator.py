import matplotlib.pyplot as p
import math
def direction(co_ordinte_of_mass,co_ordinate_of_object,r):
    if (co_ordinate_of_object-co_ordinte_of_mass > 0):
        # print float(co_ordinate_of_object-co_ordinte_of_mass)/float(r)
        return 1*float(co_ordinate_of_object-co_ordinte_of_mass)/float(r)
    elif (co_ordinate_of_object-co_ordinte_of_mass < 0):
        return  -1*(-float(co_ordinate_of_object-co_ordinte_of_mass)/float(r))
    else:
        return 0
def main():
    x1,y1=map(float,raw_input('Enter x,y of 1st').split())
    m1=int(raw_input('Mass of 1st'))
    x2,y2=map(float,raw_input('x , y of 2nd').split())
    m2=int(raw_input('mass od second'))
    m=1
    t=0
    h=0.01
    acc_x=0.0
    acc_y=0.0
    x,y=0.,0.0
    velocity_x,velocity_y=map(float,raw_input('Enter velocity').split())
    x_list,y_list=[],[]
    p.ion()
    i=0
    while True:
        i+=1
        r1=math.sqrt((x-x1)**2 + (y- y1)**2)
        r2=math.sqrt((x-x2)**2 + (y- y2)**2)
        acc_x=(m1*m/(r1**2))*direction(x,x1,r1) + (m2*m/(r2**2))*direction(x,x2,r2)
        acc_y=(m1*m/(r1**2))*direction(y,y1,r1) + (m2*m/(r2**2))*direction(y,y2,r2)
        velocity_x+=acc_x*h
        velocity_y+=acc_y*h
        x+=(1)*velocity_x*h
        y+=(1)*velocity_y*h
        if r1 < 0.1 or r2 < 0.1:
            print 'hit'
            break
        t+=h
        p.scatter(x, y)
        if i%100==0:

            p.pause(h)

    while True:
        p.pause(0.05)

if __name__ == '__main__':
    main()
