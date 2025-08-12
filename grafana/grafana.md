# Grafana

When you add a OTLP data source Grafana give you the environment setup env. If you are using windows 
make sure you escape the `%20` in the headers.
```
SET OTEL_RESOURCE_ATTRIBUTES="service.name=my-app,service.namespace=my-application-group,deployment.environment=production" 
SET OTEL_EXPORTER_OTLP_ENDPOINT="https://otlp-gateway-prod-us-east-2.grafana.net/otlp" 
SET OTEL_EXPORTER_OTLP_HEADERS="Authorization=Basic%%20<api-key>"
SET OTEL_EXPORTER_OTLP_PROTOCOL="http/protobuf" 
```

Links:
- https://grafana.com/docs/opentelemetry/instrument/python/
- https://github.com/grafana/docker-otel-lgtm/?tab=readme-ov-file#run-example-apps-in-different-languages