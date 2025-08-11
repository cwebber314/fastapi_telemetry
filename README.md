# FastAPI and Telemetry

Example of instrumenting a FastAPI applicaiton

See notes [here](https://docs.honeycomb.io/send-data/python/opentelemetry-sdk/)

Example `setup_env.bat` for windows:
```
SET OTEL_SERVICE_NAME=demo
SET OTEL_TRACES_EXPORTER=otlp
SET OTEL_LOGS_EXPORTER=otlp
SET OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
SET OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io:443
SET OTEL_EXPORTER_OTLP_HEADERS=x-honeycomb-team={apikey}
SET OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
``` 