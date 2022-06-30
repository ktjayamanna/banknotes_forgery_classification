FROM python:3.8.13-slim

RUN python -m pip install \
        parse \
        realpython-reader
COPY . /usr/app/
EXPOSE 8000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python swagger.py
