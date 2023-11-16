# Proxycurl Client for Griptape

A [Proxycurl](https://nubela.co/proxycurl/) client for use as a Griptape tool.

## Usage

This tool requires a Proxycurl API key. When you have a key, simply import the ProxycurlClient into your Griptape project, configure it as needed, and provide it to a Griptape structure.

Here's an example that uses the ProxycurlClient to tell you about Griptape's LinkedIn profile:

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
