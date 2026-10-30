from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()
import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_core.messages import HumanMessage
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
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print('session initialized')
            tools = await load_mcp_tools(session)

            agent = create_agent(llm, tools)
            result = await agent.ainvoke({'messages': [HumanMessage(content='What is 254 + 2 * 3?')]})
            print(result['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
