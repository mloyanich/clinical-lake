FROM openjdk:11-jre-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Spark
ENV SPARK_VERSION=3.3.2
RUN wget -q "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz" \
    && tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop3.tgz" -C /opt \
    && rm "spark-${SPARK_VERSION}-bin-hadoop3.tgz"
ENV SPARK_HOME /opt/spark-${SPARK_VERSION}-bin-hadoop3
ENV PATH $PATH:$SPARK_HOME/bin

# Install Iceberg and other dependencies
RUN curl -L "https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.4.2/iceberg-spark-runtime-3.3_2.12-1.4.2.jar" -o /opt/spark/jars/iceberg-spark-runtime-3.3_2.12-1.4.2.jar

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pyspark==3.3.2 pandas

WORKDIR /workspace
