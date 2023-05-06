from cassandra.cluster import Cluster

class DBFunctions():
    # Set up the connection details for the Cassandra cluster
    cloud_config= {
        'secure_connect_bundle': 'secure_connect_bundle.zip'
    }

    #list of functions
    def getAllUsers():
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

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

    def getAllBisis():
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT * FROM Bisi.bisi"
        result_set = session.execute(query)

        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set

    #confirm what needs to be returned here:::
    def getAllUsersByBisiId(id):
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT users FROM Bisi.bisi WHERE id=?"
        # Prepare the statement
        prepared = session.prepare(query)

        result1 = session.execute(prepared,id)

        values = [row[0] for row in result1]
        query2 = "SELECT users FROM Bisi.user WHERE id IN ?"
        # Prepare the statement
        prepared = session.prepare(query2)
        param2 = (values,)

        result_set = session.execute(prepared,[param2])


        # Process the result set...
        for row in result_set:
            print(row)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()

        return result_set

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
    

    def getAllBisiByUserId(id):
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query = "SELECT bisi FROM Bisi.user WHERE id=? ALLOW FILTERING"
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
        return response

    def addNewUserToBisi(userDetails):
        return response

    def updateUser(userDetails):
        return response

    def addNewBisi(bisiDetails):
        return response

    def updateBisi(bisiDetails):
        return response

    def createTables():
        cluster = Cluster(cloud=cloud_config)

        # Connect to the Cassandra cluster and create a session
        session = cluster.connect()

        # Execute a simple CQL query
        query="CREATE TABLE Bisi.user ( id UUID, lastname text, firstname text,gender text, address text, phone text, aadharnumber text, properties map<text,text>, bisi set<text>,  PRIMARY KEY (id, phone) )"
        session.execute(query)

        query="CREATE TABLE Bisi.bisi ( id UUID, name text, duration text,start text, end text, monthlypremium text, encashstatus text, properties map<text,text>, users set<text>,  PRIMARY KEY (name, id) )"
        session.execute(query)

        # Clean up the session and cluster objects
        session.shutdown()
        cluster.shutdown()