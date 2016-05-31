# Used for raw files from Photos application
import os
import argparse
import shutil

parser = argparse.ArgumentParser(description='Move photos into higher folder')

parser.add_argument('folder_location', type=str)

args = parser.parse_args()

#os.chdir(args.folder_location)
year = args.folder_location
path_list = os.listdir(year)
to_delete = []

if not path_list:
    print("empty list")
else:
    for month in path_list:
        if month != '.DS_Store':
            p_name_month = args.folder_location + month

            if os.path.isdir(p_name_month):
                to_delete += [p_name_month]
                p_month = os.listdir(p_name_month)
                for day in p_month:
                    if day != '.DS_Store':
                        p_name_day = p_name_month + '/' + day
                        p_day = os.listdir(p_name_day)
                        for timestamp in p_day:
                            if timestamp != '.DS_Store':
                                p_name_timestamp = p_name_day + '/' + timestamp
                                p_timestamp = os.listdir(p_name_timestamp)
                                for item in p_timestamp:
                                    if item != '.DS_Store':
                                        item_path = p_name_timestamp + '/' + item
                                        #print(item_path)
                                        try:
                                            shutil.move(item_path, year)
                                        except Exception as e:
                                            new_item_path = item_path.rsplit('.')[0] + ' 2.' + item_path.rsplit('.')[1]
                                            print("renaming file "+item_path+" to "+new_item_path)
                                            shutil.move(item_path, new_item_path)
                                            shutil.move(new_item_path, year)

    for month_path in to_delete:
        shutil.rmtree(month_path)
