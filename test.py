from dynamic_knapsack import *
from knapsack_brute import *
from Fractinol_brute import*
from greedy import *
import unittest

class TestKnapsack(unittest.TestCase):

    #Mixed weight
    def test_01_brute(self):
        p = [40, 60, 10, 20, 50]
        w = [20, 30, 10, 5, 25]
        m = 70  
        input = brute_01_knapsack(p, w, m)
        output = 140
        
        self.assertEqual(input, output)
    #Increasing weight
    def test_02_brute(self):
        p = [60, 100, 120]
        w = [10, 20, 30]
        m = 50
        input = brute_01_knapsack(p, w, m)
        output = 220
        self.assertEqual(input, output)
  
    
    def test01_func_brute(self):
        p = [40, 60, 10, 20, 50]
        w = [20, 30, 10, 5, 25]
        m = 70  
        input = brute_func_knapsack(p, w, m)
        output = 146
        self.assertEqual(input, output)    
    #Constant weight
    def test_03_func_brute(self):
        p = [10, 20, 30]
        w = [1, 1, 1]
        m = 2
        input = brute_func_knapsack(p, w, m)
        output = 50
        self.assertEqual(input, output)


    def test01_func_greedy(self):
        p = [40, 60, 10, 20, 50]
        w = [20, 30, 10, 5, 25]
        m = 70  
        input = greedy_knapsack(p, w, m)
        output = 150
        
        self.assertEqual(input, output)
    #Smaller values
    def test_05_greedy(self):
        p = [24, 18, 18, 10]
        w = [24, 10, 10, 7]
        m = 25
        input = greedy_knapsack(p, w, m)
        output = 43
        self.assertEqual(int(input), output)


    def test_func_dynamic(self):
        p = [40, 60, 10, 20, 50]
        w = [20, 30, 10, 5, 25]
        m = 70  
        n = len(p)
        input = knapsack(p,w,m,n)
        output =40
        
        self.assertEqual(input, output)
    #No items Fit
    def test_func_dynamic(self):
        p = [40, 60, 10, 20, 50]
        w = [20, 30, 10, 5, 25]
        m = 4
        n = 3
        input = knapsack(p,w,m,n)
        output =0
        
        self.assertEqual(input, output)
    

                
if __name__ == '__main__':
    unittest.main()