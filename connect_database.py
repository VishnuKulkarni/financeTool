from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': 'secure-connect-codebytes.zip'
}
auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
#session.execute("DROP TABLE Bisi.user")
#session.execute("DROP TABLE Bisi.bisi")

#session.execute(" CREATE KEYSPACE Bisi WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }")

query="CREATE TABLE Bisi.user ( id UUID, personName text, personGender text, personAddress text, personPhone text, personAadhar text, personDob text, personBisiEncashStatus boolean, personBisiEncashedValue text, personBisiNameWhichIsEncashed text, personAssociatedBisi text, properties map<text,text>,   PRIMARY KEY (id, personName, personAssociatedBisi) )"
#session.execute(query)

#session.execute("INSERT INTO Bisi.user (id, personName, personGender, personAddress, personPhone, personAadhar, personDob, personBisiEncashStatus, personBisiEncashedValue , personBisiNameWhichIsEncashed, personAssociatedBisi) VALUES (4c76a938-3bff-4f9a-9084-8b9248568784,'Vishnu2','Male', '123 street', '7327998030', '2345677', '13-08-1988', true, '1,00,000', 'bisi1', 'bisi1') ")

#session.execute("CREATE TYPE Bisi.bisi_history (bisiEncashStatus text, bisiEncashPerson text, bisiEncashValue text, bisiComission text)")
query2="CREATE TABLE Bisi.bisi ( id UUID, bisiName text, bisiTotalMonths int, bisiTotalPpl int, bisiStartDate text, bisiEndDate text, bisiSumAssured text, bisiStatus text, bisiComission text, bisiPrevMonthComission text, properties map<text,text>, bisiPplList list<text>, bisiCommisionHistoryData map<text,FROZEN <bisi_history>>,  PRIMARY KEY (id, bisiName) )"
#result = session.execute(query2)
#session.execute("INSERT INTO Bisi.bisi (id, bisiName, bisiTotalMonths, bisiTotalPpl, bisiStartDate, bisiEndDate, bisiSumAssured, bisiStatus, bisiComission, bisiPrevMonthComission, bisiPplList, bisiCommisionHistoryData) VALUES(6b6962dd-3f90-4c93-8f61-eabfa4a803e2,'bisi1',6,6,'01/14/2023','07/15/2023','1,00,000','not encashed','5,000','5,000',['Vishnu','Vishnu2'], {'01/14/2023-02/14/2023':{bisiEncashStatus :'encashed', bisiEncashPerson :'Vishnu', bisiEncashValue :'90,000', bisiComission :'5,000'}})")
#print (result)

row = session.execute("select release_version from system.local").one()
result_set = session.execute("SELECT * FROM system_schema.keyspaces")
#for row in result_set:
    #print(row)
session.execute("USE bisi")
result_set2 = session.execute("SELECT * FROM Bisi.bisi")
print("final result")
for row2 in result_set2:
    print("in for")
    print(row2)

result_set3 = session.execute("SELECT * FROM Bisi.user WHERE personAssociatedBisi='bisi1' ALLOW FILTERING")

for row3 in result_set3:
    print("in for")
    print(row3)
if row:
  print(row[0])
else:
  print("An error occurred.")
# Clean up the session and cluster objects 
session.shutdown()
cluster.shutdown()