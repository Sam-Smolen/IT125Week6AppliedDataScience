# IT125Week6AppliedDataScience 
## Overview
This project demonstrates python data visualizations with the Pandas library by creating two Pandas Plots of [bad-drivers.csv from FiveThirtyEight.com](https://raw.githubusercontent.com/fivethirtyeight/data/master/bad-drivers/bad-drivers.csv).   The first plot is a bar chart of the state data as provided.  Then second plot uses [pandas.Dataframe.agg](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html) to create a national summary plot.  See [pandas.Dataframe.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) for generating descriptive summary statistics. To run the Python app "main.py" you will need to run the "pip installs" in the Python Setup Notes.   For more information on using JupyterLab for displaying plots read article https://www.geeksforgeeks.org/python-pandas-dataframe-sample/?ref=lbp https://realpython.com/pandas-plot-python/

![2012 - Number Of Drivers Involved In Fatal Collisions By State](plot_bad_drivers_states.png?raw=true)

![2012 - Number Of Drivers Involved In Fatal Collisions By State](plot_bad_drivers_national.png?raw=true)


## References
### FiveThirtyEight - Bad Drivers 
https://fivethirtyeight.com/features/which-state-has-the-worst-drivers/

https://raw.githubusercontent.com/fivethirtyeight/data/master/bad-drivers/bad-drivers.csv

### Pandas
https://pandas.pydata.org/about/

https://www.w3schools.com/python/pandas/pandas_dataframes.asp

https://www.geeksforgeeks.org/python-pandas-dataframe-sample/?ref=lbp

https://realpython.com/pandas-plot-python/


### JupyterLab
https://jupyter.org/


## Python Notes

pip install pandas matplotlib

pip install jupyterlab

python main.py