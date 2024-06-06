FROM python:3.10
COPY app.py .
COPY model.pkl .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5500
ENTRYPOINT [ "uvicorn","app:app","--port","5500","--host","0.0.0.0" ] 