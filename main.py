import pandas as pd
import matplotlib.pyplot as plt

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/bad-drivers/bad-drivers.csv"
# bad-drivers.csv columns:
# - State
# - Number of drivers involved in fatal collisions per billion miles
# - Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding
# - Percentage Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired
# - Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted,
# - Percentage Of Drivers Involved In Fatal Collisions Who Had Not Been Involved In Any Previous Accidents
# - Car Insurance Premiums ($)
# - Losses incurred by insurance companies for collisions per insured driver ($)

try: 
    # Read the CSV file into a Pandas Dataframe.
    df = pd.read_csv(filepath_or_buffer=download_url)

    # Print info about the Dataframe
    print(df.info()) 

    pd.options.display.max_rows = 100
    
    f"pd.options.display.max_rows:{pd.options.display.max_rows}"
    f"pd.options.display.max_columns:{pd.options.display.max_columns}"
    
    pd.set_option("display.max.columns", None)

    # Convert percentages ("distracted","alcohol","speeding") to counts and add as new Dataframe columns. 
    df["Number Of Drivers Involved In Fatal Collisions Who Were Distracted"] = df["Number of drivers involved in fatal collisions per billion miles"] * ((100 - df["Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted"]) / 100) 
    df["Number Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired"] = df["Number of drivers involved in fatal collisions per billion miles"] * (df["Percentage Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired"] / 100)
    df["Number Of Drivers Involved In Fatal Collisions Who Were Speeding"] = df["Number of drivers involved in fatal collisions per billion miles"] * (df["Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding"] / 100)

    print(df.info())
    # df.to_csv('bad-drivers_added_counts.csv')  

    # Display horizontal bar chart with each state's numbers.
    df.plot(kind="barh",
            x="State",
            y=["Number of drivers involved in fatal collisions per billion miles",
               "Number Of Drivers Involved In Fatal Collisions Who Were Distracted",
               "Number Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired",
               "Number Of Drivers Involved In Fatal Collisions Who Were Speeding"
              ])

    plt.show()

    # Create a summary Dataframe that aggregates state counts into national counts.
    dfsummary = df.agg(total=('Number of drivers involved in fatal collisions per billion miles', sum ),
                       distracted=('Number Of Drivers Involved In Fatal Collisions Who Were Distracted', sum ),
                       alchohol=('Number Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired', sum ),
                       speeding=('Number Of Drivers Involved In Fatal Collisions Who Were Speeding', sum ))

    print(dfsummary.info())
    print(dfsummary.head())

    dfsummary.plot(kind="bar",
        y=["Number of drivers involved in fatal collisions per billion miles",
           "Number Of Drivers Involved In Fatal Collisions Who Were Distracted",
           "Number Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired",
           "Number Of Drivers Involved In Fatal Collisions Who Were Speeding"
          ])

    plt.show()

    print("Program completed.")

except Exception as e:
    print("Unexpected exception:" + str(e))
