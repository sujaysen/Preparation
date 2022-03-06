Replica Set Features:
---------------------
1. A cluster of N nodes
2. Any one node can be primary
3. All write operations go to primary
4. Automatic failover
5. Automatic recovery
6. Consensus election of primary

mongod --port "PORT" --dbpath "YOUR_DB_DATA_PATH" --replSet "REPLICA_SET_INSTANCE_NAME"
rs.add(HOST_NAME:PORT)


# Deployment
mongostat
mongotop

