import pandas as pd
import os

dfs = []
count = 0

folder_path = "./data/train_annotations"

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            file.write(lines[0].strip() + ', Notes\n')
            for line in lines[1:]:
                file.write(line.strip() + ', ' + filename + '\n')

        df = pd.read_csv(file_path)

        if count == 0:
            dfs.append(df)
            count += 1
        else:
            dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df.to_csv('./data/train_annotations/merged_data.txt', sep='\t', index=False)
