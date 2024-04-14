# ai-issue-summary
Uses composio to summarize slack issues for a day. Finds the NPS for that day.

# Prerequisites
  1. Create a slack integration. (https://docs.composio.dev/apps/slack)
  2. Create channels with issues in title (Ex: `crewai-issues`, `composio-issues`). This is where user's issues are reported.
  3. Create a channel called `today-summary-bot`. This is where the final summary would be posted.
  4. This ai agent will fetch the issues reported in the channels. Combine them based on the priority.
  5. Posts the summary in `today-summary-bot` channel.
  6. We will analyse the sentiment for that day based on the user queries.
  7. Same sentiment parameter will be posted in the channel.

# Setup
  1. pip install pyautogen composio_autogen
  2. composio-cli add slack (this is for the authentication)

# Demo
These are the channels on slack.
<img width="296" alt="Screenshot 2024-04-14 at 1 29 46 PM" src="https://github.com/nshganesh/ai-issue-summary/assets/14258513/00de3aa8-2e3c-4fdb-9046-5b7a78ad244b">
<img width="279" alt="Screenshot 2024-04-14 at 1 30 03 PM" src="https://github.com/nshganesh/ai-issue-summary/assets/14258513/98bfe32d-49ca-4ec5-ba91-c7f582cc4722">


Issues mentioned in the channels.
<img width="906" alt="Screenshot 2024-04-14 at 1 31 44 PM" src="https://github.com/nshganesh/ai-issue-summary/assets/14258513/c9cb8e3c-9c0c-4dde-97ac-acf86ce0a4e9">

<img width="893" alt="Screenshot 2024-04-14 at 1 32 04 PM" src="https://github.com/nshganesh/ai-issue-summary/assets/14258513/502f3220-9b21-40bc-886b-b3a03f9323c8">

On `summary.py` execution

<img width="914" alt="Screenshot 2024-04-14 at 1 33 34 PM" src="https://github.com/nshganesh/ai-issue-summary/assets/14258513/2fc42623-67bb-41be-aa49-2f8f0f111cf5">
