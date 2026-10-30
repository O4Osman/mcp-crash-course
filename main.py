from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

load_dotenv()
import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openrouter import ChatOpenRouter
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

llm = ChatOpenRouter(model='nvidia/nemotron-3.5-super-vl:free', temperature=0)

stdio_server_params = StdioServerParameters(
    command='python',
    args=['C:/Users/osman/PycharmProjects/mcp-crash-course/servers/math_server.py']
)


async def main():
    print("Hello world")


if __name__ == "__main__":
    asyncio.run(main())
