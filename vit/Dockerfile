FROM python:3.9

WORKDIR /code

RUN pip install \
    torch==1.12.0+cpu \
    torchvision==0.13.0+cpu \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    && rm -rf /root/.cache/pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server_vit.py ./model.script.pt /code/

CMD ["gunicorn", "server_vit:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8081"]