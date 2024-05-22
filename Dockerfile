FROM python:3.8.12
ENV PYTHONUNBUFFERED=1
WORKDIR /Portal
COPY requirements.txt /Portal/
RUN pip install -r requirements.txt
COPY . /Portal/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
