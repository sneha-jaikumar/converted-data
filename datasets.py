import pandas as pd
from typing import List

from csv import writer
from csv import reader

#function to append a list as a row
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)




#header for csv file
str_list: List[str] = ["HEADER_USER_ID", "HEADER_ACTIVITY", "HEADER_TIMSESTAMP", "HEADER_X-ACCELERATION", "HEADER_Y-ACCELERATION", "HEADER_Z-ACCELERATION", "HEADER_SENSOR_DESCRIPTION","HEADER_PARTICIPANT_DESCRIPTION", "HEADER_SPECIAL_CONSIDERATIONS"]
#adding the header to the csv file
append_list_as_row('test.csv', str_list)
dataframe1 = pd.read_csv('WISDM_ar_v1.1_raw.txt', error_bad_lines=False)
cols = len(dataframe1.axes[1])
for index in range(cols,len(str_list)):
    dataframe1[index] = "\"" + str_list[index].lower() + " is not provided\""
df= dataframe1.to_csv('Acceleration.2012-12-02.sensor.CSV', header=str_list, index= False)




# fileVariable_1 = open('Acceleration.2012-12-02.sensor.CSV', 'r+')
# fileVariable_1. truncate(0)
# fileVariable_1. close()


# default_text = ' is not provided'
# # Open the input_file in read mode and output_file in write mode
# with open('WISDM_ar_v1.1_raw.CSV', 'r') as read_obj, \
#         open('WISDM_ar_v1.1_raw_output.csv', 'w', newline='') as write_obj:
#     # Create a csv.reader object from the input file object
#     csv_reader = reader(read_obj)
#     # Create a csv.writer object from the output file object
#     csv_writer = writer(write_obj)
#     # Read each row of the input csv file as list
#     #for item in str_list_1:
#     for row in csv_reader:
#         # Append the default text in the row / list
#         row.append("objective" + default_text)
#         # Add the updated row / list to the output file
#         csv_writer.writerow(row)
    




# with open('WISDM_ar_v1.1_raw.CSV', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Iterate over each row in the csv using reader object
#     for row in csv_reader:
#         # row variable is a list that represents a row in csv
#         data = list(row)
#         append_list_as_row('test.csv',data)
