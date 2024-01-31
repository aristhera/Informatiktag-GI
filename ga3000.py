summe1 = 0
summe2 = 0
summe3 = 0
empfehlung = []
with open('ga3000.csv') as file:
        header = file.readline()
        #header = header.strip()
        for line in file:
                line = line.rstrip().split(',')
                if line[3] < '3':
                    summe1 += int(line[4])
                elif line[3] > '2' and line[3] < '5':
                    summe2 += int(line[4])
                else:
                    summe3 += int(line[4])
        empfehlung.append(summe1)
        empfehlung.append(summe2)
        empfehlung.append(summe3)

# wechsler Gymnasium
gym2 = 0
gym4 = 0
gym6 = 0
wechsel = []
with open('wechsel.csv') as file:
        header = file.readline()
        #header = header.strip()
        for line in file:
            line = line.rstrip().split(',')
            if line[0] == '2':
                gym2 = int(line[2])
            elif line[0] > '2' and line[0] < '5':
                gym4 += int(line[2])
            else:
                gym6 += int(line[2])
        wechsel.append(gym2)
        wechsel.append(gym4)
        wechsel.append(gym6)
print(wechsel)

# Differenz
import numpy as np
a=np.array(empfehlung)
b=np.array(wechsel)
print(a-b)
# oldschool
for i in range(len(wechsel)):
    print(empfehlung[i] - wechsel[i])

# Balkendiagramm
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
import matplotlib.pyplot as plt

empfehlung, wechsel
kess = ['1-2', '3-4', '5-6']
x = np.arange(len(kess))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, empfehlung, width, label='Empfehlung')
rects2 = ax.bar(x + width/2, wechsel, width, label='Wechsel')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('kess')
ax.set_ylabel('SuS')
ax.set_title('Empf/Wechsel')
ax.set_xticks(x)
ax.set_xticklabels(kess)
ax.legend()
plt.show()
