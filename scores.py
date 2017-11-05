'''
Scott Enslin
Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A

'''

import random
random_num = random.randint(0,100)
def grades():
    if (random_num >= 60 and random_num <= 69):
        print "Score: {}; Your Grade is D".format(random_num)
        
    elif (random_num >= 70 and random_num <= 79):
        print "Score: {}; Your Grade is C".format(random_num)
        
    elif (random_num >= 80 and random_num <= 89):
        print "Score: {}; Your Grade is B".format(random_num)
        
    elif (random_num >= 90 and random_num <= 100):
        print "Score: {}; Your Grade is A".format(random_num)
    else:
        print "failed"
        
    print "End of Program"

grades()



