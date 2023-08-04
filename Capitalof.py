
import os
import openai
openai.organization = "org-YLFi9xzpghD9In8J4kGESGt0"
openai.api_key = "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"#"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"


def query_gpt3(prompt):
    try:
        response = openai.Completion.create(
            prompt=prompt,
            engine="text-davinci-003",  # You can choose a different engine depending on your requirem>            ,
            max_tokens=128,  # Set the maximum number of tokens in the response
            stop=None,       # You can specify a stop sequence to end the response early if needed
            temperature=0.7  # Controls the randomness of the response (lower values make it more focu>       
        )

        return response['choices'][0]['text'].strip()

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example prompt
prompt_text = "What is capital of India"

# Query GPT-3 with the prompt
response_text = query_gpt3(prompt_text)

# Print the response
print(response_text)


# In[ ]:





# In[ ]:




