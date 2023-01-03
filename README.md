# multiples-docker-compose-same-network

Um simples estudo de como apps rodando em 2 `docker-compose.yml` diferentes
podem se comunicar utilizando a mesma rede.

## Subindo as APIs

### API A

```shell
docker-compose -f docker-compose-a.yml up -d
```

### API B

```shell
docker-compose -f docker-compose-b.yml up -d
```

## Testando a conexão entre elas

```shell
curl http://localhost:8001/other_secret
```

Através desse teste, a API A deve conseguir acessar e retornar o `SECRET_VALUE`
da API B, através de uma consulta via `GET` na mesma.
