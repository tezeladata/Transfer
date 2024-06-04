# The fact that this random number generation method will
# eventually start to repeat is a potential weakness because it
# allows people to predict what’s coming next, which is exactly
# what we don’t want to happen in situations where we’re
# seeking randomness.

# The idea of a savvy gambler trying to win at roulette is useful
# for evaluating any PRNG. If we are governing a roulette wheel
# with true randomness, no gambler will ever be able to win
# reliably. 

# Our LCG might pass the roulette test if we never
# do more than 32 spins, but after that, a gambler could notice
# the repeating pattern of outputs and start to place bets with
# perfect accuracy. The short period of our LCG has caused it to
# fail the roulette test.

# Related to the idea of a long, full period is the idea of uniform
# distribution, by which we mean that each number within the
# PRNG’s range has an equal likelihood of being output.

# We can see that these mathematical criteria for judging PRNGs
# have some relation to each other: the lack of a long or full
# period can be the cause of a lack of uniform distribution.



# There is no single silver-bullet test that indicates whether
# there’s an exploitable pattern in a PRNG.

# There are 12 Diehard
# tests, each of which evaluates a collection of random numbers
# in a different way. 

# One of the Diehard tests, called the
# overlapping sums test, takes the entire list of random numbers
# and finds sums of sections of consecutive numbers from the
# list. The collection of all these sums should follow the
# mathematical pattern colloquially called a bell curve.

# For random number generators:
def next_random(previous,n1,n2,n3):
    the_next = (previous * n1 + n2) % n3
    return the_next
def list_random(n1,n2,n3):
    output = [1]
    while len(output) <=n3:
        output.append(next_random(output[len(output) - 1],n1,n2,n3))
    return output


def overlapping_sums(the_list,sum_length):
    length_of_list = len(the_list)
    the_list.extend(the_list)
    output = []
    for n in range(0,length_of_list):
        output.append(sum(the_list[n:(n + sum_length)]))
    return output

# Showing output
import matplotlib.pyplot as plt
overlap = overlapping_sums(list_random(211111,111112,300007),12)
plt.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)
plt.title('Results of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()

# The output of this code is a histogram that records the
# frequency of the observed sums. 

# If you squint, you can see that this plot resembles a bell.
# The bell curve, like the golden ratio, appears in many
# sometimes surprising places in math and the universe.
