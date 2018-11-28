FROM python:2
MAINTAINER Brandon Gulla "gulla_brandon@bah.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["wsgi.py"]
