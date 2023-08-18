#import numpy as np
unlikely_answer=input("Bro, do you even lift?\n")

very_unlikely_answer=float(input("Um, okay then: how much can you bench press?\n"))

print("you say you can bench press %d lbs?   Ya right!" % very_unlikely_answer)

sanity_check=input("Okay, how much do you weigh?")
total_weight=float(sanity_check)

#total_weight=151 #aspirational

print("I don't believe you...")
print("Because that means you can lift %f times your total body weight" % (very_unlikely_answer/total_weight))
