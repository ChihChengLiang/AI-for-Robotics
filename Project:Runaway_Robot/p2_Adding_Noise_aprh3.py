# ----------
# Part Two
#
# Now we'll make the scenario a bit more realistic. Now Traxbot's
# sensor measurements are a bit noisy (though its motions are still
# completetly noise-free and it still moves in an almost-circle).
# You'll have to write a function that takes as input the next
# noisy (x, y) sensor measurement and outputs the best guess 
# for the robot's next position.
#
# ----------
# YOUR JOB
#
# Complete the function estimate_next_pos. You will be considered 
# correct if your estimate is within 0.01 stepsizes of Traxbot's next
# true position. 
#
# ----------
# GRADING
# 
# We will make repeated calls to your estimate_next_pos function. After
# each call, we will compare your estimated position to the robot's true
# position. As soon as you are within 0.01 stepsizes of the true position,
# you will be marked correct and we will tell you how many steps it took
# before your function successfully located the target bot.

# These import steps give you access to libraries which you may (or may
# not) want to use.
from robot import *  # Check the robot.py tab to see how this works.
from math import *
from matrix import * # Check the matrix.py tab to see how this works.
import random

# This is the function you have to write. Note that measurement is a 
# single (x, y) point. This function will have to be called multiple
# times before you have enough information to accurately predict the
# next position. The OTHER variable that your function returns will be 
# passed back to your function the next time it is called. You can use
# this to keep track of important information over time.
def estimate_next_pos(measurement, OTHER = None):
    """Estimate the next (x, y) position of the wandering Traxbot
    based on noisy (x, y) measurements."""
    # In this approach, I try to estimate the center of the circle by Circumcenter. This approach not gonna work.
    if not OTHER: # this is the first measurement
        OTHER = [[measurement],[]]
        xy_estimate = measurement
    elif len(OTHER[0])<2:
        OTHER[0].append(measurement)
        xy_estimate = measurement
    else:
        OTHER[0].append(measurement)
        p=[ OTHER[0][-1], OTHER[0][-2], OTHER[0][-3] ]
        d=[distance_between(p[k],p[(k+1)%3]) for k in range(3)]
        s=sum(d)
        const=16.0*s*(s-d[0])*(s-d[1])*(s-d[2])
        newCenter=[0,0]
        for i in range(2):
            for j in range(3):
                newCenter[i]+= ((d[j]**2) *(d[(j+1)%3]**2+d[(j-1)%3]**2-d[j]**2)/const)*p[j][i]
        OTHER[1].append(newCenter)
        N0=len(OTHER[0])
        N1=len(OTHER[1])
        center= sum([x for x,y in OTHER[1]])/N1, sum([y for x,y in OTHER[1]])/N1
        avgRadius=sum([distance_between(m,center) for m in OTHER[0]])/N0
        avgTurn=0
        xc,yc=center
        angles=[atan2(y-yc,x-xc) for x,y in OTHER[0]]
        avgTurn=sum([(angles[i]-angles[i-1])%(2*pi) for i in range(1,N0)])/ (N0-1)
        startAngle=sum([(angles[j]-j*avgTurn)%(2*pi) for j in range(len(angles))])/N1
        newAngle=startAngle+N0*avgTurn
        xy_estimate=(xc+avgRadius*cos(newAngle), yc+avgRadius*sin(newAngle))
    # You must return xy_estimate (x, y), and OTHER (even if it is None) 
    # in this order for grading purposes.
    if len(OTHER[0])>=20: print center, avgRadius,avgTurn,startAngle,xy_estimate
    if len(OTHER[0])>40: import pdb; pdb.set_trace()
    return xy_estimate, OTHER

# A helper function you may find useful.
def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# This is here to give you a sense for how we will be running and grading
# your code. Note that the OTHER variable allows you to store any 
# information that you want. 
def demo_grading(estimate_next_pos_fcn, target_bot, OTHER = None):
    localized = False
    distance_tolerance = 0.01 * target_bot.distance
    ctr = 0
    # if you haven't localized the target bot, make a guess about the next
    # position, then we move the bot and compare your guess to the true
    # next position. When you are close enough, we stop checking.
    while not localized and ctr <= 5000:
        ctr += 1
        measurement = target_bot.sense()
        position_guess, OTHER = estimate_next_pos_fcn(measurement, OTHER)
        target_bot.move_in_circle()
        true_position = (target_bot.x, target_bot.y)
        error = distance_between(position_guess, true_position)
        if error <= distance_tolerance:
            print "You got it right! It took you ", ctr, " steps to localize."
            localized = True
        if ctr == 5000:
            print "Sorry, it took you too many steps to localize the target."
    return localized



# This is a demo for what a strategy could look like. This one isn't very good.
def naive_next_pos(measurement, OTHER = None):
    """This strategy records the first reported position of the target and
    assumes that eventually the target bot will eventually return to that 
    position, so it always guesses that the first position will be the next."""
    if not OTHER: # this is the first measurement
        OTHER = measurement
    xy_estimate = OTHER 
    return xy_estimate, OTHER

# This is how we create a target bot. Check the robot.py file to understand
# How the robot class behaves.
test_target = robot(2.1, 4.3, 0.5, 2*pi / 34.0, 1.5)
measurement_noise = 0.05 * test_target.distance
test_target.set_noise(0.0, 0.0, measurement_noise)

#for i in range(100):demo_grading(estimate_next_pos, test_target)
demo_grading(estimate_next_pos, test_target)



