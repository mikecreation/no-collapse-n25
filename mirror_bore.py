import os
from collections import defaultdict
from openai import OpenAI

# remove proxy env vars
for v in ("HTTP_PROXY","HTTPS_PROXY","http_proxy","https_proxy"):
    os.environ.pop(v, None)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class ShellMemory:
    def __init__(self):
        self.store = defaultdict(list)
    def add(self, tag, line):
        self.store[tag].append(line)
    def get(self, tag):
        return "\n".join(self.store[tag])

mem = ShellMemory()

def _call(full_prompt: str, max_tokens: int = 4000):
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Python REPL. "
                    "Return exactly one line that begins with 'moves ='. "
                    "No commentary or extra text."
                )
            },
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.0,
        timeout=20,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content, resp.usage.total_tokens

def solve(tag: str, prompt: str):
    history = mem.get(tag)
    full_prompt = f"{history}\n\n{prompt}" if history else prompt
    text, toks = _call(full_prompt)
    mem.add(tag, text.splitlines()[0])
    return text, toks
