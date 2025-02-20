import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    infile = open(full_path)
    csvFile = csv.reader(infile)
    header = next(csvFile)
    dicts = {}
    list=[]
    for row in csvFile:
        list.append(row)
    dict_2020 = {}
    for i in range(len(list)):
        dict_2020[list[i][0]] = list[i][1]
    dict_2021 = {}
    for i in range(len(list)):
        dict_2021[list[i][0]] = list[i][2]
    dict_2022 = {}
    for i in range(len(list)):
        dict_2022[list[i][0]] = list[i][3]
    dicts[header[1]] = dict_2020
    dicts[header[2]] = dict_2021
    dicts[header[3]] = dict_2022
    return dicts
    
    # use this 'full_path' variable as the file that you open

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    list = []
    for key in d.keys():
        value = d[key]
        highest = 0
        currentIndex = 'HI'
        for keys in value.keys():
            if highest < int(value[keys]):
                highest = int(value[keys])
                currentIndex = keys
        tup = (key, currentIndex, highest)
        list.append(tup)
    return list

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    dict_ave = {}
    for key in d.keys():
        sum = 0
        count = 12
        ave = 0
        value = d[key]
        for keys in value.keys():
            sum += int(value[keys])
        ave = (sum/count)
        dict_ave[key] = ave
    return dict_ave

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")

    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
