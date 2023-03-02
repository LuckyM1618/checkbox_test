from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process-form', methods=['POST'])
def process_form():
    # in order to get a list of the selections for the checkbox inputs, request.form['key_name'] cannot be used; instead, use request.form.getlist('key_name')
    print(request.form)
    print(request.form.getlist('fav_lang'))
    session['form'] = request.form.getlist('fav_lang')
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)