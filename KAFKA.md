### Kafka broker
analogous to kafka server
### Kafka Topic
analogous to sql tables
used to sen/receive messages
### Producer
process that sends data
### Consumer
process that recieves data
### Kafka partition
for distribution of data
subdivisions of topic
allows parallel reading/writing
every topic has at least 1
### Kafka offset
sequence number in each partition ..makes tracking easy
just like book page number
assigned by broker
message continues from where left due to offset
### Message key
decides which partition to send the message
attached with the msg
### Serialization
conversion to bytes (encoding of the message that is sent to topic)
### Consumer group
group of consumers
avoid load on a single consumer to gather info from diff partitions
each consumer in consumer group gather info from specific partition only
### Kafka cluster
group of kafka brokers
#### replication factor
number of copies of message 

in case of two or more brokers in a cluster the leader partition in one cluster is backup partition in other
if one broker is down the leader partition of it which is backup partition in other will become leader in the other broker
### Kafka zookeeper
manages synchronization and failure of brokers
externally used
### Kraft
internal version of zookeeper..modern tech
##### bootstrap server tells the kafka client where to connect first, it gives the info of all the brokers and partition in the cluster

### Kafka connect
connects kafka to external database
just make new config file containing details of databse
contains:
- **source connectors**: pulls data
- **sink connectors**: sends data
### Kafka streams
helps in transforming and modifications on data sent by producer

./bin/kafka-topics.sh --create --topic FRAUD-TOPIC --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
