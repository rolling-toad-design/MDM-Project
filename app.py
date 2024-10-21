from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mdm.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Other models (User, Device) are here...

@app.route('/enroll', methods=['GET', 'POST'])
def enroll_device_via_form():
    if request.method == 'POST':
        device_name = request.form.get('device_name')
        device_type = request.form.get('device_type')

        # Assuming the user is authenticated and user_id is obtained in production
        # For demo purposes, we'll assign a dummy user_id (replace this in production)
        user_id = 1  # Replace with actual user_id
        device_token = 'generated_token_here'

        new_device = Device(device_name=device_name, device_type=device_type, user_id=user_id, device_token=device_token)
        db.session.add(new_device)
        db.session.commit()

        return redirect(url_for('enrollment_success'))
    return render_template('enroll.html')

@app.route('/enrollment_success')
def enrollment_success():
    return "Device successfully enrolled!"

if __name__ == '__main__':
    app.run(debug=True)
# app.py content
