# FastAPI Telemetry

Examples of adding telemetry data to a FastAPI server.

## Honeycomb.io

Pros:
- Easy to setup
- default views are great
- Manual instrumentation makes sense.
  - This is actually handled by open telemetry, but the honeycomb are great at explaining it
- Queries are pretty amazing - LLM was really helpful for a noob 

Cons:
- I couldn't get auto instrumentation to work - probably more of an open telemetry config issue.
- Probably have to lean a lot about OpenTelemetry to extend

## Pydantic Logfire

This was amazing - probably python centric but there looks to be APIs for other languages too.

Pros:
- Traces Works out of the box with FastAPI
- SQLAlchemy adapter is amazing

Cons:
- Can only sign in with public github/google identity unless you do something expensive

Questions:
- Unclear how hard customization will be.
- It's unclear how logs work - I just played with traces.
- Not sure how hard stats are going to be - looks like I get to write SQL for most analysis

## Grafana

Completely overwhelming. Setup was cumbersone - due in large part to windows being stupid. Docs are 
some really complex example, but I just needed a hello world.

Pros:
- Everyone uses Grafana
- You can do anything with Grafana

Cons:
- The Grafana ecosystem is overwhelming
- Default views for traces and logs are underwhelming