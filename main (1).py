import pandas as pd
import seaborn as sns

def main():
    data = pd.read_csv("/home/movies.csv")
    data = data.dropna()



if __name__ == '__main__':
    main()