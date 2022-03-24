# Election Analysis

## Overview of Election Audit
We are given a raw dataset by the Colorado Election comission containing all the votes. For each vote, there are the Ballot ID, County Name and Candidate Name.
Election Officials need our help to be able to see how each county and each candidate have done in the election. The dataset is a comma separated file with close to 370K rows and it's close to impossible (very time-consuming) to manually get the information the commission needs.\

## Election Audit Results
With the help of some scripting, we were able to go through each row of the data and gather the information we need, such as the number of votes each candidate has received.
### *Total Number of Votes:*
Total number of votes cast in this congresssional election was counted to be 369,711

### *County Votes:*
We also counted total vote cast by each county and the percentage of the votes by counties:

- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

*We determined that the county that had the largest turnout was **Denver**.*

### *Candidate Votes:*
Then we also were able to get the number of votes for each candidate and were able to calculate the percentage of the votes for each of the candidates: 

- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

so, we were able to declare the winning candidate of this congressional election along with the vote count and the percantage of the votes received.

- **Winner:** *Diana DeGette*
- **Winning Vote Count:** *272,892*
- **Winning Percentage:** *73.8%*


## Election Audit Summary
