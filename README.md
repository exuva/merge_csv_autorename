# merge_csv_autorename
Auto rename extension from Xlsm xlsx to csv. Compare the biggest header of all the csv file and adapt all other file from it.

How to use?
Dont need to change any disk directory, all the program has been made to work with this pattern IMPORTANT TO FOLLOW

If you start from blank:
You need Python (> 3.11) => watch my last repo https://github.com/exuva/Python_library

File pattern - recommand to change nothing:

YOURFOLDERNAME
    ->data
    ->Raw data
    HOW_TO.TXT
    Main.py
    TO_RUN.bat


=====TO RUN.BAT========

Double click on the .bat

First the program will check if there's any other table format (.xlsx & .xlsm) and change it to .csv to have the same extension between each files.

Second the program will rename the file 
The name of the file is "Export_X_DD.MM.YYYY_HHhMM.csv"
X is a Z number variable. Starting from the oldest document (document proprety) to the newest. 
The next information are taken from the last date modified of the document (for example the oldest one will have 01.01.1901 00:00 in his property) we will use this file property to fill up the timestamp
DD - Day
MM - Month
YYYY - Year 
HH - Hour
MM - Minute

X's variable will be incremented from the highest number founded at the 7th charactere of the file name.

All this need a condition if any file start with "Export_" don't have to be renamed because the're already have the correct name. In addition we will edit the document property because of changing the table (see PYTHON)

This part of naming the .csv file is finish.

Last part it will run the Python.exe (Main.py -program) --> watch next point

=====Main.py===========

The purpose of this python program is to compare every table, header and balance each of them to have the exact same between themselves.
Why this? Because this is use for a powerbi report. On the PowerQuery editor all the header need to be exactly the same between each tables.
In addition if the user want to add a table it wont be a problem. (dont need to edit 50 tables)

How it works?
First of all it will take the table which has the maximum columns and copy the header of it.
It will past automaticly with the exact same place on the other one.
It will automaticly adjust the new "0" value on the new columns (if missing on one file)

a consol print will show you the difference and what he did through all the file.

By editing the file, the property of each .csv file will be changed. That's why the first step of naming the file is very important.

Thanks.
