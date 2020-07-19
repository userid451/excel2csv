from flask import Flask, request, jsonify,render_template,make_response
import pandas as pd
import csv
from io import StringIO

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # User clicked Upload, Start Converting then downloading
        file = request.files['file']
        csv = convert_file(file)
        response = make_response(csv)
        cd = 'attachment; filename=export.csv'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='text/csv'
        return response

    return '''
    <!doctype html>
    <title>Convert Excel to CSV</title>
    <h1>Upload Excel File</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''


def convert_file(path):
    data_xls = pd.read_excel(path,dtype=str, index_col=None)
    data_xls = data_xls.to_csv()
    return data_xls

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)