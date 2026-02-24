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
