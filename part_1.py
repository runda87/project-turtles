from datetime import datetime

import csv
from typing import ItemsView


def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object. 
    '''
    return datetime.strptime(date, '%m/%d/%Y')



def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    return date.strftime('%B')



def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
        characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.

    Returns: the formatted string.
    '''
    return f"{text:<{spaces}}"


def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''

    turtle20_21= []

    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv. reader(csv_file)
        for line in reader:
            turtle20_21.append(line)

    # print('2020/2021 Flatback Turtle Migration at Cemetery Beach')

    # i = 0
    # while i < len(turtle20_21):
    #     # print(f"{turtle20_21[i][0]} {turtle20_21[i][1]} {turtle20_21[i][2]} {turtle20_21[i][3]} {turtle20_21[i][4]} {turtle20_21[i][5]}")
    #     # i = i + 1

    return turtle20_21


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''

    # print(f"Number of Nests recorded per month (X = 5 nests):") 



def output_monthly_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false crawls,
       hit rocks and nest predation per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass


def output_nests_per_month_graph(monthly_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass


def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''

    totals = data[1:13]
    oct_nest = []
    oct_false_crawls_count = []
    oct_hit_rocks = []
    oct_hatched_nests = []
    oct_nest_predation = []
    oct_list = []
    oct_n = 0
    oct_fc = 0
    oct_hr = 0
    oct_hn = 0
    oct_np = 0 
    october = 0
    for row in totals:
        # date = convert_mmddyyyy_date(row[0])
        # month = get_month_name(date)
        # if month == "October":
        #     oct_list.append(row[0])
        #     october = october+int(row[0])

      
    #  get the date for the row
    #  if date is in october:
    # increase the october counts
    # otherwise if the date is november
    # increase the november counts
        

            oct_nest.append(row[1])
            oct_n= oct_n+int(row[1])

            oct_false_crawls_count.append(row[2])
            oct_fc= oct_fc+int(row[2])

            oct_hit_rocks.append(row[3])
            oct_hr= oct_hr+int(row[3])

            oct_hatched_nests.append(row[4])
            oct_hn= oct_hn+int(row[4])

            oct_nest_predation.append(row[5])
            oct_np= oct_np+int(row[5])

    # print(october)
    # print(oct_nest)
    # print(oct_n)
    # print(oct_false_crawls_count)
    # print(oct_fc)
    # print(oct_hit_rocks)
    # print(oct_hr)
    # print(oct_hatched_nests)
    # print(oct_hn)
    # print(oct_nest_predation)
    # print(oct_np)

    totals = data[14:43]
    nov_nest = []
    nov_false_crawls_count = []
    nov_hit_rocks = []
    nov_hatched_nests = []
    nov_nest_predation = []
    nov_n = 0
    nov_fc = 0
    nov_hr = 0
    nov_hn = 0
    nov_np = 0 
    for row in totals:
        nov_nest.append(row[1])
        nov_n= nov_n+int(row[1])

        nov_false_crawls_count.append(row[2])
        nov_fc= nov_fc+int(row[2])

        nov_hit_rocks.append(row[3])
        nov_hr= nov_hr+int(row[3])

        nov_hatched_nests.append(row[4])
        nov_hn= nov_hn+int(row[4])

        nov_nest_predation.append(row[5])
        nov_np= nov_np+int(row[5])

    # print(nov_nest)
    # print(nov_n)
    # print(nov_false_crawls_count)
    # print(nov_fc)
    # print(nov_hit_rocks)
    # print(nov_hr)
    # print(nov_hatched_nests)
    # print(nov_hn)
    # print(nov_nest_predation)
    # print(nov_np)

    totals = data[42:73]
    dec_nest = []
    dec_false_crawls_count = []
    dec_hit_rocks = []
    dec_hatched_nests = []
    dec_nest_predation = []
    dec_n = 0
    dec_fc = 0
    dec_hr = 0
    dec_hn = 0
    dec_np = 0 
    for row in totals:
        dec_nest.append(row[1])
        dec_n= dec_n+int(row[1])

        dec_false_crawls_count.append(row[2])
        dec_fc= dec_fc+int(row[2])

        dec_hit_rocks.append(row[3])
        dec_hr= dec_hr+int(row[3])

        dec_hatched_nests.append(row[4])
        dec_hn= dec_hn+int(row[4])

        dec_nest_predation.append(row[5])
        dec_np= dec_np+int(row[5])

    # print(dec_nest)
    # print(dec_n)
    # print(dec_false_crawls_count)
    # print(dec_fc)
    # print(dec_hit_rocks)
    # print(dec_hr)
    # print(dec_hatched_nests)
    # print(dec_hn)
    # print(dec_nest_predation)
    # print(dec_np)

    totals = data[73:103]
    jan_nest = []
    jan_false_crawls_count = []
    jan_hit_rocks = []
    jan_hatched_nests = []
    jan_nest_predation = []
    jan_n = 0
    jan_fc = 0
    jan_hr = 0
    jan_hn = 0
    jan_np = 0 
    for row in totals:
        jan_nest.append(row[1])
        jan_n= jan_n+int(row[1])

        jan_false_crawls_count.append(row[2])
        jan_fc= jan_fc+int(row[2])

        jan_hit_rocks.append(row[3])
        jan_hr= jan_hr+int(row[3])

        jan_hatched_nests.append(row[4])
        jan_hn= jan_hn+int(row[4])

        jan_nest_predation.append(row[5])
        jan_np= jan_np+int(row[5])

    # print(jan_nest)
    # print(jan_n)
    # print(jan_false_crawls_count)
    # print(jan_fc)
    # print(jan_hit_rocks)
    # print(jan_hr)
    # print(jan_hatched_nests)
    # print(jan_hn)
    # print(jan_nest_predation)
    # print(jan_np)

    totals = data[103:115]
    feb_nest = []
    feb_false_crawls_count = []
    feb_hit_rocks = []
    feb_hatched_nests = []
    feb_nest_predation = []
    feb_n = 0
    feb_fc = 0
    feb_hr = 0
    feb_hn = 0
    feb_np = 0 
    for row in totals:
        feb_nest.append(row[1])
        feb_n= feb_n+int(row[1])

        feb_false_crawls_count.append(row[2])
        feb_fc= feb_fc+int(row[2])

        feb_hit_rocks.append(row[3])
        feb_hr= feb_hr+int(row[3])

        feb_hatched_nests.append(row[4])
        feb_hn= feb_hn+int(row[4])

        feb_nest_predation.append(row[5])
        feb_np= feb_np+int(row[5])

    # print(feb_nest)
    # print(feb_n)
    # print(feb_false_crawls_count)
    # print(feb_fc)
    # print(feb_hit_rocks)
    # print(feb_hr)
    # print(feb_hatched_nests)
    # print(feb_hn)
    # print(feb_nest_predation)
    # print(feb_np)

    totals = data[114:115]
    mar_nest = []
    mar_false_crawls_count = []
    mar_hit_rocks = []
    mar_hatched_nests = []
    mar_nest_predation = []
    mar_n = 0
    mar_fc = 0
    mar_hr = 0
    mar_hn = 0
    mar_np = 0 
    for row in totals:
        mar_nest.append(row[1])
        mar_n= mar_n+int(row[1])

        mar_false_crawls_count.append(row[2])
        mar_fc= mar_fc+int(row[2])

        mar_hit_rocks.append(row[3])
        mar_hr= mar_hr+int(row[3])

        mar_hatched_nests.append(row[4])
        mar_hn= mar_hn+int(row[4])

        mar_nest_predation.append(row[5])
        mar_np= mar_np+int(row[5])

    # print(mar_nest)
    # print(mar_n)
    # print(mar_false_crawls_count)
    # print(mar_fc)
    # print(mar_hit_rocks)
    # print(mar_hr)
    # print(mar_hatched_nests)
    # print(mar_hn)
    # print(mar_nest_predation)
    # print(mar_np)

    print(f"Months - Nests  Hatched Nests   False Crawls    Hit Rocks   Nest Predation")
    print(f"October - {oct_n},    {oct_hn},   {oct_fc},   {oct_hr},   {oct_np} ")
    print(f"November - {nov_n},    {nov_hn},   {nov_fc},   {nov_hr},   {nov_np} ")
    print(f"December - {dec_n},    {dec_hn},   {dec_fc},   {dec_hr},   {dec_np} ")
    print(f"January - {jan_n}, {jan_hn},   {jan_fc},   {jan_hr},   {jan_np} ")
    print(f"Feburay - {feb_n}, {feb_hn},   {feb_fc},   {feb_hr},   {feb_np} ")
    print(f"March - {mar_n},   {mar_hn},   {mar_fc},   {mar_hr},   {mar_np} ")



if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')
    # print(all_data)
    monthly_data = transform_daily_to_monthly(all_data)

    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    print()
    output_nests_per_month_graph(monthly_data)
    print()
    output_monthly_statistics(monthly_data)
    print()
    output_overall_statistics(monthly_data)
    print()
