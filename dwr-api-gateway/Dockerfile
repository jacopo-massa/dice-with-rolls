FROM python:3.8-alpine

ADD ./ APIGateway
WORKDIR /APIGateway

RUN apk update && \
    apk upgrade && \
    apk add git

RUN pip3 install -r requirements.txt

RUN apk add --update redis
#&& \
#    rm -rf /var/cache/apk/* && \
#    mkdir /data && \
#    chown -R redis:redis /data && \
#    sed -i 's#logfile /var/log/redis/redis.log#logfile ""#i' /etc/redis.conf && \
#    sed -i 's#daemonize yes#daemonize no#i' /etc/redis.conf && \
#    sed -i 's#dir /var/lib/redis/#dir /data#i' /etc/redis.conf && \
#    echo -e "# placeholder for local options\n" > /etc/redis-local.conf && \
#    echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf


USER redis
# Expose the ports for redis
#EXPOSE 6379
EXPOSE 5000
#ENTRYPOINT ["redis-server"]

#CMD ["redis-server", "/usr/local/etc/redis.conf", "&"]

CMD ["celery", "-A", "APIGateway.tasks", "worker", "-B", "--loglevel=info", "&"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
