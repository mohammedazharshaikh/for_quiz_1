#1
# # from flask import Flask, request, jsonify, send_from_directory
# # app = Flask(__name__)

# # data = {
# #     "apple": {"cost": 19, "pic": "apple.jpg", "descript": "apples are good"},
# #     "berry": {"cost": 20, "descript": "berries are great"},
# #     // Add other products similarly...
# # }

# # @app.route('/getinfo')
# # def get_info():
# #     name = request.args.get('name')
# #     if name in data:
# #         return jsonify({"name": name, **data[name]})
# #     else:
# #         return jsonify({}), 404

# # @app.route('/images/<path:filename>')
# # def images(filename):
# #     return send_from_directory('images', filename)

# # if __name__ == '__main__':
# #     app.run(debug=True)

#2
# from flask import Flask, request, jsonify, send_from_directory
# import csv
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# data = {}

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'message': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'message': 'No selected file'}), 400
#     if file and file.filename.endswith('.csv'):
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)
#         parse_csv(filepath)
#         return jsonify({'message': 'File uploaded and parsed successfully'}), 200
#     return jsonify({'message': 'Invalid file format'}), 400

# def parse_csv(filepath):
#     global data
#     data.clear()
#     with open(filepath, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             name = row['name'].lower()  # Assuming 'name' is the column in the CSV
#             data[name] = {
#                 'cost': row['cost'],
#                 'pic': row['pic'],
#                 'descript': row['descript']
#             }

# @app.route('/getinfo')
# def get_info():
#     name = request.args.get('name', '').lower()
#     if name in data:
#         return jsonify({"name": name, **data[name]})
#     else:
#         return jsonify({}), 404

# @app.route('/images/<path:filename>')
# def images(filename):
#     return send_from_directory('images', filename)

# if __name__ == '__main__':
#     os.makedirs(app.config['UPLOAD
# ---
#3
# from flask import Flask, request, render_template
# import csv

# app = Flask(__name__)

# # Function to load data from CSV
# def load_data():
#     data = {}
#     with open('q1x.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data[row['name']] = {'cost': row['cost'], 'descript': row['descript'], 'picture': row['pic']}
#     return data

# # Load data at the start
# data = load_data()

# # Home page route
# @app.route('/')
# def index():
#     return render_template('index1.html')

# # Result route to handle form data
# @app.route('/search', methods=['POST'])
# def search():
#     name = request.form['name']
#     item = data.get(name, None)
#     if item:
#         return render_template('result.html', item=item, name=name)
#     else:
#         return render_template('error.html', name=name)

# if __name__ == "__main__":
#     app.run(debug=True)
# ---

#4
# from flask import Flask, request, render_template, jsonify
# import csv

# app = Flask(__name__)


# def load_data():
#     data = {}
#     with open('q1x.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data[row['name'].lower()] = {
#                 'cost': row['cost'],
#                 'pic': row['pic'],
#                 'descript': row['descript'],
                
#             }
#     return data

# # Load data when the server starts
# data = load_data()
# print(data)
# # Home page route with form
# @app.route('/')
# def index():
#     return render_template('index1.html')

# # Route to handle form data and display results
# @app.route('/search', methods=['POST'])
# def search():
#     name = request.form['name'].lower()
#     item = data.get(name, None)
#     if item:
#         return render_template('result.html', item=item, name=name) #.capitalizie()
#     else:
#         return render_template('error.html', name=name.capitalize())

# if __name__ == '__main__':
#     app.run(debug=True)
# # ---

#5
from flask import Flask, request, render_template, jsonify, send_from_directory
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'  # Adjust this if your images are in a different folder

# Load data from CSV and include full path for images
def load_data():
    data = {}
    base_path = os.path.abspath(app.config['UPLOAD_FOLDER'])
    with open('q1x.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_path = os.path.join(base_path, row['pic'])
            data[row['name'].lower()] = {
                'cost': row['cost'],
                'pic': image_path,
                'descript': row['descript']
            }
    return data

data = load_data()

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name'].lower()
    item = data.get(name)
    if item:
        return render_template('result.html', item=item, name=name.capitalize())
    else:
        return render_template('error.html', name=name.capitalize())

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

# ---