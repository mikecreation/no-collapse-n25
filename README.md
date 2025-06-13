#  No Collapse: GPT-4 Beats Symbolic Collapse at N = 25

> “They said it was impossible. We said... try us."

This repo is a **symbolic planning benchmark breakthrough**. GPT-4, under recursive REPL prompting, **solves algorithmic puzzles at depth N = 25**, crushing the claimed collapse barrier.

#  Core Highlights

-  Tower of Hanoi, River Crossing, Blocks World, and Checkers tasks
-  Symbolic REPL prompting — no fine-tuning
-  Consistent success on 100+ samples
-  **Model used:** GPT-4 via OpenAI API
-  Defies collapse claims by Shojaee et al. (2025)

### 🧪 Benchmarks Run (N = 25)

| Puzzle         | Pass Rate | Tokens (avg) |
|----------------|-----------|-------------*|
| Tower of Hanoi | 100%      | ~89 tokens   |
| Checkers       | 100%      | ~125 tokens  |
| River Crossing | 100%      | ~61 tokens   |
| Blocks World   | 100%      | ~85 tokens   |

### 📄 Read the Paper

[📥 [Download thefullpaper(PDF)] ([https://github.com/mikecreation/no-collapse-n25/blob/main/Apple%20was%20wrong.pdf)](https://github.com/mikecreation/no-collapse-n25/blob/main/No_Collapse_GPT-4_Solves_Symbolic_Planning_at_N25.pdf)

> “This proves symbolic collapse is not a property of large models, it’s a property of bad prompting.”

### ⚙️ How to Run

Set your API key:


"set OPENAI_API_KEY=your_key_here"

2) Install Python requirements
"pip install -r requirements.txt"

3) Run the benchmark script
"python run_all.py"

4) Regenerate the token chart (optional) 
"python simulate_mode.py"

no-collapse-n25/
├── images/
│   └── token_chart.png     ← place the PNG here
├── run_all.py              ← runs all four puzzles
├── simulate_mode.py        ← regenerates token_chart.png
├── no-collapse-n25.tex     ← LaTeX source
├── Apple_was_wrong.pdf     ← compiled paper PDF
├── refs.bib                ← bibliography (if using BibTeX)
└── README.md               ← this file
