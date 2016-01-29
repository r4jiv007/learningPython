"""
Simulator for greedy boss scenario
"""

import math

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    
    # initialize necessary local variables
    
    current_day = 0
    bribe_amnt = INITIAL_BRIBE_COST
    total_bribe = 0
    total_earn = 0
    savings = 0
    days_req = 0
    current_sal=INITIAL_SALARY
    
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0,0)]
    
    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:

        # check whether we have enough savings to bribe without waiting
        if savings  > bribe_amnt:
            factor = int(savings/bribe_amnt)
            savings = savings - (factor * bribe_amnt)
            current_sal += (factor * SALARY_INCREMENT)
            total_bribe += (factor * bribe_amnt)
            bribe_amnt += bribe_cost_increment
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
#	print current_sal , bribe_amnt, (current_day +bribe_amnt/current_sal)
        days_req = int(math.ceil(bribe_amnt/float(current_sal)))
        current_day = current_day+ days_req
	print "current day ",current_day
        total_earn += (days_req * current_sal)
#	print "total earn ",total_earn
        total_bribe += bribe_amnt
#	print "total bribe ",total_bribe
        savings = total_earn-total_bribe
        current_sal += SALARY_INCREMENT
#	print current_sal
        
        # update state of simulation to reflect bribe

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            days_vs_earnings.append([current_day, total_earn,current_sal])
        else:
            days_vs_earnings.append([math.log(current_day), math.log(total_earn)])
   
    return days_vs_earnings




#print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700), (37, 14700)]

print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900), (36, 18600)]
    
