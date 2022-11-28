# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:27:06 2022

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:24:45 2022

@author: HP
"""

import sqlite3
conn = sqlite3.connect('hearts.db',check_same_thread=False)
c = conn.cursor()


##################################3Symptoms
def create_symptoms():
	c.execute('CREATE TABLE IF NOT EXISTS symptoms(patientId Text,age TEXT, sex TEXT, cp TEXT, trestbps TEXT, chol TEXT, fbs TEXT, restecg TEXT, thalach TEXT, exang TEXT, oldpeak TEXT, slope TEXT, ca TEXT, thal TEXT)')

def add_sysmptoms(patientId,age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal):
	c.execute('INSERT INTO symptoms(patientId, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(patientId, age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal))
	conn.commit()
    
def get_symptoms_per_id(patient_id):
	c.execute('SELECT * FROM symptoms WHERE patientId="{}"'.format(patient_id))
	data = c.fetchall()
	return data

def edit_symptoms(age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal,pid):
	c.execute("UPDATE symptoms SET age=?, sex=?, cp=?, trestbps=?, chol=?, fbs=?, restecg=?,thalach=?,exang=?,oldpeak=?,slope=?,ca=?,thal=?  WHERE patientId=?",(age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal,pid))
	conn.commit()
	data = c.fetchall()
	return data

def view_all_symptoms():
	c.execute('SELECT * FROM symptoms')
	data = c.fetchall()
	return data

def delete_sysmptoms(idno):
	c.execute('DELETE FROM symptoms WHERE patientId="{}"'.format(idno))
	conn.commit()
#################################Patient
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS patient(idnumber TEXT, firstname TEXT, lastname TEXT, gender TEXT, address TEXT, mobile TEXT, username TEXT, password TEXT)')

def add_data(idNo, firstname, lastname, gender, address, mobile, username, password):
	c.execute('INSERT INTO patient(idnumber, firstname, lastname, gender, address, mobile, username, password) VALUES (?,?,?,?,?,?,?,?)',(idNo,firstname,lastname,gender,address,mobile,username,password))
	conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM patient WHERE username =? AND password =?', (username,password))
    data = c.fetchall()
    return data

def view_all_data():
	c.execute('SELECT * FROM patient')
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT DISTINCT idnumber FROM patient')
	data = c.fetchall()
	return data

def get_user(patient_id):
	c.execute('SELECT * FROM patient WHERE idnumber="{}"'.format(patient_id))
	data = c.fetchall()
	return data

def get_user_byid(patient_id):
	c.execute('SELECT * FROM patient WHERE idnumber="{}"'.format(patient_id))
	data = c.fetchall()


def edit_user(firstname, lastname, gender, address, mobile, password,usrname, pid):
	c.execute("UPDATE patient SET firstname=?,lastname=?,gender=? ,address=? ,mobile=? ,password=?  WHERE username=? and idnumber=? ",(firstname, lastname, gender, address, mobile, password, usrname, pid))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(idno):
	c.execute('DELETE FROM patient WHERE idnumber="{}"'.format(idno))
	conn.commit()
###################################Diagnosis
def create_diagnoses():
	c.execute('CREATE TABLE IF NOT EXISTS diagnoses(patientId Text,diagnoses Text)')

def add_diagnoses(patientId,diagnoses):
	c.execute('INSERT INTO diagnoses(patientId, diagnoses) VALUES (?,?)',(patientId, diagnoses))
	conn.commit()
    
def get_diagnoses(patient_id):
	c.execute('SELECT * FROM diagnoses WHERE patientId="{}"'.format(patient_id))
	data = c.fetchall()
	return data

def edit_diagnoses(diagnosis,patientId):
	c.execute("UPDATE diagnoses SET diagnoses=? WHERE patientId=?",(diagnosis,patientId))
	conn.commit()
	data = c.fetchall()
	return data

def view_all_diagnoses():
	c.execute('SELECT * FROM diagnoses')
	data = c.fetchall()
	return data
def delete_diagnosis(idno):
	c.execute('DELETE FROM diagnoses WHERE patientId="{}"'.format(idno))
	conn.commit()