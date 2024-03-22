from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('AdminLogin.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']

    # Check if username and password are correct (replace this with your actual authentication logic)
    if username == 'admin' and password == '12345':
        # Redirect to adminDashboard.html upon successful login
        return redirect(url_for('admin_dashboard'))
    else:
        # Add authentication failure handling here (e.g., display an error message)
        return render_template('AdminLogin.html', error='Invalid username or password')

@app.route('/adminDashboard')
def admin_dashboard():
    return render_template('adminDashboard.html')


# Dummy database (replace this with your actual database implementation)
violations_database = {
    "violation1": {"license_plate": "ABC123"},
    "violation2": {"license_plate": "XYZ789"}
}

@app.route('/check_violation', methods=['POST'])
def check_violation():
    violation_id = request.form['violation_id']
    license_plate = request.form['license_plate']

    # Check if violation_id and license_plate match with the database
    if violation_id in violations_database and violations_database[violation_id]['license_plate'] == license_plate:
        # Redirect to payment portal page upon successful login
        return redirect(url_for('payment_portal'))
    else:
        # Handle invalid login (e.g., display an error message)
        return "Invalid violation ID or license plate number. Please try again."

@app.route('/paymentportal')
def payment_portal():
    return render_template('paymentportal.html')

if __name__ == '__main__':
    app.run(debug=True)
