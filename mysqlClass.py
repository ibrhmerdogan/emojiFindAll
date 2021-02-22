import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="inst"
)
mycursor = mydb.cursor()

def _CreatorTable():
    mycursor.execute(
        "CREATE TABLE instaAnaliz (id INT AUTO_INCREMENT PRIMARY KEY, Tarih VARCHAR(255), BegeniSay VARCHAR(255)"
        ",Aciklama VARCHAR(255))")
    print("tablo oluşturuldu")
def _AddData(Tarih,BegeniSay,Aciklama):
    mycursor = mydb.cursor()
    sql = "INSERT INTO instaAnaliz (Tarih,BegeniSay,Aciklama) VALUES (%s, %s, %s)"
    val = ( Tarih, BegeniSay, Aciklama)
    mycursor.execute(sql, val)
    mydb.commit()

def _SelectData():
    mycursor = mydb.cursor()
    mycursor.execute("select Aciklama  from inst.instaanaliz ")
    myresult = mycursor.fetchall()
    return  myresult

#aciklama  = _SelectData()
#for i in aciklama:
#    print(i)