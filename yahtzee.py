"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    mylist = list(set(hand))
    maxval = 0
    for dummy_id in mylist:
        val = dummy_id * hand.count(dummy_id)
        if val > maxval:
            maxval = val
    return maxval


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = set([ dummy_side+1 for dummy_side in range(num_die_sides)])
    length = num_free_dice
    all_seq = gen_all_sequences(outcomes,length)
    total_val = 0
    for dummy_seq in all_seq:
        hand = held_dice + dummy_seq
        total_val += score(hand)
    
    return float(total_val)/(len(all_seq))



def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    power_set = set([()])
    size = len(hand)
    binary_counts = list()
    length = 2 ** size
    for dummy_bin in range(length):
        binary_counts.append(bin(dummy_bin)[2:].rjust(size,'0'))
    for count in binary_counts:
        power_set.add(tuple([hand[i] for i in range(len(count))
                             if count[i] == '1']))
    return power_set




def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_val = 0.0
    max_hold = ()
    all_holds = gen_all_holds(hand)
    for hold in all_holds:
        val = expected_value(hold,num_die_sides,len(hand)-len(hold))
        if val > max_val:
            max_val = val
            max_hold = (max_val,hold)
    
    return max_hold


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
 
#print expected_value((2, 2), 6, 2)    
    
    




