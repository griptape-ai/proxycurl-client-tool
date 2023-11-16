# Proxycurl Client for Griptape

A Proxycurl client for use as a Griptape tool.

## Usage

Simply import the ProxycurlClient into your Griptape project:

```python
import os
from griptape.structures import Agent
from proxycurl_client import ProxycurlClient

# You've already set the OPENAI_API_KEY and PROXYCURL_API_KEY environment variables.

agent = Agent(
    tools=[
        ProxycurlClient(proxycurl_api_key=os.getenv("PROXYCURL_API_KEY"))
    ]
)

agent.run("Use LinkedIn to tell me about the company with id 'griptape-ai'.")
```
