import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

columns = []
col = ""


def set_colums(name):
    if name == 'StateAfter':
        col = "StateAfter"
        columns = ["0", "1"]
    elif name == 'MsgClass':
        col = "MsgClass"
        columns = ["2", "64"]
    elif name == 'PLC':
        col = "PLC"
        columns = ["MW678_F-CPU", "MW678_M-CPU"]
    elif name == 'Gruppierung':
        col = "Gruppierung"
        columns = ["Global", "Station 16", "Station 3", "Station 18", "Station 13", "Station 6", "Station 14",
                   "Station 11", "Station 13", "Station 1"]
    elif name == 'Schicht':
        col = "Schicht"
        columns = ["2-F", "3-S", "1-N"]
    elif name == 'Kalenderwoche':
        col = "Kalenderwoche"
        columns = ["49", "50", "51", "2", "3", "9", "10", "11"]
    else:
        columns = []

    # the_table = plt.table(cellText=cell_text, rowLabels=rows, rowColours=colors, colLabels=columns, loc='bottom')


df = pd.read_csv("ERASMUS_all_data.csv")


def Gruppierungall(g, k):
    tr = 0
    fl = 0
    counter = 0
    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break
    for coll in df["Gruppierung"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "Global":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 16":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 3":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 18":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 13":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 6":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 14":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1

                elif coll == "Station 11":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        tr += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        fl += 1
                counter += 1
            else:
                break
        else:
            if coll == "Global":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 16":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 3":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 18":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 13":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 6":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 14":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1

            elif coll == "Station 11":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    tr += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    fl += 1
            counter += 1

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Betriebsmeldungen', 'Störmeldungen']
    sizes = [tr, fl]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    colors = ['#F08080', '#87CEFA']

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors, )

    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Percent of mistakes overall')
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')


def Gruppierung(g, k):
    Global1 = 0
    Station161 = 0
    Station31 = 0
    Station181 = 0
    Station131 = 0
    Station61 = 0
    Station141 = 0
    Station111 = 0
    Global0 = 0
    Station160 = 0
    Station30 = 0
    Station180 = 0
    Station130 = 0
    Station60 = 0
    Station140 = 0
    Station110 = 0
    Station11 = 0
    Station10 = 0
    counter = 0
    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Gruppierung"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "Global":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Global1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Global0 += 1

                elif coll == "Station 1":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station11 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station10 += 1

                elif coll == "Station 16":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station161 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station160 += 1

                elif coll == "Station 3":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station31 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station30 += 1

                elif coll == "Station 18":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station181 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station180 += 1

                elif coll == "Station 13":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station131 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station130 += 1

                elif coll == "Station 6":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station61 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station60 += 1

                elif coll == "Station 14":

                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station141 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station140 += 1
                elif coll == "Station 11":

                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station111 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        Station110 += 1
                counter += 1
            else:
                break
        else:
            if coll == "Global":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Global1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Global0 += 1
            elif coll == "Station 1":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station11 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station10 += 1
            elif coll == "Station 16":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station161 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station160 += 1
            elif coll == "Station 3":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station31 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station30 += 1
            elif coll == "Station 18":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station181 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station180 += 1

            elif coll == "Station 13":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station131 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station130 += 1
            elif coll == "Station 6":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station61 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station60 += 1
            elif coll == "Station 14":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station141 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station140 += 1
            elif coll == "Station 11":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station111 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    Station110 += 1
            counter += 1

    N = 9
    tr = (Global1, Station161, Station31, Station181, Station131, Station61, Station141, Station111, Station11)
    fl = (Global0, Station160, Station30, Station180, Station130, Station60, Station140, Station110, Station10)
    # plt.plot(df.Name, df.Marks)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(ind, tr, width, color='#F08080')
    ax.bar(ind, fl, width, bottom=tr, color='#87CEFA')
    ax.set_ylabel('Percent of mistakes/failures')
    ax.set_title('Stations')
    ax.set_xticks(ind,
                  ('Global', 'Station16', 'Station3', 'Station18', 'Station13', 'Station6', 'Station14', 'Station11', 'Station1'))
    ax.set_yticks(np.arange(0, 81, 10))
    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')


def gr(g, k):
    Global1 = 0
    Station161 = 0
    Station31 = 0
    Station181 = 0
    Station131 = 0
    Station61 = 0
    Station141 = 0
    Station111 = 0
    Station11 = 0
    counter = 0

    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Gruppierung"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "Global":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Global1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass

                elif coll == "Station 1":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station11 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass

                elif coll == "Station 16":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station161 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                elif coll == "Station 3":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station31 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                elif coll == "Station 18":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station181 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass

                elif coll == "Station 13":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station131 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                elif coll == "Station 6":

                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station61 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                elif coll == "Station 14":

                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station141 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                elif coll == "Station 11":

                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        Station111 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        pass
                counter += 1
            else:
                break
        else:
            if coll == "Global":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Global1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass

            elif coll == "Station 1":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station11 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass

            elif coll == "Station 16":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station161 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            elif coll == "Station 3":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station31 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            elif coll == "Station 18":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station181 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass

            elif coll == "Station 13":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station131 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            elif coll == "Station 6":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station61 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            elif coll == "Station 14":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station141 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            elif coll == "Station 11":

                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    Station111 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    pass
            counter += 1

    N = 9
    tr = (Global1, Station161, Station31, Station181, Station131, Station61, Station141, Station111, Station11)
    all_ = Global1 + Station161 + Station31 + Station181 + Station131 + Station61 + Station141 + Station111 + Station11
    # plt.plot(df.Name, df.Marks)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(ind, tr, width, color='#87CEFA')
    ax.bar(ind, all_, width, bottom=tr, color='#F08080')
    ax.set_ylabel('Productivity of every station')
    ax.set_title('Stations')
    ax.set_xticks(ind,
                  ('Global', 'Station16', 'Station3', 'Station18', 'Station13', 'Station6', 'Station14', 'Station11', 'Station1'))
    ax.set_yticks(np.arange(0, 81, 10))
    ax.legend(labels=['Störmeldungen', 'All'])
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')


