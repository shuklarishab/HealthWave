from django.shortcuts import render,redirect
import MySQLdb

# Create your views here.
def home(req):
	return render(req,"Home.html")

def appointment(req):
	return render(req,"Appointment.html")

def appointmentData(req):
	appfor=req.GET['appointmentfor']
	appfname=req.GET['fname']
	applname=req.GET['lname']
	appgender=req.GET['gender']
	appmobile=req.GET['number']
	appday=req.GET['DOBDay']
	appmonth=req.GET['DOBMonth']
	appyear=req.GET['DOBYear']
	appadress=req.GET['adress']
	appemail=req.GET['email']
	appstate=req.GET['state']
	appcountry=req.GET['city']
	apphealthinsurance=req.GET['healthinsurance']
	appattendedfacility=req.GET['facility']
	appappointmenttype=req.GET['appointmenttype']
	appday=int(appday)
	appyear=int(appyear)

	con=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cur=con.cursor()
	query="insert into Appointment_Info(Appointment_For,F_Name,L_Name,Gender,Mob_No,BDay_Date,BDay_Month,BDay_Year,Address,E_Mail,State,City,Insurance,Previously_Attended,Appointment_Type) values('%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d','%s', '%s', '%s', '%s', '%s','%s','%s')"%(appfor,appfname,applname,appgender,appmobile,appday,appmonth,appyear,appadress,appemail,appstate,appcountry,apphealthinsurance,appattendedfacility,appappointmenttype)
	out=cur.execute(query)
	con.commit()
	con.close()
	return redirect("/appointment")

def donate(req):
	return render(req,"Donate.html")

def donationSubmit(req):
	donFname=req.GET['fname']
	donLname=req.GET['lname']
	donEmail=req.GET['email']
	donCountry=req.GET['country']
	donAddress=req.GET['address']
	donCity=req.GET['city']
	donNumber=req.GET['number']
	donPostcode=req.GET['postcode']
	donType=req.GET['donationtype']
	donAmount=req.GET['amount']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="insert into Donation_Info(F_Name,L_Name,E_Mail,Country,Address,City,Mobile_No,PostCode,Donation_Type,Donation_Amount) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(donFname,donLname,donEmail,donCountry,donAddress,donCity,donNumber,donPostcode,donType,donAmount)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()
	return redirect("/donate")

def login(req):
	return render(req,"Login.html")

def loginsubmit(req):
	login_e_mail=req.GET['email']
	login_pass_word=req.GET['pass']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Admins_Info where E_Mail='{}' and Password='{}'".format(login_e_mail,login_pass_word)
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	for row in data:
		if row[0]>0:
			return redirect("/admins/?name="+row[1]+" "+row[2])

def about(req):
	return render(req,"About.html")

def contact(req):
	return render(req,"Contact.html")

def department(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select D_Name from Department_Info"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Department.html",{"data":data})

def ophthalmology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Ophthalmology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Ophthalmology_Department.html",{'data':data})

