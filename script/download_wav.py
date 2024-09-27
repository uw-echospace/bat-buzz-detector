import csv
import os

# path to the randomized csv file
csv_file = './data/files_for_buzzes.csv'
# alias + bucket name in format 'alias:/bucket_name'
bucket_name = 'liuyisrclone:/bio230143-bucket01'
# path to the folder that you want to save
save_folder = './wav_files'

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # find the 'Sliced File Path' column in the randomized file
        # 'Sliced File Path' has the format: ubna_data_###/recover-###/UBNA_###/###_###.WAV
        folder_path = row['Sliced File Path']

        # build and execute the rclone command
        rclone_command = f"rclone copy {bucket_name}/{folder_path} {save_folder}"
        os.system(rclone_command)

