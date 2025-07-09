import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 
w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        best_x = x
        best_height = h[x]
        
        # Look up to 5 steps in each direction
        for step in range(1, 6):
            # Check left
            if x - step >= 0 and h[x - step] > best_height:
                best_x = x - step
                best_height = h[x - step]
            
            # Check right
            if x + step < 100 and h[x + step] > best_height:
                best_x = x + step
                best_height = h[x + step]
        
        # If we found a better position, move there
        if best_x != x:
            x = best_x
        else:
            summit = True  # No better position found within 5 steps
    
    # while not summit:
    #     summit = True
    #     for x_new in range(max(0, x-5), min(99, x+5)):
    #         if h[x_new] > h[x]:
    #             x = x_new         # here is higher, go here 
    #             summit = False    # and keep going

    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)


