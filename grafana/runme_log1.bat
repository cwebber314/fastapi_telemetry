SET OTEL_SERVICE_NAME=log1
opentelemetry-instrument --traces_exporter console,otlp python log1.py