from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

from .config import settings

SYSTEM_PROMPT = """
You are a concise voice assistant. The user's input is transcribed speech from
Siri on a HomePod, and your reply will be spoken aloud. Follow these rules:

- Keep replies to 1-2 short sentences, or a brief enumerated list (max 5 items).
- Speak naturally. No markdown, no URLs, no code, no emoji.
- You have access to the user's business systems (Asana, etc.) via the
  Agent Engine MCP tools. Use them to answer questions and to perform actions
  like creating, updating, or completing tasks.
- Distinguish queries (read) from commands (mutate). For mutations, confirm the
  action you took in your reply (e.g. "Added 'Draft copy' to the Design section.").
- If a tool fails or information is missing, say so briefly instead of guessing.
""".strip()


def _build_agent_engine_server() -> MCPServerStreamableHTTP:
    headers: dict[str, str] = {}
    if settings.agent_engine_mcp_token:
        headers["Authorization"] = f"Bearer {settings.agent_engine_mcp_token}"
    return MCPServerStreamableHTTP(url=settings.agent_engine_mcp_url, headers=headers)


agent = Agent(
    settings.model,
    system_prompt=SYSTEM_PROMPT,
    toolsets=[_build_agent_engine_server()],
)


async def handle_message(query: str) -> str:
    async with agent:
        result = await agent.run(query)
    return result.output
