from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel

from .agent import handle_message
from .config import settings

app = FastAPI(title="My Assistant")


class MessageRequest(BaseModel):
    query: str


class MessageResponse(BaseModel):
    reply: str


async def require_auth(authorization: str | None = Header(default=None)) -> None:
    expected = f"Bearer {settings.app_bearer_token}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="unauthorized")


@app.get("/health")
async def health() -> dict[str, bool]:
    return {"ok": True}


@app.post("/message", response_model=MessageResponse, dependencies=[Depends(require_auth)])
async def message(req: MessageRequest) -> MessageResponse:
    reply = await handle_message(req.query)
    return MessageResponse(reply=reply)
