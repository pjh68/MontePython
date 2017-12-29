import sys, json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def main(argv):
    #CONFIG
    outputfilename = sys.argv[1] if len(sys.argv)>1 else 'defaultDistribution.json'
    pointsScale = [0,1,2,3,5,8,13,21,40,80]

    #we need to build up the distribution profile for each key in our dictionary of story point sizes
    # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.triangular.html#numpy.random.triangular
    # numpy.random.triangular(left, mode, right, size=None)
    print '### Creating parameters for triangular distributions'
    distributions = {}
    for fibSeqNo in range(len(pointsScale)-1):
        key = pointsScale[fibSeqNo]
        left = pointsScale[fibSeqNo-1] if fibSeqNo-1 >= 0 else 0
        right = pointsScale[fibSeqNo+1] if len(pointsScale)>(fibSeqNo+1) else 100
        mid = key
        dist = (left,mid,right)
        print 'Dist: ',dist
        distributions[key] = dist
    print '###'
    
    #save output
    pprint (distributions)
    with open(outputfilename, 'w') as outfile:
        json.dump(distributions, outfile)
        print 'Saved output to', outputfilename
    

if __name__ == "__main__":
    main(sys.argv)
