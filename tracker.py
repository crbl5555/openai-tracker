import openai
import time

class OpenAITracker:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def track_usage(self, model="gpt-4", prompt="Hello", max_tokens=100):
        try:
            start = time.time()
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            duration = time.time() - start
            tokens_used = response['usage']['total_tokens']
            return {
                "prompt": prompt,
                "tokens_used": tokens_used,
                "duration": duration,
                "response": response['choices'][0]['message']['content']
            }
        except Exception as e:
            return {"error": str(e)}
