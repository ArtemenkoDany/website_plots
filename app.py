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
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action2') == 'PLC':
            plot.PLC('', '')
            name = 'PLC'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action3') == 'Gruppierung All':
            plot.Gruppierungall('', '')
            name = 'Gruppierung All'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action4') == 'Produktivitat':
            plot.gr('', '')
            name = 'Produktivitat'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action5') == 'Schicht':
            plot.schicht('', '')
            name = 'Schicht'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action6') == 'Schicht 2-F':
            plot.schichtF('', '')
            name = 'Schicht 2-F'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action7') == 'Schicht 3-S':
            plot.schichtS('', '')
            name = 'Schicht 3-S'
            return render_template("index.html", name=' ', url='/static/plot.png')

        elif request.form.get('action8') == 'Schicht 1-N':
            plot.schichtN('', '')
            name = 'Schicht 1-N'
            return render_template("index.html", name=' ', url='/static/plot.png')
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
