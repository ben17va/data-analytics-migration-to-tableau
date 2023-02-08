import pandas as pd

class Extractor:
    def __init__(self, file_list):
        self.file_list = file_list

    def process_file(self, file):
        df = pd.read_csv(file)
        sample = df.sample(frac=0.3)  # Take a random sample of 10% of the data
        sample = sample.dropna(axis=1, how='all')
        sample = sample.fillna(0)
        sample = sample.dropna()
        return sample

    def process_all_files(self):
        df_list = []
        for file in self.file_list:
            df = self.process_file(file)
            df_list.append(df)
            master_df = pd.concat(df_list)
            master_df = master_df.dropna()
            return master_df


# List of file names
file_list = ['1987.csv', '1989.csv', '1990.csv', '1991.csv', '1992.csv',
             '1993.csv', '1994.csv', '1995.csv', '1996.csv']


extractor = Extractor(file_list)


master_df = extractor.process_all_files()

print(master_df)

master_df.to_csv("combined_data.csv") 
