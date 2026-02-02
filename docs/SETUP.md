# OpenClaw / Moltbot Docker Setup

## Start
docker compose up -d --build

## Stop (clean)
docker compose down --remove-orphans

## Status
docker compose ps

## Logs
docker compose logs -f gateway
docker compose logs -f moltbot

## Health Checks
curl -i http://localhost:8080/
curl -i http://localhost:8080/echo/
curl -i http://localhost:8080/health/
curl -i http://localhost:8080/moltbot/health

## Nginx Routing
gateway/nginx/default.conf routes:
- /echo/    -> echo:5000
- /health/  -> health:5000
- /moltbot/ -> moltbot:8000

