from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rekenmachine():
    if request.method == 'POST':
        taal = request.form['taal']
        keuze = request.form['keuze']
        getal1 = float(request.form['getal1'])
        getal2 = float(request.form['getal2'])
        resultaat = None
        fout = None

        if keuze == '1':
            resultaat = getal1 + getal2
        elif keuze == '2':
            resultaat = getal1 - getal2
        elif keuze == '3':
            resultaat = getal1 * getal2
        elif keuze == '4':
            if getal2 != 0:
                resultaat = getal1 / getal2
            else:
                fout = "Fout: Delen door nul is niet toegestaan." if taal == 'nl' else "Error: Division by zero is not allowed."

        return render_template_string(template, taal=taal, resultaat=resultaat, fout=fout)

    return render_template_string(template)

template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Rekenmachine</title>
  </head>
  <body>
    <h1>{{ 'Rekenmachine' if taal == 'nl' else 'Calculator' }}</h1>
    <form method="post">
      <label>{{ 'Kies een taal' if taal == 'nl' else 'Choose a language' }}:</label>
      <select name="taal">
        <option value="nl">Nederlands</option>
        <option value="en">English</option>
      </select><br><br>
      <label>{{ 'Kies een bewerking' if taal == 'nl' else 'Choose an operation' }}:</label>
      <select name="keuze">
        <option value="1">{{ 'Optellen' if taal == 'nl' else 'Addition' }}</option>
        <option value="2">{{ 'Aftrekken' if taal == 'nl' else 'Subtraction' }}</option>
        <option value="3">{{ 'Vermenigvuldigen' if taal == 'nl' else 'Multiplication' }}</option>
        <option value="4">{{ 'Delen' if taal == 'nl' else 'Division' }}</option>
      </select><br><br>
      <label>{{ 'Voer het eerste getal in' if taal == 'nl' else 'Enter the first number' }}:</label>
      <input type="text" name="getal1"><br><br>
      <label>{{ 'Voer het tweede getal in' if taal == 'nl' else 'Enter the second number' }}:</label>
      <input type="text" name="getal2"><br><br>
      <input type="submit" value="{{ 'Bereken' if taal == 'nl' else 'Calculate' }}">
    </form>
    {% if resultaat is not none %}
      <h2>{{ 'Resultaat' if taal == 'nl' else 'Result' }}: {{ resultaat }}</h2>
    {% endif %}
    {% if fout %}
      <h2>{{ fout }}</h2>
    {% endif %}
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
