FROM zironycho/pytorch:1120-cpu-py38

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./server_gpt.py ./model.script.pt /code/

CMD ["gunicorn", "server_gpt:app",  "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]