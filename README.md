Started this just before leaving for edinburgh so it is clearly incomplete.
It does Income tax currently, next steps would be to add USC and more configuration for tax credits.
Thoughts for future development: 
1) USC bands are in terms of weekly income so either the bands or the user input will need to be converted. Other than that it should be okay.
2) Add configurability for the tax credits
3) Figure out how to do min(x,0) where x is a numpy vector. the current approach is ugly and should be refactored into a helper function if no solution is found.
4) For visualisation the linegraph is unsatisfactory, perhaps one of those graphs where the area under the line is filled in would be better.
5) Better xlim and ylim proportions (I'm forgetting the term for this- ratio, 16:9 etc) in the visuals
6) Mark chinks in the visuals where the slope of the line (or the ratio of net/gross income) changes
