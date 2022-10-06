FROM python:3.6

COPY . /seguranca

WORKDIR seguranca

EXPOSE 5000:5000

RUN pip install flask

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
