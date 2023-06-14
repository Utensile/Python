import os
import openai

# Set your API key
openai.api_key = "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"

# Define the prompt
prompt = "Hello, ChatGPT!"

# Generate a completion
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=100
)

# Extract the generated text from the response
generated_text = response['choices'][0]['text']

# Print the generated text
print("Generated text: ", generated_text)
