class Doctor:
    def __init__(self,id,name,specialization,WorkingTime,Qualification,RoomNumber):
        self.id=id
        self.name=name
        self.specialization=specialization
        self.WorkingTime=WorkingTime
        self.Qualification=Qualification
        self.RoomNumber=RoomNumber

#Getter and setters method 
    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id=id

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name

    def getSpecialization(self):
        return self.specialization
    
    def setSpecialization(self,specialization):
        self.specialization=specialization

    def getWorkingTime(self):
        return self.WorkingTime
    
    def setWorkingTime(self,WorkingTime):
        self.WorkingTime=WorkingTime

    def getQualification(self):
        return self.Qualification
    
    def setQualification(self,Qualification):
        self.Qualification=Qualification

    def getRoomNumber(self):
        return self.RoomNumber
    
    def setRoomNumber(self,RoomNumber):
        self.RoomNumber=RoomNumber

    def __str__(self):
        return f"{self.id}_{self.name}_{self.specialization}_{self.WorkingTime}_{self.Qualification}_{self.RoomNumber}"

######################################################

class DoctorManager:
    def __init__(self):
        self.doctor_list=[]
        self.read_doctors_file()
#--------------------------------------------------------        
    def format_dr_info(self, doctor):
        formatted_info = f"{doctor.id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"
        return formatted_info
#---------------------------------------------------------
    def read_doctors_file(self):
        with open('doctors.txt', 'r') as file:
            for line in file:
                doctor_data = line.strip().split('_')
                doctor = Doctor(
                    id=doctor_data[0],
                    name=doctor_data[1],
                    specialization=doctor_data[2],
                    WorkingTime=doctor_data[3],
                    Qualification=doctor_data[4],
                    RoomNumber=doctor_data[5]
                )
                self.doctor_list.append(doctor)
#----------------------------------------------------------
    def enter_dr_info(self):
        id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        WorkingTime=input("Enter Working Time: ")
        Qualification = input("Enter doctor qualification: ")
        RoomNumber = input("Enter doctor room number: ")

        new_doctor = Doctor(
            id=id,
            name=name,
            specialization=specialization,
            WorkingTime=WorkingTime,
            Qualification=Qualification,
            RoomNumber=RoomNumber,
        )
        return new_doctor

#---------------------------------------------------------------
    def Search_by_id(Search_id):
        Search_id=int(input("please Enter the ID of Doctor: "))
        getLines = []
        results = []
        file = open("doctors.txt",'r')
        for line in file:
            getLines.append(line)

        for line in getLines:
            if str(Search_id) in line:
                results.append(line)

        if not results:
            print("Record not found")
        else:
            print(*results)
            print("Record found")
        file.close()
#-----------------------------------------------------------------
    def Search_by_name(Search_name):
        Search_name=input("please Enter the name of Doctor: ")
        getLines = []
        results = []
        file = open("doctors.txt",'r')
        for line in file:
            getLines.append(line)
        for line in getLines:
            if Search_name.lower() in line.lower():
                results.append(line)
        if not results:
            print("Record not found")
        else:
            print(*results)
            print("Record found")
        file.close()
#-----------------------------------------------------------------
    def display_doctor_info(self):
        formatted_data = "" 
        with open('doctors.txt', 'r') as f:
            for line in f:
                id, name, specialization,WorkingTime,Qualification, RoomNumber= line.strip().split('_')
                formatted_data += f"{id:<5}{name:<23}{specialization:<15}{WorkingTime:<15}{Qualification:<15}{RoomNumber}\n"
        return formatted_data
#-----------------------------------------------------------------
    def addDoctor(self):
        new_doctor=DM.enter_dr_info() 
        with open("doctors.txt", "a") as file:
            file.write(
                f"{new_doctor.getId()}\t"
                f"{new_doctor.getName()}\t"
                f"{new_doctor.getSpecialization()}\t"
                f"{new_doctor.getWorkingTime()}\t"
                f"{new_doctor.getQualification()}\t"
                f"{new_doctor.getRoomNumber()}\n"
            )
        print("Doctor whose ID is",new_doctor.getId()," has been added")
        file.close()
