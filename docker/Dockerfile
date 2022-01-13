FROM python:3.9-slim

COPY ./server /server
COPY ./names_and_reps.pkl /server/names_and_reps.pkl

RUN pip install -r /server/requirements.txt

CMD ["python", "-m", "streamlit", "run", "/server/app.py", "--", "--rep-path", "/server/names_and_reps.pkl"]
