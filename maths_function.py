import math

def clamp(x, a=0.0, b=1.0):
    if x < a:
        return a
    elif x > b:
        return b
    else:
        return x
        
def step(x, a, b):
    if x < a:
        return 0.0
    elif x > b:
        return 1.0
    else:
        return (x - a) / (b - a)

#skipped max min absolute as python has buildin 

def lerp(a, b, t):
    return (a * (1.0 - t)) + (b * t)

def cubic_smooth_compact(x, r):
    if x > r:
        return 0.0
    else:
        return (1.0 - x / r) * (1.0 - x / r) * (1.0 - x / r)
    
def cubic_sigmoid(x, r, t):
    if x > 0.0:
        if x < r:
            return x * (1.0 + x * ((3.0*t - 2.0*r) / (r*r) + x * (r - 2.0*t) / (r*r*r)))
        else:
            return t
    else:
        if x > -r:
            y = -x
            return -(y * (1.0 + y * ((3.0*t - 2.0*r) / (r*r) + y * (r - 2.0*t) / (r*r*r))))
        else:
            return -t
        
def cubic_smooth(x,r):
    return (1.0 - x / r) * (1.0 - x / r) * (1.0 - x / r)

def cubic_smooth_step(x,a,b):
    if x < a:
        return 0.0
    elif x > b:
        return 1.0
    else:
        return 1.0 - cubic_smooth((x - a) * (x - a), (b - a) * (b - a))
def quintic_smooth(t):
    return pow(t, 3.0) * (t * (t * 6.0 - 15.0) + 10.0)