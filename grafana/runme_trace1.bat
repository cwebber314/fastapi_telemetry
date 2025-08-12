SET OTEL_SERVICE_NAME=trace1
opentelemetry-instrument --traces_exporter console,otlp python trace1.py