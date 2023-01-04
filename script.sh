#!/bin/bash

# Comment out the line starting with cluster.id in file /home/kafka/logs/meta.properties
sed -i '/cluster.id/ s/^#*/#/' /home/kafka/logs/meta.properties

# Start the Kafka service using systemctl
systemctl start kafka
