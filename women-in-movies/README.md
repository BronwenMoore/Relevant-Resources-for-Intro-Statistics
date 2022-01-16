## Data Overview

This data is queried from https://bechdeltest.com/ - a volunteer run, online database and website dedicated to cataloguing movies that pass and fail the bechdel test. [API Docs](https://bechdeltest.com/api/v1/doc). 


## File by file

### 1. bachdel-abridged.csv

The output of running bachdel.py and then deleting the "id" column. 


| Column name      | Significance |
| ----------- | ----------- |
| year      | Year the movie was released according to IMDB       |
| title   |  The title of the movie        |
| rating   | Number from 0 to 3 (0 means no two women, 1 means no talking, 2 means talking about a man, 3 means it passes the test).        |
| pass   | 0 = the movie failed the test. 1 = the movie passed the test (i.e. its rating was 3).     |


### 2. bachdel-unabridged.csv

The same as above except including the ID column. ID is the unique id according to https://bechdeltest.com. It is used to look up more about the movie in the database if so desired - such as ratings, comments, etc. Look at API docs to learn more.  

### 3. bechdel.py

A script to query the entire https://bechdeltest.com database and return the full movie list with details for each movie. See above for more details. 

### 4. bechdel_calcs.py

A script to aggregate the data in the datbase and output total counts and concrete counts for each decade. 

### 5. output-women-in-movies-by-decades.txt

The output of running bechdel_calcs.py.  

