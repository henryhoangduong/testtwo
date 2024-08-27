#!/bin/sh
# Start the Uvicorn server
exec uvicorn main:app --host 0.0.0.0 --reload --port ${PORT:-8080}