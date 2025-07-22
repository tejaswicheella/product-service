# 1. Use a lean Python base
FROM python:3.10-slim

# 2. Set workdir & copy deps
WORKDIR /app
COPY requirements.txt .

# 3. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy code
#COPY app/ ./app
COPY app/ ./app/

# 5. Expose port & define startup
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#Use below command to insert data into mongodb
#CMD ["python", "insertDataToMongo.py"]