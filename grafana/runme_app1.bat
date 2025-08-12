SET OTEL_SERVICE_NAME=app1
opentelemetry-instrument --traces_exporter console,otlp flask run -p 8080