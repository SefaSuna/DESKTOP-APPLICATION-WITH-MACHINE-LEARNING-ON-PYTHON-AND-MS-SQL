
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PYQT5_SETTINGS import * #APPEARANCE SETTINGS OF THE PROGRAM
import pypyodbc 
from MACHINE_LEARNING_METHOD import * #MACHINE LEARNING ALGORITHM

app=QApplication(sys.argv)
win=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(win)
win.show()
#TAKE ATTRIBUTE VALUES
gender1=ui.GENDER1.currentText()
experience1=ui.EXPERINENCE1.text()
department1=ui.DEPARTMENT1.currentText()
position1=ui.POSITION1.currentText()
predict1=ui.PREDICT.text()


#CONNECT TO MY SQL SERVER TO TAKE DATA
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-ALKJBUB;'
    'Database=PERSON;'
    'Trusted_Connection=True;'
)
imlec=db.cursor()
#SHOW DATA WHICH TAKEN FROM SQL SERVER
def listele():
    ui.TABLE.clear()
    imlec.execute("select NAME,SURNAME,GENDER,EXPERIENCE,DEPARTMENT,POSITION,SALARY from PERSON_INFO")
    for satırindex,satırveri in enumerate(imlec):
        for sutunındex,sutunveri in enumerate(satırveri):
            ui.TABLE.setItem(satırindex,sutunındex,QTableWidgetItem(str(sutunveri)))
       
ui.SHOW_DATA.clicked.connect(listele)

def ABOUT():
    msgBox = QMessageBox()
    msgBox.setWindowTitle("WARNING")
    msgBox.setText("THIS APPLICATION IS MADE BY SEFA SUNA")
    msgBox.exec_()

ui.actionABOUT.triggered.connect(ABOUT)

#ADD DATA TO SQL SERVER
def add_d():
    name=ui.NAME.text()
    surname=ui.SURNAME.text()
    gender=ui.GENDER.currentText()
    experience=ui.EXPERIENCE.text()
    department=ui.DEPARTMENT.currentText()
    position=ui.POSITION.currentText()
    salary=ui.SALARY.text()
    liste=[name,surname,gender,experience,department,position,salary]
    a=[]
    b=[]
    for i in liste:
        if i=='' or i==0:
            a.append(i)

        elif i!='' and i!=0:
            b.append(i)
    if len(b)!=7:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("WARNING")
        msgBox.setText("EMPTY VALUE EXIST")
        msgBox.exec_()
        
            
    elif len(b)==7:
                
        imlec.execute("insert into PERSON_INFO(NAME,SURNAME,GENDER,EXPERIENCE,DEPARTMENT,POSITION,SALARY) \
                    values(?,?,?,?,?,?,?)",(name,surname,gender,experience,department,position,salary))
        db.commit()
        ui.TABLE.clear()
        imlec.execute("select NAME,SURNAME,GENDER,EXPERIENCE,DEPARTMENT,POSITION,SALARY from PERSON_INFO")
        for satırindex,satırveri in enumerate(imlec):
            for sutunındex,sutunveri in enumerate(satırveri):
                ui.TABLE.setItem(satırindex,sutunındex,QTableWidgetItem(str(sutunveri)))
        msgBox = QMessageBox()
        msgBox.setWindowTitle("SUCCESSFUL")
        msgBox.setText("DATA IS ADDED")
        msgBox.exec_()
      
