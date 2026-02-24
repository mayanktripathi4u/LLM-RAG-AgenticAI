1. Create a file `app.py`
```python
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
```

2. Make sure to have Docker installed and running on the local machine.
3. Run Jaeger in Docker
```sh
docker run -d --name jaeger -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 -e COLLECTOR_OLTP_ENABLED=true \
-p 6831:6831/udp -p 6832:6832/udp \
-p 5778:5778 -p 16686:16686 \
-p 4317:4317 \
-p 4318:4318 \
-p 14250:14250 \
-p 14268:14268 \
-p 14260:14260 \
-p 9411:9411 \
jaegertracking/all-in-one:1.38
```
4. Start Jaeger in Docker Container. Now should be able to browse the Jaeger web page (home page).
5. Requirements or Libraries required. For this new record 
```txt
fastapi==0.85.0
uvicorn==0.18.3
pydantic==1.10.2
opentelemetry-distro==0.33b0
opentelemetry-instrumentation-fastapi==0.33b0
opentelemetry-exporter-otlp-proto-grpc==1.12.0
```
6. Install Dependencies
```sh
pip install -r requirements.txt
```
7. Run with OpenTelemetry
```sh
opentelemetry-instrument --service_name my_otl_service.api uvicorn app:app
```
8. Hit the URL may be using curl
```sh
curl http://localhost:8080
```
9. Refresh the Jaeger Page, and now should be able to see new Service "my_otl_service.api" as we set above.
10. Now modify the code or better create a new copy as `app_enriched.py`
```python
from fastapi import FastAPI
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

# Initialize OpenTelemetry Tracer
provider = TracerProvider()
# Set the global tracer provider
trace.set_tracer_provider(provider)
# Create a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)


app = FastAPI()

@app.get("/")
def get_homepage():
    count = 1
    while count <= 5:
        with tracer.start_as_current_span(f"processing_count: {count}") as span:
            print(f"Processing count: {count}")
            time.sleep(1)  # Simulate a time-consuming task
            count += 1
    return {"status": "ok", "message": "Hello, FastAPI with OpenTelemetry!"}
```
Re-Run with new file
```sh
opentelemetry-instrument --service_name my_otl_service.api uvicorn app_enriched:app
```
Followed with accessing URL
```sh
curl http://localhost:8080
```
Now should see more details.
