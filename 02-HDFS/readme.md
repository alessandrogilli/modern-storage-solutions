# HDFS
## Environment configuration
- Install [Docker and Docker compose](https://docs.docker.com/engine/install/)
- Inside this directory, open a terminal and run:
    
    ```docker compose up -d```

## HDFS Web UI
connect to http://localhost:50070

## HDFS Command Line Interface
Enter the namenode container:
```bash
docker exec -it namenode bash
```
Check the content of HDFS
```bash
hdfs dfs -ls /
```
Create a directory
```bash
hdfs dfs -mkdir -p /user/root
```
Prepare a big file to store in HDFS
```bash
cd /hadoop/staging/
```
```bash
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 80 | head -c 1G  > bigfile
```
Store the file in HDFS with default parameters
```bash
hdfs dfs -put bigfile /user/root/bigfile
```
Remove the file from HDFS
```bash
hdfs dfs -rm /user/root/bigfile
```
Store the file in HDFS with replication factor = 1
```bash
hdfs dfs -D dfs.replication=1 -put bigfile /user/root/bigfile
```
Remove the file from HDFS
```bash
hdfs dfs -rm /user/root/bigfile
```

## Credits
- https://towardsdatascience.com/hdfs-simple-docker-installation-guide-for-data-science-workflow-b3ca764fc94b

- [Complete list of HDFS commands](https://sparkbyexamples.com/apache-hadoop/hadoop-hdfs-dfs-commands-and-starting-hdfs-dfs-services/)