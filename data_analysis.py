import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

try

    #load dataset and display the first few rows

    df = pd.read_csv(r'C:\Users\hp\SOFTWARE ENG\Python\week 7\week-7-assignment\irisdata.csv')
    print('\n data loaded successfully')
    print('\n', df.head())

    #clean the dataset
    #verify datatype

    print('data types before cleaning: \n', df.dtypes)


    #fill empty columns with mean 

    df.fillna(df.mean(numeric_only=True), inplace=True)

    #drop duplicates

    df.drop_duplicates()

    #verify cleaning
    print('after cleaning', df.isnull().sum())

    #basic data analysis df.describe()
    print(df.describe())

    #groupings

    grouped = df.groupby('class').agg({'sepal length': 'mean', 'sepal width': 'mean', 'petal length': 'mean', 'petal width': 'mean'} )
    print('Data grouped:', grouped)

    # 5Patterns & Visualization
    print("\n Observations:")
    print("- Petal length and width vary the most and best distinguish species.")
    print("- Setosa has the smallest petals, Virginica the largest.")
    print("- Dataset is clean and balanced (50 samples per species).")

    # line chart
    plt.plot(df.index, df['sepal length'], color='green', label='sepal length')
    plt.plot(df.index, df['petal length'], color='blue', label='petal length')
    plt.title('Line plot of petal length vs sepal length')
    plt.xlabel('Petal length')
    plt.ylabel('sepal length')
    plt.legend()
    plt.show()

    #bar graph

    df.groupby('class')[['sepal length','petal length']].mean().plot(kind='bar')
    plt.title('average sepal and petal length')
    plt.xlabel('class')
    plt.ylabel('average length(cm)')
    plt.legend(title='class')
    plt.show()

    #histogram
    plt.hist(df['petal length'], bins=15, color= 'blue', edgecolor='black')
    plt.title('Histogram of petal length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    #scatter plot
    sns.scatterplot(data=df,x='sepal length', y='petal length', hue='class', palette='deep')
    plt.title('scatter plot: sepal length vs petal length')
    plt.xlabel('sepal length(cm)')
    plt.ylabel('petal length(cm)')
    plt.legend(title='class')
    plt.show()

   # error handling
except FileNotFoundError:
    print('file not found')
except Exception as e:
    print('unexpected error',e)