# Machine-Learning
A repository where i'll push code and data as I learn ML &amp; Data Science. Based on the contents of [this](https://www.udemy.com/machinelearning/) course.

## Data preprocessing template
A python (& R) template to preprocess your data before running any ML algorithm. Put it at the beginning of your code.
* What it does:
  * Imports the dataset and initializes your dependent and independent variables. (don't forget to put the folder where your data s as your workdir, and to change the arguments of iloc to select the correct columns)
  * Takes care of the missing data. (Uses the mean strategy by default)
  * Encodes your categorical data using the scikit-learn OneHotEncoder
  * Splits the dataset into training and test sets
  * Scales your features
  


