import sys, json
from collections import Counter
from pprint import pprint

def main(argv):
    #open up supplied file
    filename = sys.argv[1] if len(sys.argv)>1 else 'queryResult.json'
    outputfilename = sys.argv[2] if len(sys.argv)>2 else 'countOfStorySize.json'
    print 'Loading work items from ',filename
    data = json.load(open(filename))
    print 'Found', len(data), 'work items'

    #parsing the json
    fields = list(map(lambda x: x[u'fields'], data))
    #TODO: more sophisticated handling of no story points field (e.g. bugs)
    points = list(map(lambda x: x[u'fields'].get(u'Microsoft.VSTS.Scheduling.StoryPoints',0),data))
    pointsDist = Counter(points)
    pprint(pointsDist)
    with open(outputfilename, 'w') as outfile:
        json.dump(pointsDist, outfile)
        print 'Saved output to', outputfilename

if __name__ == "__main__":
    main(sys.argv)
