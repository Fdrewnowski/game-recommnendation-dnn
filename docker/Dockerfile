FROM python:3.9-slim

COPY ./server /server
COPY ./names_and_reps.pkl /server/names_and_reps.pkl

RUN apt install 
RUN pip3 install -r /server/requirements.txt

CMD ["python3", "-m", "streamlit", "run", "/server/app.py", "--", "--rep-path", "/server/names_and_reps.pkl"]
