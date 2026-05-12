from Demos.c_extension.setup import sources
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams,Distance,PointStruct
from sqlalchemy.orm import collections
from workflows.runtime.types import results


class VectorDB:
    def __init__(self,url="http://127.0.0.1:6333",collection="docs",dim=3072):
        self.client = QdrantClient(url=url,collection=collection,timeout=30)
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim,distance=Distance.COSINE)

            )

    def upsert(self,ids,vectors,payloads):
        points=[PointStruct(id=ids[i],vector=vectors[i],payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection,points=points)

    def search(self,query_vector,top_k,int=5):
        results=self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            with_payload=True,
            limit=top_k
        )

        context=[]
        sources=set()

        for r in results:
            payload=getattr(r,'payload',None)or {}
            text=payload.get('text',"")
            source=payload.get('source',"")
            if text:
                context.append(text)
                sources.append(source)


        return {"context":context, "source":list(sources)}
