import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openrouter import ChatOpenRouter
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenRouter(model='nvidia/nemotron-3.5-super-vl:free', temperature=0)


async def main():
    print('hello langchain mcp')


if __name__ == '__main__':
    asyncio.run(main())
