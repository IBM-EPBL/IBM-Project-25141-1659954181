import ibm_db
def connection():
    try:
        #jesima db2 credential
        conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;\
            PORT=32716;PROTOCOL=TCPIP;UID=rmy92863;PWD=DDoUqjA0drfzoKCm;SECURITY=SSL;SSLServiceCertificate=DigiCertGlobalRootCA.crt", "", "")
        print("CONNECTED TO DATABASE")
    except:
        print(ibm_db.conn_errormsg())
        print("CONNECTION FAILED")

    print("select * from bludb;")