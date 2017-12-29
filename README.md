# Monte Python - monte-carlo analysis of shipping date based on story point analyis

This library is source-system agnostic. All that is needed is a json file containing a count of stories by story points. See "countOfStorySize.json" for an example.
Having said that, an adapter script is included to generate this file from the output of the VSTS CLI tool.

## Status:
Early prototype. 
And not to make excuses, but written with a broken thumb in a brace so please excuse the typos!

## Usage:

1. Populate "countOfStorySize.json" file (see below for VSTS example)
2. Generate default distribution parameters (for triangular distribution): `python generateDefaultDistribution.py`
3. Run simulation: `python monteCarlo.py`

Advanced:
`python monteCarlo.py numSimulations countOfStorySize distributionFile`

You can modify the default distribution to be more optimistic or more pessamistic - see neverEarlyDistribution.json as an example!


## VSTS extract:

1. Install the VSTS CLI
2. Generate your access token and login: `vsts login --token xxxxxxxx`
3. In VSTS, create a query to fetch the stories you want to analyse. Find the ID of this report from the URL
4. Use the CLI to extract report as json: `vsts work item query --id xxxxxxxx > queryResult.json`
5. Process the result file: `python extractPointsFromVSTSjson.py`
