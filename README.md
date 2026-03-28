# AI Voice Agent Starter

Open-source starter kit for building LLM-powered voice agents.

## Overview

This project is a lightweight starting point for building conversational voice agents for use cases such as:

- AI sales calls
- customer support automation
- conversational voice workflows

It currently includes a simple Python-based demo agent to simulate a voice conversation loop.

## Features

- modular agent structure
- prompt-based conversation flow
- simple interactive demo
- ready to expand with ASR / TTS / LLM integrations

## Project structure

```text
app/
  demo_agent.py
.env.example
requirements.txt
README.md
.gitignore
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

## Use Case

This project simulates a real-world AI sales agent for outbound calls.

Example flow:

- greeting
- qualification
- need discovery
- offer generation
- objection handling
- closing

## Roadmap

- [x] Basic conversational demo
- [x] LLM-ready setup
- [ ] Conversation state machine
- [ ] Speech-to-text integration
- [ ] Text-to-speech integration
- [ ] API layer
- [ ] Multi-agent workflows

## Example conversation

User:
Hi, I’m looking for toner supplies for our office printers.

Agent:
Hello, great to hear from you. May I ask which printer models you're currently using?

User:
We use HP LaserJet Pro.

Agent:
Perfect. Based on that, I can suggest compatible toner options that reduce cost per page. Would you like a standard or high-capacity solution?
