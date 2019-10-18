import csv
import time
import sys
import operator

while True:
    action = float(input( "Get Specifics of one team[1], all teams[2], or calculate the best alliance[3]" ))
    if action == 1:
        with open('responses.csv', 'r') as f:
            reader = csv.reader(f)
            teamwanted = input(" What team do you want to get stats on? ")
            string = teamwanted
            for line in reader:
                print(line)
                for i, row in enumerate(reader):
                    for j, column in enumerate(row):
                        if string in column:
                            print(row)
    if action == 2:
        with open('responses.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            linewanted = input(" What do you want to see, Robot function[2], Starting position[3], Auton Points[4], # of cubes able to stack[5], Towers able to stack in[6], V5 or Cortex[7], Defensive or Offensive[8], Skills Scores[9],  ")
            linenumber = int(linewanted)
            for line in csv_reader:
                print([line[1],line[linenumber]])

    if action == 3:
        with open('responses.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            sort = sorted(csv_reader, key=operator.itemgetter(6))
            my_file_name = "responses.csv"
            cleaned_file = "sorted.csv"
            remove_words = ['short']

            with open(my_file_name, 'r', newline='') as infile, \
                open(cleaned_file, 'w',newline='') as outfile:
                writer = csv.writer(outfile)
                for line in csv.reader(infile, delimiter=','):
                    if not any(remove_word in element
                                for element in line
                                for remove_word in remove_words):   
                        writer.writerow(line)
            with open('sorted.csv', 'r') as sorted_file:
                csv_reader = csv.reader(sorted_file)

                sortagain = sorted(csv_reader, key=operator.itemgetter(4))
                # for eachline in sort:
                #     print(eachline)
                print('Best team at the bottom of list')
                for col in sortagain:
                    
                    print(col[1])

        
        
        

        