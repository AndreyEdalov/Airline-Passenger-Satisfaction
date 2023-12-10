from flask import Flask, render_template, request
import csv

app = Flask(__name__, template_folder="templates")

csv_file_path = 'Data/train.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jupyter_code')
def jupyter_code():
    return render_template('Jupyter_code.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/result', methods=['POST'])
def result():
    selected_gender = request.form.get('gender')
    selected_age = int(request.form.get('age'))

    filtered_data = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Gender'] == selected_gender and int(row['Age']) == selected_age:
                filtered_data.append(row)

    return render_template('result.html', data=filtered_data) 

if __name__ == '__main__':
    app.run(debug=True)
