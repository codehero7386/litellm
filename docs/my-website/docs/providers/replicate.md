# Replicate

LiteLLM supports all models on Replicate

### API KEYS
```python
import os 
os.environ["REPLICATE_API_KEY"] = ""
```


### Replicate Models
liteLLM supports all replicate LLMs. For replicate models ensure to add a `replicate` prefix to the `model` arg. liteLLM detects it using this arg. 
Below are examples on how to call replicate LLMs using liteLLM 

Model Name                  | Function Call                                                  | Required OS Variables                |
-----------------------------|----------------------------------------------------------------|--------------------------------------|
 replicate/llama-2-70b-chat | `completion('replicate/replicate/llama-2-70b-chat', messages)` | `os.environ['REPLICATE_API_KEY']`    |
 a16z-infra/llama-2-13b-chat| `completion('replicate/a16z-infra/llama-2-13b-chat', messages)`| `os.environ['REPLICATE_API_KEY']`    |
 joehoover/instructblip-vicuna13b | `completion('replicate/joehoover/instructblip-vicuna13b', messages)` | `os.environ['REPLICATE_API_KEY']` |
 replicate/dolly-v2-12b     | `completion('replicate/replicate/dolly-v2-12b', messages)`     | `os.environ['REPLICATE_API_KEY']`    |
 a16z-infra/llama-2-7b-chat | `completion('replicate/a16z-infra/llama-2-7b-chat', messages)` | `os.environ['REPLICATE_API_KEY']`    |
 replicate/vicuna-13b       | `completion('replicate/replicate/vicuna-13b', messages)`       | `os.environ['REPLICATE_API_KEY']`    |
 daanelson/flan-t5-large    | `completion('replicate/daanelson/flan-t5-large', messages)`    | `os.environ['REPLICATE_API_KEY']`    |
 replit/replit-code-v1-3b   | `completion('replicate/replit/replit-code-v1-3b', messages)`   | `os.environ['REPLICATE_API_KEY']`    |