FROM python_venv_pytest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "-q"]