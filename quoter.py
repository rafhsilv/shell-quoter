#!/usr/bin/env python3

import glob
import random

colours = ('38;5;160;01','38;5;196;01','38;5;202;01','38;5;208;01','38;5;214;01',
               '38;5;220;01','38;5;226;01','38;5;190;01','38;5;154;01','38;5;118;01',
               '38;5;046;01','38;5;047;01','38;5;048;01','38;5;049;01','38;5;051;01',
               '38;5;039;01','38;5;027;01','38;5;021;01','38;5;021;01','38;5;057;01',
               '38;5;093;01')

quotes = glob.glob("quotes/*.txt")

file = open(random.choice(quotes), 'r')
lines = []
for line in file:
    lines.append(line.replace('\n', ''))
file.close()

for index in range(len(lines)):
    print("\033[{}m {}\033[0;m".format(colours[index],lines[index]))
