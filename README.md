# dataset-overview-movie

Dataset Overview
For this project we are going to perform a number analytic tasks on the movie_methadata.csv
file. Each row of the dataset contains 28 pieces of information about a movie. Some of those include:

• color
• director_name
• duration
• actor_2_name
• gross
• genres
• actor_1name
• movie_title
• num_voted_users
• actor_3_name
• plot_keywords
• num_user_for_reviews
• language
• country
• content_rating
• budget
• title_year
• imdb_score
• aspect_ratio

1.2 Project Specification
The objective of this project is to provide an insight into some of the relationships and trends that
exist within this dataset. Please note that you can only use Pandas, Numpy and Matplotlib as
means of analysing data within this dataset.

1.2.1 Details of the project specified as a number of tasks

1. Complete the Task1 function in the template file and use groupby in pandas to return the
name of those actors/actresses that have played at least in two Black and White movies.
Actors/actresses’ name can be found in a column with header: actor_1_name.
Data cleansing: Some values in the color column have extra space at the beginning, remove
the spaces from the beginning and the end of each value in the cell.

3. Complete the Task2 function in the template file and extract those country names that have
at least one movie that is longer than 150 and the language is not English.

4. Complete the Task3 function in the template file.
Calculate the the amount of income that is gained in each year. Use an appropriate visualiza-
tion technique and show the yearly income trend from the earliest year until the latest year
in the file. Each movie has a column called gross that can be assumed as the income.
Data Cleansing: Some movies do not have a known income (gross); fill the empty cells in
gross column with the average value of the gross column.

5. Complete the Task4 function in the template file.
Each movie has a column called year (titleyear) that indicates the year that the movie was
made.
For each year, extract the percentage of those movies that their income (gross) is higher than
the doubled of the budget.
Only consider the years after 1989.
Use an appropriate visualization technique to visualize this information. See Figure 1.
Data Cleansing: Remove all the rows from the data frame where they have an empty cell in
gross or budget.

6. Complete the Task5 function in the template file.
Use an appropriate visualization technique that visually depicts the number of movies at each
country. Display the percentage of the number of movies for each country on the visualization.
The USA and the UK and those countries with less then 30 movies should not be considered
for this task.

7. Complete the Task6 function in the template file.
Each movie has a length (duration). Apply an appropriate visualization technique and visually
depict what durations (movie lengths) are more common and popular among all movies in
the file.


Use comment and indicate the common and popular movie lengths.
Data Cleansing: Some movies do not have a known duration, those movies (rows) should be
ignored for this task.

