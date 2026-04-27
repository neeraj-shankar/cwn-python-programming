
# What is Prompt Engineering?
Prompt engineering is the process of designing inputs to guide a generative AI model to produce accurate, relevant, and structured outputs. Since LLMs are probabilistic, the way we phrase prompts significantly affects results.

- In practice, I use techniques like:
    1. Clear instructions
    2. Role-based prompting
    3. Few-shot examples
    4. Output formatting constraints

For example, instead of saying *‘summarize this’*, I’d say:
*‘Summarize in 3 bullet points for a non-technical audience.’*
This improves consistency and usability in production systems.”


# What are different prompt techniques?
“I usually categorize prompt techniques into:

- **Zero-shot prompting** → No examples
- **Few-shot prompting** → Provide examples for better accuracy
- **Chain-of-thought prompting** → Ask model to reason step-by-step
- **Role prompting** → ‘You are a senior backend engineer…’
- **Instruction-based prompting** → Clear task definition
- **Output formatting** → JSON, bullet points, etc.