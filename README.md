# Machine-Learning
A repository where i'll push code and data as I learn ML &amp; Data Science. Based on the contents of [this](https://www.udemy.com/machinelearning/) course and other internet ressources.

## Data preprocessing template
A python (& R) template to preprocess your data before running any ML algorithm. Put it at the beginning of your code.
* What it does:
  * Imports the dataset and initializes your dependent and independent variables. (don't forget to put the folder where your data s as your workdir, and to change the arguments of iloc to select the correct columns)
  * Takes care of the missing data. (Uses the mean strategy by default)
  * Encodes your categorical data using the scikit-learn OneHotEncoder
  * Splits the dataset into training and test sets
  * Scales your features
 
## Linear Regression 
A simple linear regression implementing the data preprocessing template. It has been written to analyze the Salary data provided in the folder. 

## Multilinear Regression 
A simple multilinear regression implementing the data preprocessing template. It has been written to analyze the Start-ups data provided in the folder. 

## Polynomial Regression 
A simple polynomial regression implementing the data preprocessing template. It has been written to analyze the Position Salaries data provided in the folder.

## Twitter Sentiment Analysis
**__UPDATE 13/03/2018:__** I am currently working on an improved version. Stay tuned.

An attempt to use the [tweepy](http://www.tweepy.org/) and [textblob](http://textblob.readthedocs.io/en/dev/index.html) to retrieve tweets (through the twitter API) concerning certain queries. It then saves the tweets in a csv and processes the data to tell us what people think about these queries. It's **__NOT__** working at the current moment (I made some changes long ago and I have to review the whole code to understand the problem). 

* **queries**: List of Strings defining the queries. Just change the values to what you want to analyze.
* **hashtag**: String. Refines your search by only selecting the tweets with this hashtag.
* **Since/Until**: String. Defines the time period where you want to search for tweets.
  


