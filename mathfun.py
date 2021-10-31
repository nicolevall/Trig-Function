#Nicole Vall mathfun.py
#this program's job is to do basic trig calculations to find either a length or the angle (SOHCAHTOA)
import math

# here i have the function for finding the ajacent length using the hypotenuse and adjacent angle
def adj_ang_hyp(angle, hypotenuse):
    angle = math.radians(angle)
    adj_length = (math.cos(angle)*hypotenuse)
    print("\nAdjacent Length:{0:.2f}".format(adj_length))

    
# here i have the function for finding the opposite length using the adjacent length and the hypotenuse
def opp_ang_hyp(angle, hypotenuse): 
    angle = math.radians(angle)
    opp_Length = (math.sin(angle)* hypotenuse)
    print("Opposite Length:{0:.2f}".format(opp_Length))


# here i have the function for finding the angle using the opposite length and the hypotenuse
def ang_opp_hyp(opposite, hypotenuse):
    res =  opposite/hypotenuse
    angle = round(math.degrees((math.asin(res))))
    print("The angle is:",angle)
    
# Function that computes adjacent angle using the adjacent length and the opposite length
def ang_adj_opp(adjacent, opposite):
    res =  opposite/adjacent
    angle= round(math.degrees((math.atan(res))))
    print("The angle is:",angle)

#takining user input for the variables
hypotenuse=float(input("Enter the hypotenuse: "))
adjacent = float(input("Enter the adjacent length: "))
opposite = float(input("Enter the opposite length: "))
angle = float(input("Enter the adjacent angle: "))

#calling the functions
adj_ang_hyp(angle, hypotenuse)
opp_ang_hyp(angle, hypotenuse)
ang_opp_hyp(opposite, hypotenuse)
ang_adj_opp(adjacent, opposite)