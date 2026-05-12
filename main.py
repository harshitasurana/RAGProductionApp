import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from dotenv import load_dotenv
import uuid
import os
import datetime

load_dotenv()

inngest_client= inngest.Inngest(
    app_id="rag-application",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer()
)

@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event="rag/inngest_pdf")
)

async def rag_ingest_pdf(ctx: inngest.Context):
    return {"hello": "world"}

app = FastAPI()


# // endpoint
inngest.fast_api.serve(app,inngest_client,[rag_ingest_pdf])
