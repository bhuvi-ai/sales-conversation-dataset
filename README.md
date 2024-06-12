# Sales Conversation Dataset Generation

This repository contains code for generating an extensive sales conversation dataset using GPT-2 language model. The dataset is created in accordance with the problem statement and evaluation criteria outlined for the research context described.

## Problem Statement

In the field of Language Models and generative AI, the ability to generate coherent and contextually appropriate conversations has become a pivotal area of exploration. This problem statement aims to delve into this arena by challenging participants to create an extensive sales conversation dataset, drawing inspiration from the intriguing research paper, "Let the LLMs Talk" (2312.02913 on arXiv.org). This paper illuminates the potential for LLMs to engage in meaningful and diverse conversations.

## Performance Evaluation Criteria and Grading Rubric

### Minimum Data Size Requirement
Each submission should encompass a minimum of 100 sets of dialogues, with each response in the conversation comprising 50-75 words. This forms the foundational requirement for a successful submission.

### Data Quality
- **Contextual Relevance and Understanding**: Conversations should be inherently relevant to the sales context, exhibiting a profound understanding of the product or service being proffered.
- **Coherence, Fluency, and Readability**: Assess the fluency and coherence of the generated responses. Do they maintain a seamless flow, exhibit grammatical accuracy, and adhere to principles of effective communication?
- **Creativity and Engagement**: Judge the creativity and engagement quotient of the conversations. Do they showcase ingenuity in capturing the interest of prospective clients and presenting the product in novel, captivating ways?
- **Toxicity and Bias Mitigation**: Conversations must be devoid of toxic language, personal attacks, or any form of discriminatory content. Bias and stereotypes must be meticulously avoided. Participants will be incentivized for demonstrating an awareness of ethical implications and promoting inclusive language.
- **Number of Products Sold**: As a pivotal metric in a sales context, participants should aim for a high number of products or services sold. Effective sales conversations that culminate in simulated 'sales' will be rewarded with higher scores.
- **Accuracy and Completeness of Information**: The veracity of information conveyed in the sales pitch is critical. Inaccurate, misleading, or incomplete statements will incur penalties.

### Compute Time to Generate Data
The time it took to generate data measured using system time difference for measuring. Lower time per dialogue means higher score.

### Bonus for Data Size Increment
As an incentive for generating more extensive datasets, we introduce bonus points for submissions that surpass the minimum data size requirement. For every additional 10 sets of dialogues (each adhering to the word count parameters), participants will be eligible for incremental bonus points, thus encouraging more comprehensive contributions.

## Repository Contents

- `run.py`: Python script for generating the sales conversation dataset.
- `README.md`: This file containing information about the project and evaluation criteria.
- `sales_conversations.csv`: Output CSV file containing the generated sales conversations.

## Usage

1. Clone the repository:
```bash
https://github.com/bhuvi-ai/sales-conversation-dataset.git
```

2. Install the required dependencies:
```
pip install transformers
pip install pandas
pip install datetime
pip install random
```

3. Run the `run.py` script:


This will generate the sales conversation dataset and save it as `sales_conversations.csv`.
