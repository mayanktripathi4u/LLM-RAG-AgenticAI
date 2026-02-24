from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def get_homepage():
    count = 1
    while count <= 5:
        print(f"Processing count: {count}")
        time.sleep(1)  # Simulate a time-consuming task
        count += 1
    return {"status": "ok", "message": "Hello, FastAPI with OpenTelemetry!"}