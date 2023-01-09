#!/bin/bash

# Comment out the line starting with cluster.id in file /home/kafka/logs/meta.properties
sed -i '/cluster.id/ s/^#*/#/' /home/kafka/logs/meta.properties

# Start the Kafka service using systemctl
systemctl start kafka

# Delete the outdated partition
/home/kafka/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic net-hw2
