import os
from griptape.tools import TaskMemoryClient
from griptape.structures import Agent
from proxycurl_client import ProxycurlClient

# Create the ProxycurlClient tool
proxycurl_tool = ProxycurlClient(
    proxycurl_api_key=os.environ["PROXYCURL_API_KEY"]
)

# Set up an agent using the ProxycurlClient tool
agent = Agent(
    tools=[proxycurl_tool, TaskMemoryClient(off_prompt=False)]
)

# Task: Fetch information for the company Griptape.ai
agent.run("Tell me about the company profile Griptape.ai.")
