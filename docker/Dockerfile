FROM python:3.9

RUN apt-get update && apt-get install libatlas-base-dev -y

RUN pip3 install --index-url=https://www.piwheels.org/simple --no-cache-dir -r /server/requirements.txt;

COPY ./server /server
COPY ./names_and_reps.pkl /server/names_and_reps.pkl

CMD ["python3", "-m", "streamlit", "run", "/server/app.py", "--", "--rep-path", "/server/names_and_reps.pkl"]
