# LinkedIn Post Generation Agent

This project provides an automated pipeline for generating, refining, and reviewing LinkedIn posts using AI agents. The system ensures posts meet professional standards and style requirements through an iterative review and refinement process.

## Features

- **Initial Post Generation:** Automatically creates a LinkedIn post draft on a given topic.
- **Iterative Review & Refinement:** Uses a loop of review and refinement agents to ensure the post meets quality and style guidelines.
- **Customizable Tools:** Includes tools for character count validation and quality checks.

## Project Structure

```
basic_agent/
└── linkedin_post_agent/
    ├── agent.py                # Root agent pipeline definition
    ├── requirements.txt        # Python dependencies
    ├── subagents/
    │   ├── post_generator/
    │   │   └── agent.py        # Initial post generator agent
    │   ├── post_refiner/
    │   │   └── agent.py        # Post refiner agent
    │   └── post_reviewer/
    │       ├── agent.py        # Post reviewer agent
    │       └── tools.py        # Tools for review (e.g., character count)
    └── ...
```

## How It Works

1. **Initial Post Generation:**  
   The [`initial_post_generator`](linkedin_post_agent/subagents/post_generator/agent.py) creates a draft LinkedIn post.

2. **Refinement Loop:**  
   The draft is passed into a loop ([`refinement_loop`](linkedin_post_agent/agent.py)) where:
   - The [`post_reviewer`](linkedin_post_agent/subagents/post_reviewer/agent.py) checks for length and quality.
   - If improvements are needed, the [`post_refiner`](linkedin_post_agent/subagents/post_refiner/agent.py) updates the post based on feedback.
   - The loop continues until all requirements are met.

3. **Tools:**  
   The reviewer uses tools like [`count_characters`](linkedin_post_agent/subagents/post_reviewer/tools.py) to validate post length and provide actionable feedback.

## Requirements

- Python 3.10+
- See [`requirements.txt`](linkedin_post_agent/requirements.txt) for dependencies.

## Usage

1. **Install dependencies:**
   ```sh
   pip install -r basic_agent/linkedin_post_agent/requirements.txt
   ```

2. **Configure environment variables:**  
   Copy `.env.example` to `.env` and set required values.

3. **Run the agent pipeline:**  
   (Integration with your orchestration framework required; see [`agent.py`](linkedin_post_agent/agent.py) for entry point.)

## Customization

- Modify agent instructions or tools in the `subagents/` directory to adjust review criteria or style requirements.