def orthopedics(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Orthopedics'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Orthopedics_Department.html",{'data':data})

def cardiology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Cardiology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Cardiology_Department.html",{'data':data})

def nephrology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Nephrology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Nephrology_Department.html",{'data':data})

def pathology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Pathology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Pathology_Department.html",{'data':data})

def neurology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Neurology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Neurology_Department.html",{'data':data})

def oncology(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select Doc_Name from Doctors_Info where Doc_Department='Oncology'"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"Oncology_Department.html",{'data':data})

def admin(req):
	if 'name' in req.GET:
		name=req.GET['name']
		return render(req,"Admin.html",{'name':name});
	else:
		return redirect('/login')

def departmentAdminPage(req):
	return render(req,"DepartmentAdminPage.html")

def showDepartmentInsertPageAdmin(req):
	return render(req,"DepartmentAdminInsertPage.html")

def insertDepartmentInfo(req):
	dId=req.GET['d_id']
	dName=req.GET['d_nm']
	dId=int(dId)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="insert into Department_Info(D_Id,D_Name) values ({},'{}')".format(dId,dName)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()
	return redirect("/showDepartmentInfoPageAdmin")

def showDepartmentRecordsInfoPageAdmin(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Department_Info"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"DepartmentAdminRecordsInfoPage.html",{"data":data})

def showUpdateDepartmentInfoPage(req):
	dId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Department_Info where D_Id={}".format(dId)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"DepartmentAdminUpdatePage.html",{'record':row})

def UpdateDepartmentDataAdmin(req):
	dName=req.GET['d_nm']
	dId=req.GET['d_id']
	dId=int(dId)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="update Department_Info set D_Name='{}' where D_Id={}".format(dName,dId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDepartmentRecordsInfoPageAdmin")

def deleteDepartmentData(req):
	dId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="delete from Department_Info where D_Id={}".format(dId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDepartmentRecordsInfoPageAdmin")

def doctorAdminPage(req):
	return render(req,"DoctorAdminPage.html")

def showDoctorInsertPageAdmin(req):
	return render(req,"DoctorAdminInsertPage.html")

def insertDoctorInfo(req):
	docId=req.GET['doc_id']
	docName=req.GET['doc_nm']
	docPic=req.GET['doc_pic']
	docDept=req.GET['doc_dept']
	docId=int(docId)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="insert into Doctors_Info(Doc_Id,Doc_Name,Doc_Pic,Doc_Department) values ({},'{}','{}','{}')".format(docId,docName,docPic,docDept)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()
	return redirect("/showDoctorRecordsInfoPageAdmin")

def showDoctorRecordsInfoPageAdmin(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Doctors_Info"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"DoctorAdminRecordsInfoPage.html",{"data":data})

def showUpdateDoctorInfoPage(req):
	docId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Doctors_Info where Doc_Id={}".format(docId)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"DoctorAdminUpdatePage.html",{'record':row})

def UpdateDoctorDataAdmin(req):
	docId=req.GET['doc_id']
	docName=req.GET['doc_nm']
	docPic=req.GET['doc_pic']
	docDept=req.GET['doc_dept']
	docId=int(docId)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="update Doctors_Info set Doc_Name='{}',Doc_Pic='{}',Doc_Department='{}' where Doc_Id={}".format(docName,docPic,docDept,docId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDoctorRecordsInfoPageAdmin")

def deleteDoctorData(req):
	docId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="delete from Doctors_Info where Doc_Id={}".format(docId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDoctorRecordsInfoPageAdmin")

def appointmentAdminPage(req):
	return render(req,"AppointmentAdminPage.html")

def showAppointmentRecordsInfoPageAdmin(req):
	con=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")	
	cur=con.cursor()
	query="select * from Appointment_Info"
	cur.execute(query)
	data=cur.fetchall()
	con.close()

	return render(req,"AppointmentAdminRecordsInfoPage.html",{"data":data})

def showUpdateAppointmentInfoPage(req):
	appId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Appointment_Info where App_Id={}".format(appId)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"AppointmentAdminUpdatePage.html",{'record':row})

def UpdateAppointmentDataAdmin(req):
	appId=req.GET['app_id']
	appFor=req.GET['app_for']
	appF_Name=req.GET['app_f_nm']
	appL_Name=req.GET['app_l_nm']
	appGen=req.GET['gen']
	appMob=req.GET['mob_no']
	appDate=req.GET['b_date']
	appMonth=req.GET['b_month']
	appYear=req.GET['b_year']
	appAddress=req.GET['addr']
	appEmail=req.GET['email']
	appState=req.GET['state']
	appCity=req.GET['city']
	appInsurance=req.GET['hea_insu']
	appFacility=req.GET['att_faci']
	appType=req.GET['app_type']
	appId=int(appId)
	appDate=int(appDate)
	appYear=int(appYear)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="update Appointment_Info set Appointment_For='%s',F_Name='%s',L_Name='%s',Gender='%s',Mob_No='%s',BDay_Date='%d',BDay_Month='%s',BDay_Year='%d',Address='%s',E_Mail='%s',State='%s',City='%s',Insurance='%s',Previously_Attended='%s',Appointment_Type='%s' where App_Id='%d'"%(appFor,appF_Name,appL_Name,appGen,appMob,appDate,appMonth,appYear,appAddress,appEmail,appState,appCity,appInsurance,appFacility,appType,appId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showAppointmentRecordsInfoPageAdmin")

def deleteAppointmentData(req):
	appId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="delete from Appointment_Info where App_Id={}".format(appId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showAppointmentRecordsInfoPageAdmin")

def loginAdminPage(req):
	return render(req,"LoginAdminPage.html")

def showLoginRecordsInfoPageAdmin(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Admins_Info"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"LoginAdminRecordsInfoPage.html",{"data":data})

def showUpdateLoginInfoPage(req):
	adminId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Admins_Info where Id={}".format(adminId)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"LoginAdminUpdatePage.html",{'record':row})

def UpdateLoginDataAdmin(req):
	adminId=req.GET['ad_id']
	fname=req.GET['ad_f_nm']
	lname=req.GET['ad_l_nm']
	email=req.GET['ad_email']
	password=req.GET['ad_pass']
	gender=req.GET['ad_gen']
	mobile=req.GET['ad_cont']
	address=req.GET['ad_addr']
	state=req.GET['ad_state']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="update Admins_Info set First_Name='{}',Last_Name='{}',E_Mail='{}',Password='{}',Gender='{}',Contact_Num='{}',Address='{}',State='{}' where Id={}".format(fname,lname,email,password,gender,mobile,address,state,adminId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showLoginRecordsInfoPageAdmin")

def deleteLoginData(req):
	adminId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="delete from Admins_Info where Id={}".format(adminId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showLoginRecordsInfoPageAdmin")

def donationAdminPage(req):
	return render(req,"DonationAdminPage.html")

def showDonationRecordsInfoPageAdmin(req):
	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Donation_Info"
	cursor.execute(query)
	data=cursor.fetchall()
	cursor.close()
	conn.close()

	return render(req,"DonationAdminRecordsInfoPage.html",{"data":data})

def showUpdateDonationInfoPage(req):
	donId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="select * from Donation_Info where Don_Id={}".format(donId)
	cursor.execute(query)
	row=cursor.fetchone()
	cursor.close()
	conn.close()

	return render(req,"DonationAdminUpdatePage.html",{'record':row})

def UpdateDonationDataAdmin(req):
	donId=req.GET['don_id']
	donFname=req.GET['don_f_nm']
	donLname=req.GET['don_l_nm']
	donEmail=req.GET['email']
	donCountry=req.GET['country']
	donAddress=req.GET['addr']
	donCity=req.GET['city']
	donNumber=req.GET['mob_no']
	donPostcode=req.GET['postcode']
	donType=req.GET['donationtype']
	donAmount=req.GET['donationamount']
	donId=int(donId)

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="update Donation_Info set F_Name='{}',L_Name='{}',E_Mail='{}',Country='{}',Address='{}',City='{}',Mobile_No='{}',PostCode='{}',Donation_Type='{}',Donation_Amount='{}' where Don_Id={}".format(donFname,donLname,donEmail,donCountry,donAddress,donCity,donNumber,donPostcode,donType,donAmount,donId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDonationRecordsInfoPageAdmin")

def deleteDonationData(req):
	donId=req.GET['id']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="delete from Donation_Info where Don_Id={}".format(donId)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/showDonationRecordsInfoPageAdmin")

def signup(req):
	return render(req,"Signup.html");

def signupAdmin(req):
	fname=req.GET['fname']
	lname=req.GET['lname']
	email=req.GET['email']
	password=req.GET['pass']
	repassword=req.GET['repass']
	gender=req.GET['gender']
	mobile=req.GET['cont_no']
	address=req.GET['address']
	state=req.GET['state']

	conn=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")
	cursor=conn.cursor()
	query="insert into Admins_Info(First_Name,Last_Name,E_Mail,Password,Gender,Contact_Num,Address,State) values('%s', '%s', '%s', '%s', '%s' ,'%s', '%s', '%s')"%(fname,lname,email,password,gender,mobile,address,state)
	cursor.execute(query)
	conn.commit()
	cursor.close()
	conn.close()

	return redirect("/login")

# def showDonationData(req):
# 	con=MySQLdb.connect("localhost","root","animeshroot@123","HealthWave")	
# 	cur=con.cursor()
# 	query="select * from Donation_Info"
# 	cur.execute(query)
# 	data=cur.fetchall()
# 	con.close()

# 	return render(req,"DonateView.html",{"data":data})