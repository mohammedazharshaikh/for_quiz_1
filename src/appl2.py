from flask import Flask, render_template, request, url_for, redirect
import os
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('show_image', name=name))
    return render_template('index22.html')

@app.route('/show_image/<name>')
def show_image(name):
    # Path to the CSV file
    csv_path = 'q1x.csv'  # Adjust the path as needed
    # Path to the image directory
    image_directory = os.path.join(app.static_folder, 'images')
    print(image_directory)
    # Read CSV and find the image file name
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            image_filename = None
            for row in reader:
                if row['Name'].strip().lower() == name.lower():
                    image_filename = row['Picture'].strip()
                    print(image_filename)
                    break

        if image_filename and os.path.exists(os.path.join(image_directory, image_filename)):
            return render_template('display_image.html', image_file=url_for('static', filename=f'images/{image_filename}'), name=name)
        else:
            return render_template('error.html', message=f"Image not available for {name}")
    except Exception as e:
        return render_template('error.html', message=str(e))  # For debugging, show the error message

if __name__ == '__main__':
    app.run(debug=True)
