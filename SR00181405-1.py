# -*- coding: utf-8 -*-
"""
Created on a cloudy day

@author: AUGUSTO KUUSBERG ELIAS
@id: R00181405
@Cohort: SOFTWARE DEVELOPMENT EVENING
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')

 
def Task1():
    df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
    # Cleansing: take off all the spaces on the cell to avoid problems with extra space
    blackAndWhite = df['color'].str.replace(' ', '') == 'BlackandWhite'

    # prepare the query with the specific conditions (work on black and white movie)
    df2 = df[['actor_1_name']][blackAndWhite]

    # prepare a dataframe with the actor name and the number of movies in black and white
    totalMovie = (df2['actor_1_name'].value_counts()).rename_axis('NAME').reset_index(name='TOTAL MOVIES BLACK AND WHITE')
    
    # prepare the query with the specific conditions (work on at leats black and white movie)
    atLeastTwo = (totalMovie['TOTAL MOVIES BLACK AND WHITE'] >= 2)
    df3 = totalMovie[['NAME', 'TOTAL MOVIES BLACK AND WHITE']][atLeastTwo]
    print(df3)
    
Task1()



def Task2():
    df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
    # variable to store data where movie is longer than 150
    longer = (df['duration'] > 150)
    # variable to store data where movie language is not english
    notEnglish = (df['language'].str.replace(' ', '') != 'English')  
    
    # variable to store name of the countries where the needs are met
    countryName = df['country'][longer][notEnglish]
    
    # use the function unique to show the country names only once
    listOfCountries = pd.unique(countryName)
    print('This is the list of countries who have movies longer than 150 minutes and the language is not english:')
    print(listOfCountries)

Task2()


def Task3():
   df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
   pd.options.display.float_format = '{:.2f}'.format
    # calculate the average value of gross column
   meanGross = df['gross'].mean()
   # THE AVERAGE VALUE OF GROSS IS:  4.846841e+07 or 48468407.52680933
   #replace missing values on gross column by its average
   df['gross'].fillna(meanGross, inplace = True)

    # use group by to group the gross year by year
   groupGrossByYear = df.groupby('title_year')['gross']
   # print the sum of gross for each year
   result = groupGrossByYear.sum()
   print('First column shows the year, second column shows the total income for that year')
   print (result)

    # I decided for that kind of bar graph to best vizualization (but remember the gross on graph need to be multiplied for 1e10)
   result.plot()
   plt.xlabel('Year')
   plt.ylabel('Gross (Value is multiplied by 1e10)')
   
Task3()



def Task4():
    df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
    # Cleansing to remove empty cells based on gross and budget
    dropGross = (df.dropna(subset=['gross']))
    dropBudget = (dropGross.dropna(subset=['budget']))

    # variable to store data where movie is older than 1989
    over1989 = dropBudget[dropBudget['title_year'] > 1989] 
    # variable to store data where movie has gross 2 times or more than budget
    grossOver = over1989[over1989['gross'] >(over1989['budget']*2)]  
    
    # use group by to group based on restrictions of year and income 
    groupByYear = over1989.groupby('title_year')['country'].count()  
    groupByIncome= grossOver.groupby('title_year')['country'].count()
    # calculation to discover the percentade of movies where the gross was more than double of budget
    percentage =  (groupByIncome * 100 )/ groupByYear 
    
    print('First column shows the year, second column shows the percentade of movies where the gross was more than double of budget')
    print(percentage)
    
    # based on the figure of the assigment i decided to use this type of visualization
    percentage.plot()
    plt.xlabel('Year')
    plt.ylabel('Percentage of movies where the gross was more than doble of budget')
    
Task4()


def Task5():
    df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
    # In this task we dont consider movies from UK and USA, so we will drop it
    df.drop(df.index[df['country'] == 'USA'], inplace = True)
    df.drop(df.index[df['country'] == 'UK'], inplace = True)
    
    # In this task we dont consider countries with less than 30 movies, so we will drop it
    counts = df.country.value_counts()
    df2 = df[df.country.isin(counts.index[counts.gt(30)])]

    # Create a variable to store the percentage of movies per country, in a specific query
    percentage = (df2['country'].value_counts(normalize=True) * 100)
    print('First column shows the country and second column shows the percentage of movies for each country')
    print(percentage)

    # Because we are dealing with 100% total, i decided to use pie chart to best vizualization
    plt.pie(percentage, autopct='%1.1f%%', shadow=True, startangle=90, labels=percentage.index)
    plt.title('Percentage of movies per country')
       
Task5()      
       
   

def Task6():
    df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')
    # Cleansing to remove empty cells based on duration
    removeEmptyDuration = (df.dropna(subset=['duration']))

    # Create a variable to store the top 5 most common movies, based on length
    durationMostCommon = removeEmptyDuration['duration'].value_counts().head()
    print ('This are the 5 most popular lengths of a movie (first column) and the number of movies with that length (second column)')
    print(durationMostCommon)

    # I decided for that kind of bar graph to best vizualization 
    durationMostCommon.plot( kind='bar')
    plt.xlabel('Most popular length of a movie in minutes')
    plt.ylabel('Number of movies')

Task6()
