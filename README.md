# Database BenchMarking

This Repo contains database benchmarking done on different database: Geomesa and Hbase.
More will be added in future

# Geomesa
GeoMesa is an open-source, distributed, spatio-temporal database built on a number of distributed cloud data storage systems, including Accumulo, HBase, Cassandra, and Kafka. Leveraging a highly parallelized indexing strategy, GeoMesa aims to provide as much of the spatial querying and data manipulation to Accumulo/Hbase as PostGIS does to Postgres.
GeoMesa does this by providing spatio-temporal data persistence on top of the Accumulo, HBase, and Cassandra distributed column-oriented databases for massive storage of point, line, and polygon data. It allows rapid access to this data via queries that take full advantage of geographical properties to specify distance and area. GeoMesa also provides support for near real time stream processing of spatio-temporal data by layering spatial semantics on top of the Apache Kafka messaging system.

# Hbase
Apache HBase is the Hadoop database, a distributed, scalable, big data store.

Use Apache HBase™ when you need random, realtime read/write access to your Big Data. This project's goal is the hosting of very large tables -- billions of rows X millions of columns -- atop clusters of commodity hardware. Apache HBase is an open-source, distributed, versioned, non-relational database modeled after Google's Bigtable: A Distributed Storage System for Structured Data by Chang et al. Just as Bigtable leverages the distributed data storage provided by the Google File System, Apache HBase provides Bigtable-like capabilities on top of Hadoop and HDFS. 

# Hbase in Python
Code : https://github.com/sandeep-iitr/Database-BenchMarking/blob/master/PythonCode/HBase/HBase_Test.ipynb
## Requirements
- Hbase Installed
- Start Hbase: ./start-hase.sh
    - This will require the Zookeeper running, or in standalone mode the conf file specifications
    - Start Zookeeper: bin/zkServer.sh start
    - Start Hadoop: sbin/start-dfs.sh
    - Stop Zookeeper: bin/zkServer.sh Stop
    - Stop Hadoop: sbin/stop-dfs.sh
- Start the Hbase thrift server
    - ./hbase thrift start
- Jupyter Environment
   - source activate py36

## Debugging
- Check Zookeeper is running:
  - bin/zkCli.sh -server 127.0.0.1:2181
  - Zookeeper single node setup guide: https://zookeeper.apache.org/doc/r3.3.3/zookeeperStarted.html
  - Clean Zookeeper Data: 
    - Stop Zookeeper, then clean the data directory.
    - This may be needed, if HDFS data is cleaned. If zookeeper is not cleaned then it results in inconsistency in Hbase metadata, which is stores in zookeeper.
- Check HDFS is running:
  - http://localhost:50070/
  - Hadoop single node cluster: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
  
- Check Hbase
   - http://localhost:16010/master-status
   - Make sure to set env variable in Hbase for separate zookeeper, if it run outside in a separate java process.
   - Hbase Distributed Cluster setup: http://hbase.apache.org/book.html#distributed
   
   

## Building
This is a apache Maven project, and can be compiled and tested using the mvn commands.
Requires, the Hbase database installed on local machine, at the default port running.

## Hadoop
### 1. Installation
[Single Node Cluster](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)
- Download the stable version of Hadoop
- Make changes in the etc/hadoop/core-site.xml and etc/hadoop/hdfs-site.xml.
- Specify Java path in etc/hadoop/hadoop-env.sh
- Format the File System bin/hdfs namenode -format
- Start NameNode Daemon and DataNode Daemon sbin/start-dfs.sh
- NameNode available at [http://localhost:50070/](http://localhost:50070/)
