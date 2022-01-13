FROM python:3.9

RUN apt-get update && apt-get install libatlas-base-dev -y

COPY ./server/requirements.txt /server/requirements.txt

RUN pip3 install --index-url=https://www.piwheels.org/simple --no-cache-dir -r /server/requirements.txt
RUN pip3 install -r /server/requirements_compile.txt

COPY ./server /server
COPY ./names_and_reps-nlp.pkl /server/names_and_reps-nlp.pkl
COPY ./names_and_reps-cbog.pkl /server/names_and_reps-cbog.pkl
COPY ./names_and_reps-nonlp.pkl /server/names_and_reps-nonlp.pkl
COPY ./fluff_data.csv /server/fluff_data.csv

CMD ["python3", "-m", "streamlit", "run", "/server/app.py", "--", "--nlp-rep-path", "/server/names_and_reps-nlp.pkl", "--cbog-rep-path", "/server/names_and_reps-cbog.pkl", "--nonlp-rep-path", "/server/names_and_reps-nonlp.pkl", "--fluff-data-path", "/server/fluff_data.csv"]