# print(df['Schicht'].to_string())

def PLC(g, k):
    MW678_M_CPU1 = 0
    MW678_F_CPU1 = 0
    MW678_M_CPU0 = 0
    MW678_F_CPU0 = 0
    counter = 0
    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["PLC"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "MW678_F-CPU":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        MW678_M_CPU1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        MW678_M_CPU0 += 1

                elif coll == "MW678_M-CPU":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        MW678_F_CPU1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        MW678_F_CPU0 += 1
                counter += 1
            else:
                break
        else:
            if coll == "MW678_F-CPU":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    MW678_M_CPU1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    MW678_M_CPU0 += 1

            elif coll == "MW678_M-CPU":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    MW678_F_CPU1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    MW678_F_CPU0 += 1
            counter += 1

    N = 2
    tr = (MW678_M_CPU1, MW678_F_CPU1)
    fl = (MW678_M_CPU0, MW678_F_CPU0)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(ind, tr, width, color='#F08080')
    ax.bar(ind, fl, width, bottom=tr, color='#87CEFA')
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind, ('MW678_M_CPU', 'MW678_F_CPU'))
    ax.set_yticks(np.arange(0, 81, 10))
    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])

    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')

def schicht(g, k):
    counter = 0
    F1 = 0
    S1 = 0
    N1 = 0
    F0 = 0
    S0 = 0
    N0 = 0
    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Schicht"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "2-F":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        F1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        F0 += 1
                elif coll == "3-S":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        S1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        S0 += 1
                elif coll == "1-N":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        N1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        N0 += 0
                counter += 1
            else:
                break
        else:
            if coll == "2-F":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    F1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    F0 += 1
            elif coll == "3-S":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    S1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    S0 += 1
            elif coll == "1-N":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    N1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    N0 += 0
            counter += 1
    labels = '2-F', '3-S', '1-N'
    sizes = [F1, S1, N1]
    explode = (0, 0, 0.1)  # only "explode" the 2nd slice
    colors = ['#F08080', '#87CEFA', '#7B68EE']

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors, )

    ax.legend(labels=['2-F', '3-S', '1-N'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Schicht')
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')

def schichtF(g, k):
    counter = 0
    F1 = 0
    F0 = 0

    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Schicht"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "2-F":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        F1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        F0 += 1
                counter += 1
            else:
                break
        else:
            if coll == "2-F":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    F1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    F0 += 1
            counter += 1
    labels = '2-F', '3-S', '1-N'
    sizes = [F1, F0]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    colors = ['#F08080', '#87CEFA']

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors, )

    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Schicht 2-F')
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')

def schichtS(g, k):
    counter = 0
    S1= 0
    S0 = 0

    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Schicht"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "3-S":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        S1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        S0 += 1
                counter += 1
            else:
                break
        else:
            if coll == "3-S":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    S1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    S0 += 1
            counter += 1

    sizes = [S1, S0]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    colors = ['#F08080', '#87CEFA']

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors, )

    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Schicht 3-S')
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')

def schichtN(g, k):
    counter = 0
    N1= 0
    N0 = 0

    if k != '':
        while df['TimeString'][counter] != k:
            counter += 1
            if df['TimeString'][counter] == k:
                break

    for coll in df["Schicht"]:
        if g != '':
            if df['TimeString'][counter] != g:
                if coll == "1-N":
                    if df["MsgTyp"][counter] == "Betriebsmeldungen":
                        N1 += 1
                    elif df["MsgTyp"][counter] == "Störmeldungen":
                        N0 += 1
                counter += 1
            else:
                break
        else:
            if coll == "1-N":
                if df["MsgTyp"][counter] == "Betriebsmeldungen":
                    N1 += 1
                elif df["MsgTyp"][counter] == "Störmeldungen":
                    N0 += 1
            counter += 1

    sizes = [N1, N0]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    colors = ['#F08080', '#87CEFA']

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, autopct='%1.1f%%', startangle=90, colors=colors, )

    ax.legend(labels=['Betriebsmeldungen', 'Störmeldungen'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Schicht 1-N')
    plt.savefig('static/plot.png', dpi=300, bbox_inches='tight')

# StateAfter 0 1

# MsgClass 2 64

# PLC MW678_F-CPU MW678_M-CPU

# Gruppierung Global Station 16 Station 3 Station 18 Station 13 Station 6 Station 14 Station 11

# Schicht 2-F 3-S 1-N

# Kalenderwoche 49 50 51 2 3 9 10 11

