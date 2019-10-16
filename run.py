import csv
while True:
    action = float(input( "Get Specifics of one team[1] or all teams[2]?" ))
    if action == 1:
        with open('responses.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            teamwanted = input(" What team do you want to get stats on? ")
            team = int(teamwanted)
            data = list(csv_reader)
            print(data[team])
    else:
        with open('responses.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            linewanted = input(" What do you want to see, Robot function[2], Starting position[3], Auton Points[4], # of cubes able to stack[5], Towers able to stack in[6], V5 or Cortex[7], Defensive or Offensive[8], Skills Scores[9],  ")
            linenumber = int(linewanted)
            for line in csv_reader:
                print([line[1],line[linenumber]])
       
