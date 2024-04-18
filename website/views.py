from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import pyodbc

driver = '{ODBC Driver 18 for SQL Server}'
server = 'localhost'
database = 'CrazyCleanCarptes'
username = 'sa'
password = 'reallyStrongPwd123'
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=No')

views = Blueprint('views', __name__)



@views.route('/customer_entry', methods=['GET', 'POST'])
@login_required
def customer_entry():
    if request.method == 'POST':
        cu_first_name = request.form.get('cu_first_name')
        cu_last_name = request.form.get('cu_last_name')
        phone_nu = request.form.get('phone_nu')
        street = request.form.get('street')
        cu_city = request.form.get('cu_city')
        cu_state = request.form.get('cu_state')
        cu_zip = request.form.get('cu_zip')

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer (cu_first_name, cu_last_name, phone_nu, street, cu_city, cu_state, cu_zip) VALUES (?,?,?,?,?,?,?)"
                       , cu_first_name, cu_last_name, phone_nu, street, cu_city, cu_state, cu_zip)
        conn.commit()
        cursor.close()
    return render_template("customer_entry.html", user=current_user) 

@views.route('/')
@login_required
def home():

    return render_template("home.html", user=current_user)

@views.route('/card', methods=['GET', 'POST'])
@login_required
def card():
    if request.method == 'POST':
        card_no = request.form.get('card_no')
        card_fname = request.form.get('card_fname')
        card_lname = request.form.get('card_lname')
        exp_date = request.form.get('exp_date')
        cvc = request.form.get('cvc')
        bank = request.form.get('bank')
        customer_id = request.form.get('customer_id')

        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Card (card_no, card_fname, card_lname, exp_date, cvc, bank, customer_id) VALUES (?,?,?,?,?,?,?)",
                        (card_no, card_fname, card_lname, exp_date, cvc, bank, customer_id))
        except Exception as e:
            flash(f'Error: check that the customer id is valid','error')

        conn.commit()
        cursor.close()

    return render_template("card.html", user=current_user)

@views.route('/employee', methods=['GET', 'POST'])
@login_required
def employee():
    if request.method == 'POST':
        em_first_name = request.form.get('em_first_name')
        em_last_name = request.form.get('em_last_name')

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Employee (em_first_name, em_last_name) VALUES (?,?)",
                       (em_first_name, em_last_name))
        conn.commit()
        cursor.close()

    return render_template("employee.html", user=current_user)

@views.route('/appointments', methods=['GET', 'POST'])
@login_required
def appointments():
    if request.method == 'POST':
        service_id = request.form.get('service_id')
        appt_date = request.form.get('appt_date')
        appt_time = request.form.get('appt_time')
        customer_id = request.form.get('customer_id')

        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Appointments (service_id, appt_date, appt_time, customer_id) VALUES (?,?,?,?)",
                        (service_id, appt_date, appt_time, customer_id))
        except Exception as e:
            flash(f'Error: check that the customer id is valid: {e}','error')
        conn.commit()
        cursor.close()

    # Fetch appointments to display
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CurrentAppointments")
    appointments = cursor.fetchall()
    cursor.close()
    return render_template("appointments.html", user=current_user, appointments=appointments)


@views.route('/service_record', methods=['GET', 'POST'])
@login_required
def service_record():
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        service_cost = request.form.get('service_cost')

        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO ServiceRecord (customer_id, service_cost) VALUES (?,?)",
                        (customer_id, service_cost))
        except Exception as e:
            flash(f'Error: check that the employee id is valid: {e}','error')
        conn.commit()
        cursor.close()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ServiceRecord")
    records = cursor.fetchall()
    cursor.close()

    return render_template("service_record.html", user=current_user, records=records)


