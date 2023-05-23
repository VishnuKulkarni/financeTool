from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

class DBFunctions():
    # Set up the connection details for the Cassandra cluster
    cloud_config= {
        'secure_connect_bundle': 'secure-connect-codebytes.zip'
    }
    auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

    # Connect to the Cassandra cluster and create a session
    #session = cluster.connect()

    #list of functions
    def getAllUsers():
    
        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.user"
        result_set = session.execute(query)

        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set

    def getAllBisisList():
        print("In get Bisis")
        # Set up the connection details for the Cassandra cluster
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-codebytes.zip'
        }
        auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()
        cluster = Cluster(cloud=cloud_config)

        # Execute a simple CQL query
        query = "SELECT bisiName FROM Bisi.bisi"
        result_set = session.execute(query)
        final_result1 = [i[0] for i in result_set]
        print (final_result1)
        
        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()
        return final_result1

    #confirm what needs to be returned here:::
    def getAllUsersListByBisiName(bisiName):
        print("In get usrs")

        # Set up the connection details for the Cassandra cluster
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-codebytes.zip'
        }
        auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()
        cluster = Cluster(cloud=cloud_config)

        # Execute a simple CQL query
        query = "SELECT bisiPplList FROM Bisi.bisi WHERE bisiName=? ALLOW FILTERING"
        # Prepare the statement
        prepared = session.prepare(query)

        result1 = session.execute(prepared,(bisiName,))
        python_list = []
        for row in result1:
            cassandra_list = row.bisippllist
            python_list.extend(cassandra_list)        
       
        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return python_list

    def getBisiDetailsByBisiId(id):
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.bisi WHERE id=?"
        # Prepare the statement
        prepared = session.prepare(query)

        result_set = session.execute(prepared,id)

        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set
    
    def getBisiHistory(bisiName):
        print("in history")
        # Set up the connection details for the Cassandra cluster
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-codebytes.zip'
        }
        auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()
        cluster = Cluster(cloud=cloud_config)

        # Execute a simple CQL query
        query = "SELECT bisiCommisionHistoryData FROM Bisi.bisi WHERE bisiName=? ALLOW FILTERING"
        # Prepare the statement
        prepared = session.prepare(query)

        result_set = session.execute(prepared,(bisiName,))
        print("executed")
        structured_dict = {}

        # Extract and store the map values
        for row in result_set:
            bisiCommisionHistoryData = row.bisicommisionhistorydata
            print(bisiCommisionHistoryData)
            print("raw")

            for key, value in bisiCommisionHistoryData.items():
                structured_dict[key] = value

        print(structured_dict)
        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return structured_dict

    def getUserDetailsByUserNameAndBisiName(personName, bisiName):
        # Set up the connection details for the Cassandra cluster
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-codebytes.zip'
        }
        auth_provider = PlainTextAuthProvider('zcZcWDthSpEiyCQRiWDBpGom', '34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()
        cluster = Cluster(cloud=cloud_config)
        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.user WHERE personName=? AND personAssociatedBisi=? ALLOW FILTERING"
        # Prepare the statement
        prepared = session.prepare(query)

        result_set = session.execute(prepared,(personName, bisiName))

        result_dict = []
        for row in result_set:
            row_dict = { 
                'personName':personName,
                'personGender': row.persongender,
                'personAddress': row.personaddress,
                'personPhone': row.personphone,
                'personAadhar': row.personaadhar,
                'personDob': row.persondob,
                'personBisiEncashStatus': row.personbisiencashstatus,
                'personBisiEncashedValue': row.personbisiencashedvalue,
                'personBisiNameWhichIsEncashed': row.personbisinamewhichisencashed,
                'personAssociatedBisi': bisiName,
            }
            result_dict.append(row_dict)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        print(result_dict)

        return result_dict

    def getUserDetailsByUserPhone(phone):
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.user WHERE phone=? ALLOW FILTERING"
        # Prepare the statement
        prepared = session.prepare(query)

        result_set = session.execute(prepared,id)

        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set

    def getUserDetailsByUserGovtId(govtId):
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.user WHERE aadharnumber=? ALLOW FILTERING"
        # Prepare the statement
        prepared = session.prepare(query)

        result_set = session.execute(prepared,id)

        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set

    def addNewUser(userDetails):
        # Prepare the INSERT statement
        insert_statement = session.prepare("INSERT INTO your_table (column1, column2, column3) VALUES (?, ?, ?)")

        # Execute the INSERT statement with values from the dictionary
        session.execute(insert_statement, tuple(data_dict.values()))

        return response

    def addNewUserToBisi(userDetails):

        return response

    def updateUser(userDetails):
        return response

    def addNewBisi(bisiDetails):

        return response

    def updateBisi(bisiDetails):
        return response

    def main():
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query="CREATE TABLE Bisi.user ( id UUID, lastname text, firstname text,gender text, address text, phone text, aadharnumber text, properties map<text,text>, bisi set<text>,  PRIMARY KEY (id, phone) )"
        #session.execute(query)

        query="CREATE TABLE Bisi.bisi ( id UUID, name text, duration text,start text, end text, monthlypremium text, encashstatus text, properties map<text,text>, users set<text>,  PRIMARY KEY (name, id) )"
        #session.execute(query)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()


# extra commented code for future use
# query2 = "SELECT firstname, lastname FROM Bisi.user WHERE id IN ?"
'''        prepared = session.prepare(query2)
        param2 = (values,)

        result_set = session.execute(prepared,[param2])
        #values = [row[0] for row in result1]


        # Process the result set...
        for row in result_set:
            print(row)


        json_objects = []
        for row in result_set:
            json_string = row[0]
            json_object = json.loads(json_string)
            json_objects.append(json_object)

        # Print the JSON objects
        #for json_obj in json_objects:
            #print(json_obj)
'''