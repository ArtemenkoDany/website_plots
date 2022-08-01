from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import plot

app = Flask(__name__)

name = ''

@app.route('/', methods=['POST', 'GET'])
def index():
    global name
    if request.method == 'POST':
        if request.form.get('action1') == 'Gruppierung':
            plot.Gruppierung('', '')
            name = 'Gruppierung'
            return render_template("index.html", name='This graph allows us to see most clearly the efficiency of each station and evaluate its productivity.\nFor example, '
                                                      'we can see that stations 18, 3 and Global need significant optimisation or complete replacement, due to \n'
                                                      'their zero efficiency and significant consumption of company resources, while station 11 \n'
                                                      'operates almost error-free with extremely high efficiency.\nStation 13 also stands a good chance of having higher '
                                                      'productivity if properly optimised',
                                   url='/static/plot.png')

        elif request.form.get('action2') == 'PLC':
            plot.PLC('', '')
            name = 'PLC'
            return render_template("index.html", name='In this graph we can see a clear visualization of the data for the two Programmable Logic Controllers. '
                                                      'As we can see there is a noticeable correlation between the '
                                                      'MW678_M_CPU and production errors.',
                                   url='/static/plot.png')

        elif request.form.get('action3') == 'Gruppierung All':
            plot.Gruppierungall('', '')
            name = 'Gruppierung All'
            return render_template("index.html", name='In this graph we can observe a clear visualisation of the data for a greater understanding of the productivity'
                                                      ' of the company as a whole',
                                   url='/static/plot.png')

        elif request.form.get('action4') == 'Produktivitat':
            plot.gr('', '')
            name = 'Produktivitat'
            return render_template("index.html", name='This graph gives us information about the percentage of the product successfully produced as a percentage of the total number of units produced.'
                                                      'Thus, we are able to realise that the highest profits of the company will be associated with stations 13, 6, 11, 1.'
                                                      'Stations 18 and 14, on the other hand, need to be urgently optimised and/or replaced due to a complete lack of benefit.',
                                   url='/static/plot.png')

        elif request.form.get('action5') == 'Schicht':
            plot.schicht('', '')
            name = 'Schicht'
            return render_template("index.html", name='This graph gives a clear indication of the productivity of each shift over a period of time', url='/static/plot.png')

        elif request.form.get('action6') == 'Schicht 2-F':
            plot.schichtF('', '')
            name = 'Schicht 2-F'
            return render_template("index.html", name='This graph gives a clear indication of the productivity of each shift over a period of time', url='/static/plot.png')

        elif request.form.get('action7') == 'Schicht 3-S':
            plot.schichtS('', '')
            name = 'Schicht 3-S'
            return render_template("index.html", name='This graph gives a clear indication of the productivity of each shift over a period of time', url='/static/plot.png')

        elif request.form.get('action8') == 'Schicht 1-N':
            plot.schichtN('', '')
            name = 'Schicht 1-N'
            return render_template("index.html", name='This graph gives a clear indication of the productivity of each shift over a period of time', url='/static/plot.png')
        else:
            pass  # unknown
        if request.form['dateto'] != '' or request.form['from'] != '':
            print(name)

            if name == 'Gruppierung':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.Gruppierung(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'PLC':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.PLC(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Schicht':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.schicht(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Schicht 2-F':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.schichtF(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Schicht 3-S':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.schichtS(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Schicht 1-N':
                dateto_input = request.form['dateto']
                datefrom_input = request.form['datefrom']
                plot.schichtN(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Gruppierung All':
                datefrom_input = request.form['datefrom']
                dateto_input = request.form['dateto']
                plot.Gruppierungall(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

            elif name == 'Prodofevrstat':
                datefrom_input = request.form['datefrom']
                dateto_input = request.form['dateto']
                plot.gr(dateto_input, datefrom_input)
                return render_template("index.html", name="from " + datefrom_input + " to " + dateto_input, url='/static/plot.png')

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
