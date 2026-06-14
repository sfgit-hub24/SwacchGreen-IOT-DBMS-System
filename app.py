from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret_key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sf2407",
    database="swacchgreen"
)

# HOME
@app.route('/')
def home():
    return render_template('index.html')

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print("REGISTER FORM RECEIVED")

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(name, email, password)

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO Users(Name, Email, Password) VALUES(%s,%s,%s)",
            (name, email, password)
        )
        db.commit()

        print("USER INSERTED")

        return redirect(url_for('login'))

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE Email=%s AND Password=%s",
            (
                request.form['email'],
                request.form['password']
            )
        )

        user = cursor.fetchone()

        if user:
            session['user'] = user[1]
            flash("Login Successful!")
            return redirect(url_for('dashboard'))

        flash("Invalid Login!")
        return redirect(url_for('login'))

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# REPORT
@app.route('/report', methods=['GET', 'POST'])
def report():

    if request.method == 'POST':

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO Complaints(Location, Description, Status) VALUES(%s,%s,%s)",
            (
                request.form['location'],
                request.form['description'],
                "Pending"
            )
        )

        db.commit()

        flash("Complaint Submitted Successfully!")
        return redirect(url_for('dashboard'))

    return render_template('report.html')


# SMART BINS
@app.route('/smartbins')
def smartbins():
    return render_template('smartbins.html')


# ADMIN
@app.route('/admin')
def admin():

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Complaints")
    complaint_count = cursor.fetchone()[0]

    cursor.execute("SELECT Location, Description, Status FROM Complaints")
    complaints = cursor.fetchall()

    return render_template(
        'admin_dashboard.html',
        users=users,
        complaint_count=complaint_count,
        complaints=complaints
    )


# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged Out Successfully!")
    return redirect(url_for('home'))

@app.route('/testinsert')
def testinsert():
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO Complaints(Location, Description, Status) VALUES(%s,%s,%s)",
        ("Test Location", "Test Complaint", "Pending")
    )

    db.commit()

    return "Inserted!"

if __name__ == "__main__":
    app.run(debug=True)