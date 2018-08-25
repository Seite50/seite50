FROM python:3 as builder

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./manage test" ]

WORKDIR /usr/src/app
COPY --from=0 /usr/src/app .

CMD [ "sh", "start.sh" ]