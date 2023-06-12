from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class CassandraManager:
    def __init__(self, secure_connect_bundle_path, username, password, keyspace):
        self.cluster = None
        self.session = None
        self.secure_connect_bundle_path = secure_connect_bundle_path
        self.username = username
        self.password = password
        self.keyspace = keyspace

    def connect(self):
        cloud_config = {
            'secure_connect_bundle': self.secure_connect_bundle_path
        }
        auth_provider = PlainTextAuthProvider(
            username=self.username,
            password=self.password
        )
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect()
        self.session.set_keyspace(self.keyspace)

    def close(self):
        self.session.shutdown()
        self.cluster.shutdown()

# Create an instance of CassandraManager with connection details
cassandra_manager = CassandraManager(
    secure_connect_bundle_path='secure-connect-codebytes.zip',
    username='zcZcWDthSpEiyCQRiWDBpGom',
    password='34PgNiXLTu.zaiKhdstHPNZwe8gZPSJshR+BB-at61hab.mxN2MJLh_0tFwdfNRkNxgGHr,hTv8w4+c_Ig_S-ZFprsLRhfgAQjEqkSn9zqezUPo-+qphgDnj9ifkY5gz',
    keyspace='bisi'
)



# ... Use the cassandra_manager.session throughout your app ...


