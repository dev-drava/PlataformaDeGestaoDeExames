import mysql.connector

def start_connection():

    return mysql.connector.connect(
      host="gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com",
      user="31KQqAzuXFDyWLb.root",
      password="2e5GKWvRCDEsRtJ0",
      database="gestao_exames"
    )
