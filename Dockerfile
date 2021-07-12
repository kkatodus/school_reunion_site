FROM python:3
ENV PYTHONBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=dousoukai_event.settings_dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
