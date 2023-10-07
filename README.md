# NBADollarAWin

How much is the NBA dollar worth in terms of team success?

## Project Setup

This is the recommended way to use this project.

### **Clone the repository:**

```sh
git clone https://github.com/marcolagos/NBADollarAWin.git
```

### **Navigate to the directory and use the following command to create a new virtual environment:**

```sh
python -m venv NBADollarAWin_env
```

### **To activate virtual environment, use the following commands:**

Windows

```sh
NBADollarAWin_env/Scripts/activate.bat
```

MacOS

```sh
source NBADollarAWin_env/bin/activate
```

### **Once the virtual environment is activated, you can install packages using pip, and they will be installed only in the virtual environment, not globally on your machine. Use the following command:**

```sh
pip install -r requirements.txt
```

### **When you're finished working in the virtual environment, you can deactivate it using the following command:**

```sh
deactivate
```

## Project Description

General Description: Given a year and given all the values of the relevant x variables for a
specific team during that year's season, predict the number of wins that
that specific team will receive in that season.

### Preprocessing Data

1. Remove asterisks from team name
2. Standardize column names
3. Flip nba_team_wins to have a team column and call this new dataframe variable
   "wins_long".
4. Remove the Unnamed empty columns (that have "NA" value for every
   element in its column) in any dataset.
5. Unit Normal Scaling for both x variables and y variables
6. Adjust the salaries according to CPI not GDP Deflator

### Variables

### Analysis

#### General Information Analysis

the mean, standard deviation, minimum, maximum, and quartiles for each variable.

-   multicollinearity
-   mean of every x variable
-   variance of every x variable
-   mean of the y variable
-   variance of the y variable
-   for every x variable, make a plot of the mean of that x variable across the 20 years.
    If possible, in this plot, you can also draw a vertical line which represents one
    standard deviation in that x variable in that year.
-   correlation coefficients to examine the relationships between variables

1. Call the pairs() function to visualize the multicollinearity between
   every pair of x variables.

#### 3PT Impact over the course of 20 seasons

1. For every year, plot the number of wins over number of 3PT attempts for each team
2. Use the lm function to get the beta coefficients for each of the plots and plot those lines on the plots
3. Create a vector of beta coefficients and plot the vector over corresponding 20 years
4. use the lm function on the vector of beta coefficients and years and plot that line on the plot from step 3
5. Take note of any jumps in the impact of 3PT shots and attribute it a reason such as a player or shift in
   team paradigms.