ui.ADD_DATA.clicked.connect(add_d)
#PREDICT WITH MACHINE LEARNING METHOD TO GIVEN INPUT VALUES
def predict():
    gender1=ui.GENDER1.currentText()
    experience1=[int(ui.EXPERINENCE1.text())]
    department1=ui.DEPARTMENT1.currentText()
    position1=ui.POSITION1.currentText()
    predict1=ui.PREDICT.text()
    MALE=0
    FEMALE=0
    BİLGİ_TEKNOLOJİLERİ=0
    MUHASEBE=0
    SATIŞ=0
    İNSAN_KAYNAKLARI=0
    PLANLAMA=0
    PAZARLAMA=0
    YÖNETİM=0
    İLETİŞİM=0
    FİNANS=0
    SATINALMA=0

    İLETİŞİM_MÜDÜR_YRD=0,
    İNSAN_KAYNAKLARI_MEMURU=0,
    PAZARLAMA_MÜDÜRÜ=0,
    GENEL_MÜDÜR=0,
    BİLGİ_TEKNOLOJİLERİ_MEMURU=0,
    TEKNİK_GMY=0,
    İK_DAN_SORUMLU_GMY=0,
    İNSAN_KAYNAKLARI_MÜDÜRÜ=0,
    SATINALMA_MÜDÜR_YRD=0,
    MUHASEBE_MÜDÜR_YRD=0,
    İLETİŞİM_MEMURU=0,
    PAZARLAMA_MEMURU=0,
    BİLGİ_TEKNOLOJİLERİ_MÜDÜRÜ=0,
    İLETİŞİM_ŞEFİ=0,
    PAZARLAMA_MÜDÜR_YRD=0,
    FİNANS_ŞEFİ=0,
    İDARİ_MALİ_İŞLERDEN_SORUMLU_GMY=0,
    SATINALMA_MÜDÜRÜ=0,
    İLETİŞİM_MÜDÜRÜ=0,
    SATINALMA_ŞEFİ=0,
    MUHASEBE_MÜDÜRÜ=0,
    BİLGİ_TEKNOLOJİLERİ_MÜDÜR_YRD=0,
    SATIŞ_MÜDÜRÜ=0,
    PLANLAMA_MEMURU=0,
    PLANLAMA_ŞEFİ=0,
    PLANLAMA_MÜDÜR_YRD=0,
    FİNANS_MÜDÜR_YRD=0,
    SATIŞ_MEMURU=0,
    İNSAN_KAYNAKLARI_ŞEFİ=0,
    SATINALMA_MEMURU=0,
    PLANLAMA_MÜDÜRÜ=0,
    BİLGİ_TEKNOLOJİLERİ_ŞEFİ=0,
    SATIŞ_MÜDÜR_YRD=0,
    SATIŞ_ŞEFİ=0,
    FİNANS_MÜDÜRÜ=0,
    MUHASEBE_MEMURU=0,
    MUHASEBE_ŞEFİ=0,
    PAZARLAMA_ŞEFİ=0,
    İNSAN_KAYNAKLARI_MÜDÜR_YRD=0,
    FİNANS_MEMURU=0

    if gender1=='MALE':
        MALE=1
    else:
        FEMALE=1
    genders=[FEMALE,MALE]
    

    depart=[BİLGİ_TEKNOLOJİLERİ,FİNANS,MUHASEBE,PAZARLAMA,PLANLAMA,SATINALMA,
    SATIŞ,YÖNETİM,İLETİŞİM,İNSAN_KAYNAKLARI]

    depart1=["BİLGİ TEKNOLOJİLERİ","FİNANS","MUHASEBE","PAZARLAMA","PLANLAMA","SATINALMA",
    "SATIŞ","YÖNETİM","İLETİŞİM","İNSAN KAYNAKLARI"]
    for a in depart1:
            if department1==a:
                index1=depart1.index(a)
                depart[index1]=1
    
                
            else:
                index1=depart1.index(a)
                depart[index1]=0
                

                continue
    posıt=[BİLGİ_TEKNOLOJİLERİ_MEMURU,BİLGİ_TEKNOLOJİLERİ_MÜDÜR_YRD,BİLGİ_TEKNOLOJİLERİ_MÜDÜRÜ,
        BİLGİ_TEKNOLOJİLERİ_ŞEFİ,FİNANS_MEMURU,FİNANS_MÜDÜR_YRD,
        FİNANS_MÜDÜRÜ,FİNANS_ŞEFİ,GENEL_MÜDÜR,
        MUHASEBE_MEMURU,MUHASEBE_MÜDÜR_YRD,MUHASEBE_MÜDÜRÜ,MUHASEBE_ŞEFİ,
        PAZARLAMA_MEMURU,PAZARLAMA_MÜDÜR_YRD,PAZARLAMA_MÜDÜRÜ,PAZARLAMA_ŞEFİ,
        PLANLAMA_MEMURU,PLANLAMA_MÜDÜR_YRD,PLANLAMA_MÜDÜRÜ,PLANLAMA_ŞEFİ,
        SATINALMA_MEMURU,SATINALMA_MÜDÜR_YRD,SATINALMA_MÜDÜRÜ,SATINALMA_ŞEFİ,
        SATIŞ_MEMURU,SATIŞ_MÜDÜR_YRD,SATIŞ_MÜDÜRÜ,SATIŞ_ŞEFİ,TEKNİK_GMY,
        İDARİ_MALİ_İŞLERDEN_SORUMLU_GMY,İK_DAN_SORUMLU_GMY,İLETİŞİM_MEMURU,
        İLETİŞİM_MÜDÜR_YRD,İLETİŞİM_MÜDÜRÜ,İLETİŞİM_ŞEFİ,İNSAN_KAYNAKLARI_MEMURU,
        İNSAN_KAYNAKLARI_MÜDÜR_YRD,İNSAN_KAYNAKLARI_MÜDÜRÜ,İNSAN_KAYNAKLARI_ŞEFİ]
 
    posıt1=['BİLGİ TEKNOLOJİLERİ MEMURU','BİLGİ TEKNOLOJİLERİ MÜDÜR YRD.','BİLGİ TEKNOLOJİLERİ MÜDÜRÜ',
       'BİLGİ TEKNOLOJİLERİ ŞEFİ','FİNANS MEMURU','FİNANS MÜDÜR YRD.',
       'FİNANS MÜDÜRÜ','FİNANS ŞEFİ','GENEL MÜDÜR',
       'MUHASEBE MEMURU','MUHASEBE MÜDÜR YRD.','MUHASEBE MÜDÜRÜ','MUHASEBE ŞEFİ',
       'PAZARLAMA MEMURU','PAZARLAMA MÜDÜR YRD.','PAZARLAMA MÜDÜRÜ','PAZARLAMA ŞEFİ',
       'PLANLAMA MEMURU','PLANLAMA MÜDÜR YRD.','PLANLAMA MÜDÜRÜ','PLANLAMA ŞEFİ',
       'SATINALMA MEMURU','SATINALMA MÜDÜR YRD.','SATINALMA MÜDÜRÜ','SATINALMA ŞEFİ',
       'SATIŞ MEMURU','SATIŞ MÜDÜR YRD.','SATIŞ MÜDÜRÜ','SATIŞ ŞEFİ', 'TEKNİK GMY',
       'İDARİ MALİ İŞLERDEN SORUMLU GMY',"İK'DAN SORUMLU GMY",'İLETİŞİM MEMURU',
       'İLETİŞİM MÜDÜR YRD.','İLETİŞİM MÜDÜRÜ','İLETİŞİM ŞEFİ','İNSAN KAYNAKLARI MEMURU',
       'İNSAN KAYNAKLARI MÜDÜR YRD.','İNSAN KAYNAKLARI MÜDÜRÜ','İNSAN KAYNAKLARI ŞEFİ']
    for i in posıt1:
            if position1==i:
                index2=posıt1.index(i)
                posıt[index2]=1
            else:
                index2=posıt1.index(i)
                posıt[index2]=0
                

                continue
    A=[experience1+genders+depart+posıt]
    ui.PREDICTION.setText("{}".format(lr.predict(A)))
    
   

