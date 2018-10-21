import unittest
import random

def find_largest_loss(pricesLst):
    
    largest_loss = 0 #set largest loss to zero (no loss remains zero)

    for i in range(1, len(pricesLst)): 

        if pricesLst[i-1] < pricesLst[i]:        #compare adjacent prices (if index1 < index2)
            loss = pricesLst[i] - pricesLst[i-1] #then subtract index1 from index2
                
            if largest_loss < loss: #compare new loss value to the previous largest loss
                largest_loss = loss #if larger then save

    return largest_loss


class TestFindLargestLoss(unittest.TestCase):

    def test_find_largest_loss(self):

        pricesLst = random.sample(range(1, 100000), 99999) # Generate a large random sample, integers used for the sake of simplicity

        print(find_largest_loss(pricesLst))

        #############################################################################

        #Find largest loss using an alternative (slower) method and compare results

        diffLst = [pricesLst[i+1]-pricesLst[i] for i in range(len(pricesLst)-1)] #Find the difference between every price pair
        diffLst.sort() #Quicksort results

        diff_result = diffLst[-1]
        function_result = find_largest_loss(pricesLst) #Store test results
        self.assertEqual(function_result, diff_result) #Compare results (test pass if matching)

        #############################################################################

        #Check result is zero if there is no loss (prices always ascending)

        pricesLst = list(range(100, 0, -5))
        self.assertEqual(find_largest_loss(pricesLst), 0)
 

if __name__ == '__main__':
    unittest.main()