#------------------------------------------------------------------    
    def edit_doctor_info(self):
        doctor_id = input("Please enter the ID of the doctor that you want to edit their information: ")
        found = False

        for i, doctor in enumerate(self.doctor_list):
            if doctor.getId() == doctor_id:
                found = True
                print("Found doctor:")
                print(doctor)
                print("Enter new Name: ", end="")
                new_name = input()
                print("Enter new Specialist in: ", end="")
                new_specialization = input()
                print("Enter new Timing: ", end="")
                new_working_time = input()
                print("Enter new Qualification: ", end="")
                new_qualification = input()
                print("Enter new Room number: ", end="")
                new_room_number = input()

                doctor.setName(new_name)
                doctor.setSpecialization(new_specialization)
                doctor.setWorkingTime(new_working_time)
                doctor.setQualification(new_qualification)
                doctor.setRoomNumber(new_room_number)
                
                # Update the doctor_list
                self.doctor_list[i] = doctor
                self.update_doctors_file()
                print("Doctor information updated.")
                break

        if not found:
            print("Doctor not found.")
    def update_doctors_file(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctor_list:
                data = (
                    f"{doctor.getId()}_{doctor.getName()}_{doctor.getSpecialization()}"
                    f"_{doctor.getWorkingTime()}_{doctor.getQualification()}_{doctor.getRoomNumber()}\n"
                )
                file.write(data)
#--------------------------------------------------------------------
DM=DoctorManager()
#====================================================================
class Patient:
    def __init__(self, id="", name="", disease="", gender="", age=""):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender 
        self.age = age 

        #Getter and setters method
    def getid(self):
        return self.id
    
    def getname(self):
        return self.name
    
    def getdisease(self):
        return self.disease
    
    def getgender(self):
        return self.gender
    
    def getage(self):
        return self.age
    
    def setid(self, id):
        self.patientid = id

    def setname(self, patientname):
        self.name = patientname

    def setdisease(self, disease):
        self.disease = disease

    def setgender(self, patientgender):
        self.gender = patientgender

    def setage(self,patient_age):
        self.age=patient_age

    def format_file_layout(self):
         return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

#=================================================================================
class PatientManager:
    def __init__(self):
        self.patient_list=[]
        self.read_patient_file()
#--------------------------------------------------------        
    def format_patient_Info_for_file(self, patient):
        formatted_info = f"{patient.id}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"
        return formatted_info
#---------------------------------------------------------
    def read_patient_file(self):
        with open('patients.txt', 'r') as file:
            for line in file:
                patient_data = line.strip().split('_')
                patient = Patient(
                    id=patient_data[0],
                    name=patient_data[1],
                    disease=patient_data[2],
                    gender=patient_data[3],
                    age=patient_data[4]
                )
                self.patient_list.append(patient)
#----------------------------------------------------------
    def enter_patient_iInfo(self):
        id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")

        new_patient = Patient(
            id=id,
            name=name,
            disease=disease,
            gender=gender,
            age=age,
        )
        return new_patient

#---------------------------------------------------------------
    def search_patient_by_Id(Search_id):
        Search_id=int(input("please Enter the ID of Patient: "))
        getLines = []
        results = []
        file = open("patients.txt",'r')
        for line in file:
            getLines.append(line)

        for line in getLines:
            if str(Search_id) in line:
                results.append(line)

        if not results:
            print("Can't find the Patient with id",Search_id," on the system")
        else:
            print(*results)
            print("Record found")
        file.close()
#-----------------------------------------------------------------
    def display_patient_info(self):
        formatted_data = "" 
        with open('patients.txt', 'r') as f:
            for line in f:
                id, name, disease,gender,age = line.strip().split('_')
                formatted_data += f"{id:<5}{name:<23}{disease:<15}{gender:<15}{age:<15}\n"
        return formatted_data
#-----------------------------------------------------------------
    def addPatient(self):
        new_patient=PM.enter_patient_iInfo() 
        with open("patients.txt", "a") as file:
            file.write(
                f"{new_patient.getid()}\t"
                f"{new_patient.getname()}\t"
                f"{new_patient.getdisease()}\t"
                f"{new_patient.getgender()}\t"
                f"{new_patient.getage()}\n"
            )
        print("Patient whose ID is",new_patient.getid()," has been added")
        file.close()
#------------------------------------------------------------------    
    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the ID of the patient that you want to edit their information: ")
        found = False

        for i, patient in enumerate(self.patient_list):
            if patient.getid() == patient_id:
                found = True
                print("Found Patient:")
                print(patient)
                print("Enter new Name: ", end="")
                new_name = input()
                print("Enter new disease in: ", end="")
                new_disease = input()
                print("Enter gender: ", end="")
                gender= input()
                print("Enter age: ", end="")
                age = input()

                patient.setname(new_name)
                patient.setdisease(new_disease)
                patient.setgender(gender)
                patient.setage(age)
                
                # Update the doctor_list
                self.patient_list[i] = patient
                self.update_patient_file()
                print("Patient whose ID is",patient_id," has been edited.")
                break

        if not found:
            print("Patient not found.")
    def update_patient_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patient_list:
                data = (
                    f"{patient.getid()}_{patient.getname()}_{patient.getdisease()}"
                    f"_{patient.getgender()}_{patient.getage()}\n"
                )
                file.write(data)
#--------------------------------------------------------------------
PM=PatientManager()
#--------------------------------------------------------------------
class management:
    def display_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Managment system Select from the following options, or select 3 to stop: ")
            print('Main Menu:')
            print("1. Doctor ")
            print("2. Patient ")
            print("3. Exit Program")

            choice=input("enter your choice: ")
            if choice == "1":
                self.doctors_submenu()
            elif choice == "2":
                self.patients_submenu()   
            elif choice == "3":
                print("Thanks for using the program. Bye!.")    
                break
            else:
                print("invalid choice. please try again")

    def doctors_submenu(self):
        while True:
            print("Doctors Menu:")
            print("1. Display Doctors list ")
            print("2. Search for doctor by ID ")
            print("3. Search for doctor by name ")
            print("4. Add doctor ")
            print("5. Edit doctor info ")
            print("6. Back to the Main Menu ")

            choice=input("enter your choice: ")
            if choice == "1":
                print(DM.display_doctor_info())
            elif choice == "2":
                DM.search_by_id()
            elif choice == "3":
                DM.Search_by_name()
            elif choice == "4":
                DM.addDoctor()
            elif choice == "5":
                DM.edit_doctor_info()
            elif choice == "6":
                break
            else:
                print("invalid choice. please try again")
    def patients_submenu(self):
        while True:
            print('Main Menu:')
            print("1. displaying patients list, ")
            print("2. searching by id")
            print("3. adding a new patient")
            print("4. editing existing patient information")
            print("5. Return to main menu")

            choice=input("enter your choice: ")
            if choice == "1":
                print(PM.display_patient_info())
            elif choice == "2":
                print(PM.search_patient_by_Id())
            elif choice == "3":
                print(PM.addPatient())
            elif choice == "4":
                print(PM.edit_patient_info_by_id())
            elif choice == "5":
                break
            else:
                print("invalid choice. please try again")
myManagement = management()

myManagement.display_menu()