ui.PREDICT.clicked.connect(predict)

#DELETE SELECTED ROW FROM SQL SERVER
def delete():
    info=ui.TABLE.selectedItems()
    ad=info[0].text()
    soyad=info[1].text()
    dep=info[4].text()
   
    imlec.execute("DELETE FROM PERSON_INFO WHERE NAME='{}' and SURNAME='{}' and DEPARTMENT='{}'".format(ad,soyad,dep))
    db.commit()
    ui.TABLE.clear()
    imlec.execute("select NAME,SURNAME,GENDER,EXPERIENCE,DEPARTMENT,POSITION,SALARY from PERSON_INFO")
    msgBox = QMessageBox()
    for satırindex,satırveri in enumerate(imlec):
        for sutunındex,sutunveri in enumerate(satırveri):
            ui.TABLE.setItem(satırindex,sutunındex,QTableWidgetItem(str(sutunveri)))
    msgBox.setWindowTitle("SUCCESSFUL")
    msgBox.setText("THE RECORD IS DELETED")
    msgBox.exec_()
   
ui.DELETE.clicked.connect(delete)

#FIND DATA FROM SQL SERVER WITH GIVEN INPUT VALUES
def fınd():
    name2=ui.NAME.text()
    surname2=ui.SURNAME.text()
    gender2=ui.GENDER.currentText()
    experience2=ui.EXPERIENCE.text()
    department2=ui.DEPARTMENT.currentText()
    position2=ui.POSITION.currentText()
    salary2=ui.SALARY.text()
    ui.TABLE.clear()
    imlec.execute("select NAME,SURNAME,GENDER,EXPERIENCE,DEPARTMENT,POSITION,SALARY from PERSON_INFO \
        where (NAME='{}' and SURNAME='{}') or GENDER='{}' or EXPERIENCE='{}' or DEPARTMENT='{}' or POSITION='{}' or SALARY='{}'\
            ".format(name2,surname2,gender2,experience2,department2,position2,salary2))
    for satırindex,satırveri in enumerate(imlec):
        for sutunındex,sutunveri in enumerate(satırveri):
            ui.TABLE.setItem(satırindex,sutunındex,QTableWidgetItem(str(sutunveri)))

ui.FIND.clicked.connect(fınd)
sys.exit(app.exec_())
