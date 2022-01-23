# Election_Analysis
Module 3. Python 

## Project Overview
A colorado Board of Elections employee has given you the following tasks to complete the election audit for a recent local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes wach candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.0, Visual Studio Code, 1.63.2

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidates results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette


# Challenge Overview
The election commission has requested some additional data to complete the audit:

1. The voter turnout for each county.
    - Create a county list and county votes dictionary and Extract the county name from each row.
    <img src="/Resources/img1.png" width="50%" height="50%">
    
    <img src="/Resources/img2.png" width="50%" height="50%">
    
    - Write an if statement that checks that the county does not match any existing county in the county list and add a vote to that county's vote count.
    
    <img src="/Resources/img2_2.png" width="50%" height="50%">
    
    
    - Write a script that adds a vote to the county’s vote count as you are looping through all the rows.
    
    <img src="/Resources/img3.png" width="50%" height="50%">
    
2. The percentage of votes from each county out of the total count
    
    <img src="/Resources/img4.png" width="50%" height="50%">

3. The county with the highest turnout

    <img src="/Resources/img5.png" width="50%" height="50%">

## Challenge Results
The analysis of the new request shows that:
- The percentage and number of votes cast by county were:
    - Jefferson county cast 10.5% of the votes and 38,855 votes.
    - Denver county cast 82.8% of the votes and 306,05 votes.
    - Arapahoe county cast 6.7% of the  votes and 24,801 votes.
- The county with the highest turnout:
    - Denver was the county with the largest voter turnout at 306,055 votes.

| Election Results Printed to the Command Line | Election Results Saved to a Text File |
| --- | --- |
| <img src="/Resources/img6.png"> | <img src="/Resources/img7.png"> |

## Challenge Summary
- Print *vote* and *percentage* per candidate in each county
- Print which counties voted for which candidate the most
- Add socio-demographic variables

