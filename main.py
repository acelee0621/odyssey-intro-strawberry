from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter
from contextlib import asynccontextmanager

from api.schema import schema
from mock_spotify_rest_api_client.client import Client


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with Client(
        base_url="https://spotify-demo-api-fe224840a08c.herokuapp.com/v1"
    ) as spotify_client:
        yield {"spotify_client": spotify_client}


app = FastAPI(lifespan=lifespan)


async def context_getter(request: Request):
    spotify_client = request.state.spotify_client
    return {"spotify_client": spotify_client}


graphql_router = GraphQLRouter(
    schema, path="/", graphql_ide="apollo-sandbox", context_getter=context_getter
)


app.include_router(graphql_router)


@app.get("/health")
async def health_check():
    return {"message": "Status OK"}
