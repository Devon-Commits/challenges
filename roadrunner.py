# ROADRUNNER

# A coyote is chasing a roadrunner and they start out 50 feet apart. If you know how fast they are both traveling, 
# and how far the roadrunner is from safety, determine whether or not the coyote is able to catch the roadrunner. 

# Both animals and the roadrunner's safe place are on a straight line.

# Task: 
# Determine whether or not the roadrunner made it to safety.

# Input Format: 
# Three integer values, the first value represents the distance the roadrunner is from safety, 
# then the roadrunner's speed (feet/second) and then the coyote's speed (feet/second).

# Output Format: 
# A string that says 'Meep Meep' if the roadrunner made it, or 'Yum' if the coyote caught up to the roadrunner.

# Sample Input: 
# 10 
# 5 
# 20

# Sample Output: 
# Meep Meep


class Roadrunner():

    def chase(self, dist_safe, runner_speed, coyote_speed): # dist_safe = 100, runner_speed = 5, coyote_speed = 20
        start_dist = 50
        final_dist = start_dist + dist_safe # 150 feet
        runner_current = start_dist # roadrunner starts 50 feet ahead of coyote
        coyote_current = 0
        for i in range(0, final_dist): # for each iteration(second), add the runners speed to their current distance
            runner_current += runner_speed # +5
            coyote_current += coyote_speed # +20

            if coyote_current >= runner_current: # if coyote reaches roadrunner before roadrunner can reach safety
                print("Yum")
                break
            elif runner_current > coyote_current and runner_current >= final_dist: # if roadrunner stays ahead of coyote and reaches safety
                print("Meep Meep")
                break
        
dist_safe = int(input()) # 100 feet from safety
runner_speed = int(input()) # 5 feet/second
coyote_speed = int(input()) # 20 feet/second

r = Roadrunner()
r.chase(dist_safe, runner_speed, coyote_speed) # Yum

