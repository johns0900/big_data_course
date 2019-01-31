import sys
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if len(sys.argv) < 2:
  print "Please pass broker URL"
  sys.exit(0)

brokerURL = sys.argv[1]
sc = SparkContext("local[2]", "KafkaStreaming")
ssc = StreamingContext(sc, 5)
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["test"], {"metadata.broker.list": brokerURL, "zookeeper.connect": "18.236.141.245:2181"})
directKafkaStream.pprint()
ssc.start()
ssc.awaitTermination()
