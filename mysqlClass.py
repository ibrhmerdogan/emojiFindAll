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
        "CREATE TABLE emoji (id INT AUTO_INCREMENT PRIMARY KEY, İnsID VARCHAR(255), Emoji VARCHAR(255), Adet VARCHAR(255))")
    print("tablo oluşturuldu")
def _AddData(İnsID,Emoji,Adet):
    mycursor = mydb.cursor()
    sql = "INSERT INTO emoji (İnsID,Emoji,Adet) VALUES (%s, %s, %s)"
    val = (İnsID, Emoji, Adet)
    mycursor.execute(sql, val)
    mydb.commit()

def _SelectData():
    mycursor = mydb.cursor()
    mycursor.execute("select Aciklama, id from inst.instaanaliz ")
    myresult = mycursor.fetchall()
    return  myresult

