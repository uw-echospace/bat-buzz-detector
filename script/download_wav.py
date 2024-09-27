# You have to change the bucket_name into 'alias:/bucket_name' in order to download the WAV files from the OSN bucket.
import csv
import os

# path to the randomized csv file
csv_file = './data/files_for_buzzes.csv'
# Here to change 
# alias + bucket name in format 'alias:/bucket_name'
bucket_name = ''
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

