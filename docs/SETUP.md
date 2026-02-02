# OpenClaw Setup (WSL + Docker)

## Start
docker compose up -d --build

## Stop
docker compose down --remove-orphans

## Status / Logs
docker compose ps
docker compose logs -f gateway
docker compose logs -f moltbot

## Endpoints (über nginx)
- http://localhost:8080/           -> Gateway OK
- http://localhost:8080/echo/      -> Echo Service
- http://localhost:8080/health/    -> Health Service
- http://localhost:8080/moltbot/   -> Moltbot API (reverse proxied)

## Secrets
- Secrets stehen in .env (nicht in Git)
- .env ist in .gitignore
