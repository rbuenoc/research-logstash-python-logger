FROM logstash:7.9.3

ADD logstash.yml /usr/share/logstash/config/logstash.yml
ADD tcp-s3.conf /usr/share/logstash/pipeline/tcp-s3.conf

EXPOSE 5000
