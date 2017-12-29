import sys, json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def main(argv):
    #CONFIG
    monteSimulationRuns = int(sys.argv[1]) if len(sys.argv)>1 else 10
    storySizesFilename = sys.argv[2] if len(sys.argv)>2 else 'countOfStorySize.json'
    distributionsFilename = sys.argv[3] if len(sys.argv)>3 else 'defaultDistribution.json'
    
    velocity = 70 #points per sprint - we won't monte this
    outputfilename = 'MonteOutput.json'
    
    #Load story sizes
    print 'Loading story point sizes from ',storySizesFilename
    data = json.load(open(storySizesFilename))
    print data

    #Load distributiond
    print 'Loading distributions from ',distributionsFilename
    distro = json.load(open(distributionsFilename))
    #covert nestest arrays to tuples
    distributions = {int(float(k)) : tuple(v) for k, v in distro.iteritems()}
    print distributions

    #do some monte!
    monteResults = []
    for x in range(monteSimulationRuns):
        simulatedStoryPoints = []
        for key in data.keys():
            cleanKey = int(float(key))
            dist = distributions[cleanKey]
            #simulate each story
            simulatedStoryPoints.extend(np.random.triangular(*dist, size=data[key]))
        totalPoints = sum(simulatedStoryPoints)
        monteResults.append(totalPoints)
        #print 'Monte run', x,' Total points', totalPoints

    #print some stats
    print 'Executed simulations: ',monteSimulationRuns
    print 'Min simulated points ',min(monteResults)
    print 'Max simulated points ',max(monteResults)
    print 'Avg simulated points ', np.mean(monteResults)

    #show some graphics
    sorted_data = np.sort(monteResults)
    plt.step(sorted_data, np.arange(sorted_data.size))  # From 0 to the number of data points-1
    plt.show()



    #calculate distribution of end dates
    #TODO



    #with open(outputfilename, 'w') as outfile:
    #    json.dump(pointsDist, outfile)
    #    print 'Saved output to', outputfilename
    

if __name__ == "__main__":
    main(sys.argv)
