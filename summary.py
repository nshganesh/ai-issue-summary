# prerequisites
# Create a slack integration

# Create channels with issues in title (Ex: crewai-issues, composio-issues). This is where user's issues are reported.
# Create a channel called `today-summary-bot`. This is where the final message would be posted.

# This ai agent will fetch the issues reported in the channels. Combine them based on the priority.
# Posts the final summary in a `today-summary-bot` channel.
# We can analyse the sentiment for that day based on the user queries.
# Same sentiment parametr will be posted in the channel

# composio-cli add slack

from autogen import AssistantAgent, UserProxyAgent
from composio_autogen import App, Action, ComposioToolset


llm_config = {
    "config_list": [
        {
            "model": "gpt-3.5-turbo",
            "api_key": '***OPEN_API_KEY***',
        }
    ]
}

super_agent = AssistantAgent(
    "chatbot",
    system_message="""You are a super intelligent personal assistant.
    You have been given a set of tools that you are supposed to choose from.
    You decide the right tool and execute it to achieve your task.
    Reply TERMINATE when the task is done or when user's content is empty""",
    llm_config=llm_config,
)

user_proxy = UserProxyAgent(
    "user_proxy",
    is_termination_msg=lambda x: x.get("content", "")
    and "TERMINATE" in x.get("content", ""),
    human_input_mode="NEVER",  # Don't take input from User
    code_execution_config={"use_docker": False},
)

composio_tools = ComposioToolset()

composio_tools.register_tools(
    tools=[App.SLACK], caller=super_agent, executor=user_proxy
)

task = """Fetch all the messages from channels which includes `issues` in title for that day.
Group the messages based on the priority.
Ones with bug, error or security vulnerability will be of highest priority (add a nice icon).
Feature requests, documentation are medium priority (add a nice icon).
Unclear requirements are lowest priority (add a nice icon).
Summarize the messages with highest priority to lowest priority order.
Post the summary in the `today-summary-bot` channel with title having `Today's Issues Summary`"""

response = user_proxy.initiate_chat(super_agent, message=task)

print(response.chat_history)


nps_task = """Fetch the message from `today-summary-bot` channel for today.
  This lists the issues faced by the user, their requirements from composio.
  They are ordered from highest priority to lowest priority.
  Go through the content and understand the user's sentiments.
  Rate them on a scale of 100 to determine the today's NPS.
  Post the rating in `today-summary-bot` channel with title `Today's NPS: ` (add a nice icon) 
"""

response = user_proxy.initiate_chat(super_agent, message=nps_task)

print(response.chat_history)
