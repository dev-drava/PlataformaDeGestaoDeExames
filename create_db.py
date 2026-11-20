import mysql.connector

mydb = mysql.connector.connect(
  host="gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com",
  user="31KQqAzuXFDyWLb.root",
  password="2e5GKWvRCDEsRtJ0"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS gestao_exames")
print("Database criada com sucesso")
