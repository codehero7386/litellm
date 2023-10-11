import requests
import json

class LLMClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def generate_text(self, prompt, max_length=50, num_results=1, temperature=0.7):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'prompt': prompt,
            'max_length': max_length,
            'num_results': num_results,
            'temperature': temperature
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            results = response.json()
            return [result['choices'][0]['message']['content'] for result in results]
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example usage with OpenAI's GPT-3
    api_key = 'YOUR_OPENAI_API_KEY'
    api_url = 'https://api.openai.com/v1/engines/davinci/completions'  # Replace with the appropriate URL

    llm_client = LLMClient(api_key, api_url)

    prompt = "Translate the following English text to French: 'Hello, World!'"
    translated_text = llm_client.generate_text(prompt, max_length=50, num_results=1, temperature=0.7)

    for text in translated_text:
        print(text)
