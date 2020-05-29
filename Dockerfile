FROM python:3.8.2
ADD . /code
WORKDIR /code
ARG ENV
RUN ./env.sh ${ENV}
#RUN pip install mysql-python
CMD ["python", "mysql-clickhouse-replication.py"]