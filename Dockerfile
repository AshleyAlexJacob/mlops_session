FROM python:3.10.13 as build
WORKDIR /app

# copy files
COPY ./mlruns/ ./mlruns/
COPY ./models.py ./models.py
COPY ./predict.py ./predict.py
COPY ./requirements.txt ./requirements.txt

ENV VIRTUAL_ENV=/home/packages/.venv
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 777 /install.sh && /install.sh && rm /install.sh
RUN /root/.cargo/bin/uv venv /home/packages/.venv

RUN /root/.cargo/bin/uv pip install --no-cache --system  -r requirements.txt



