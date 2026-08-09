# Context Engineering: A Step-by-Step Practical Guide

*How to build context so agents can reliably build features and fix bugs in your project.*

---

## Table of Contents

1. [What Is Context Engineering?](#1-what-is-context-engineering)
2. [The Context Window: What Goes In](#2-the-context-window-what-goes-in)
3. [Token Budgets & What to Leave Out](#3-token-budgets--what-to-leave-out)
4. [Memory & Retrieval Strategies](#4-memory--retrieval-strategies)
5. [Context Patterns for Code Agents](#5-context-patterns-for-code-agents)
6. [Onboarding an Agent to Your Project](#6-onboarding-an-agent-to-your-project)
7. [Building a Context Pipeline from Scratch](#7-building-a-context-pipeline-from-scratch)
8. [Worked Example A: Bug-Fix Agent](#8-worked-example-a-bug-fix-agent)
9. [Worked Example B: Feature-Building Agent](#9-worked-example-b-feature-building-agent)
10. [What to Do Next](#10-what-to-do-next)

---

## 1. What Is Context Engineering?

### The one-line definition

> Context engineering is designing dynamic systems that give an LLM the right information, in the right format, at the right time — so it can act correctly.

### Prompt engineering vs context engineering

| | Prompt Engineering | Context Engineering |
|---|---|---|
| **Focus** | The words you type | The entire system that fills the context window |
| **Scope** | One message | Many sources assembled dynamically |
| **Skill** | Communication | System design + architecture |
| **Failure mode** | Bad phrasing | Wrong or missing information |

**Key insight:** Most agent failures are context failures, not model failures. The model is capable — it just didn't have what it needed.

### Mental model: the agent as a contractor

Imagine hiring a contractor to renovate your house. If you hand them only a vague request ("make it better"), they'll guess wrong. If you give them:

- Blueprints (project structure)
- The specific problem (task description)
- What they can't touch (constraints)
- Examples of your taste (few-shot examples)
- A way to look things up (retrieval tools)

They'll do exactly what you wanted. Context engineering is the practice of building that information package — dynamically, for every task.

---

## 2. The Context Window: What Goes In

Every LLM call has a **context window** — a fixed token budget. Think of it as a whiteboard the model can see. Everything you want the agent to know must fit on that whiteboard.

### The four zones

```
┌─────────────────────────────────────────────────────┐
│  ZONE 1: SYSTEM PROMPT                              │  ~500–2000 tokens
│  Role, project conventions, rules, output format   │  (static, always present)
├─────────────────────────────────────────────────────┤
│  ZONE 2: RETRIEVED CONTEXT                          │  ~2000–10000 tokens
│  Relevant files, docs, past memories, tool outputs │  (dynamic, per task)
├─────────────────────────────────────────────────────┤
│  ZONE 3: TASK + CONVERSATION                        │  ~500–2000 tokens
│  Current task, user message, recent history        │  (dynamic, per turn)
├─────────────────────────────────────────────────────┤
│  ZONE 4: RESPONSE SPACE                             │  ~1000–4000 tokens
│  Reserved for the model's output                   │  (always reserve this!)
└─────────────────────────────────────────────────────┘
```

**Rule:** Reserve Zone 4 first. Fill Zones 1 → 3 in priority order. Never let Zone 2 crowd out the others.

### What each zone contains

**Zone 1 — System Prompt (static)**
- Agent role: "You are a senior Python engineer working on a FastAPI project."
- Project conventions: "Always use type hints. Never modify tests."
- Output format: "Return code changes as unified diffs."
- Constraints: "Only edit files the user specifies."

**Zone 2 — Retrieved Context (dynamic per task)**
- Source files relevant to the current task
- Relevant test files
- Error traces / stack traces
- Past task outcomes (memory)
- API docs or dependency information
- Dependency graph for affected modules

**Zone 3 — Task + Conversation (dynamic per turn)**
- The specific task: "Fix the NullPointerException in auth.py line 47"
- Conversation history (last 3–5 turns, not all of history)
- Tool call results from this turn

**Zone 4 — Response Space**
- Always reserve at minimum 1000 tokens, ideally 2000–4000 for code tasks.

---

## 3. Token Budgets & What to Leave Out

### Why less is often more

Models have an **attention problem**: they pay more attention to content near the beginning and end of the context. Content buried in the middle gets "lost." This is called the **lost-in-the-middle problem**.

```
Attention level:
HIGH  ████████░░░░░░░░░░░░░░░░░░░░░░░░████████  HIGH
       start                              end
LOW                   MIDDLE
```

→ **Put your most important context at the start (system prompt) or the end (task). Never bury key instructions in the middle.**

### What to leave out

| Include | Leave out |
|---------|-----------|
| Files the agent needs to read or edit | Files unrelated to the task |
| The exact error trace | Full application logs (all of them) |
| The 3 most relevant tests | All 500 tests |
| Recent conversation (last 3–5 turns) | Full conversation history |
| Concise project conventions | Long verbose documentation |
| The dependency graph for affected modules | The entire codebase |

### Token budget calculation (example for 128k window)

```
Total window:          128,000 tokens
Reserve for response:   -4,000 tokens
Available for context: 124,000 tokens

Allocation:
  System prompt:        ~1,500 tokens  (role + conventions + output format)
  Project overview:     ~1,000 tokens  (architecture summary)
  Retrieved files:     ~80,000 tokens  (relevant source code)
  Error trace + task:   ~2,000 tokens  (current task)
  Conversation history: ~3,000 tokens  (last 5 turns)
  Tool outputs:         ~5,000 tokens  (search results, test runs)
  Safety buffer:       ~31,500 tokens  (room to grow)
```

---

## 4. Memory & Retrieval Strategies

### The four types of memory

```
┌─────────────────────────────────────────────────────────────┐
│  WORKING MEMORY         In the context window right now     │
│  (short-term)           Cleared after the session ends      │
├─────────────────────────────────────────────────────────────┤
│  EPISODIC MEMORY        What happened in past sessions      │
│  (experience log)       "Last time I edited auth.py, X broke"│
├─────────────────────────────────────────────────────────────┤
│  SEMANTIC MEMORY        General facts about the project     │
│  (knowledge store)      Architecture, patterns, conventions  │
├─────────────────────────────────────────────────────────────┤
│  PROCEDURAL MEMORY      How to do recurring tasks           │
│  (skills)               "To add an endpoint, do A → B → C"  │
└─────────────────────────────────────────────────────────────┘
```

### RAG vs Memory — they solve different problems

| | RAG | Agent Memory |
|---|---|---|
| **What it gives** | External knowledge (docs, files) | Past experience (outcomes, preferences) |
| **Stateless?** | Yes — no awareness of prior sessions | No — persists across sessions |
| **When to use** | "Look up this file / this doc" | "Remember what happened last time" |
| **Implementation** | Vector DB + semantic search | Database keyed by session/user/task |

**You need both.** RAG gives the agent knowledge. Memory gives it continuity.

### How to implement simple memory (Python)

```python
import json
from pathlib import Path

# Episodic memory: save outcomes after each task
def save_memory(task_id: str, task: str, outcome: str, files_changed: list[str]):
    memory_file = Path(".agent-memory/episodes.jsonl")
    memory_file.parent.mkdir(exist_ok=True)
    with open(memory_file, "a") as f:
        f.write(json.dumps({
            "task_id": task_id,
            "task": task,
            "outcome": outcome,        # "success" | "failed" | "partial"
            "files_changed": files_changed,
            "timestamp": "2026-08-09"
        }) + "\n")

# Retrieve relevant past episodes for a new task
def get_relevant_memories(new_task: str, files_involved: list[str]) -> list[dict]:
    memory_file = Path(".agent-memory/episodes.jsonl")
    if not memory_file.exists():
        return []
    episodes = [json.loads(line) for line in memory_file.read_text().splitlines()]
    # Simple relevance: episodes that touched the same files
    relevant = [e for e in episodes if any(f in e["files_changed"] for f in files_involved)]
    return relevant[-5:]  # return last 5 relevant episodes
```

### Simple RAG pipeline (Python)

```python
# pip install llama-index-core llama-index-readers-file openai
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Build the index from your project files
documents = SimpleDirectoryReader("./src").load_data()
index = VectorStoreIndex.from_documents(documents)

# Query: retrieve the most relevant chunks for a task
retriever = index.as_retriever(similarity_top_k=5)

def get_relevant_code(task_description: str) -> str:
    nodes = retriever.retrieve(task_description)
    return "\n\n---\n\n".join(node.text for node in nodes)
```

---

## 5. Context Patterns for Code Agents

### Pattern 1: Task-scoped context loading

Never pre-load the entire codebase. Load only what the current task needs.

```python
def build_task_context(task: str, error_trace: str = None) -> str:
    context_parts = []

    # 1. Project overview (always include — small and high value)
    context_parts.append(Path("CLAUDE.md").read_text())

    # 2. Files directly mentioned in the task
    for filepath in extract_file_mentions(task):
        context_parts.append(f"=== {filepath} ===\n{Path(filepath).read_text()}")

    # 3. Error trace (if this is a bug fix)
    if error_trace:
        context_parts.append(f"=== ERROR TRACE ===\n{error_trace}")
        # Find files mentioned in the trace and load them too
        for filepath in extract_file_mentions(error_trace):
            context_parts.append(f"=== {filepath} ===\n{Path(filepath).read_text()}")

    # 4. Relevant past memories
    memories = get_relevant_memories(task, extract_file_mentions(task))
    if memories:
        memory_text = "\n".join(f"- Past task: {m['task']} → {m['outcome']}" for m in memories)
        context_parts.append(f"=== RELEVANT PAST EXPERIENCE ===\n{memory_text}")

    return "\n\n".join(context_parts)
```

### Pattern 2: Error trace formatting

A well-formatted error trace dramatically improves fix quality. Structure it explicitly:

```
=== ERROR TRACE ===
Type:    NullPointerException
File:    src/auth/validator.py
Line:    47
Message: 'NoneType' object has no attribute 'user_id'

Stack:
  auth/validator.py:47  validate_token(token)
  auth/router.py:23     POST /auth/login
  main.py:8             app startup

Failing test:
  tests/test_auth.py::test_login_with_expired_token

Test output:
  FAILED tests/test_auth.py::test_login_with_expired_token
  AssertionError: Expected 401, got 500
```

Don't just dump the raw stack trace. Label each part. The model reasons better over structured, labeled input.

### Pattern 3: Diff output format

Ask the agent to output diffs, not full files. This keeps the response small and reviewable.

```python
SYSTEM_PROMPT = """
You are a Python engineer. When making code changes:
- Return ONLY the changed code as a unified diff
- Do not repeat unchanged lines
- Include file path and line numbers in the diff header

Format:
--- a/src/auth/validator.py
+++ b/src/auth/validator.py
@@ -44,7 +44,10 @@
 def validate_token(token: str) -> User:
-    return db.get_user(token)
+    user = db.get_user(token)
+    if user is None:
+        raise HTTPException(status_code=401, detail="Invalid token")
+    return user
"""
```

### Pattern 4: Codebase map (for large projects)

Instead of loading raw files, pre-generate a structural map and load that first:

```python
# Generate once, update when structure changes
def generate_codebase_map(root: str = "./src") -> str:
    lines = ["# Codebase Map\n"]
    for path in sorted(Path(root).rglob("*.py")):
        rel = path.relative_to(root)
        # Extract function/class names without loading full file content
        import ast
        try:
            tree = ast.parse(path.read_text())
            symbols = [n.name for n in ast.walk(tree)
                      if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
            lines.append(f"{rel}: {', '.join(symbols)}")
        except:
            lines.append(str(rel))
    return "\n".join(lines)
```

The map looks like:
```
src/auth/validator.py: validate_token, TokenValidator, check_expiry
src/auth/router.py: login, logout, refresh_token
src/users/models.py: User, UserCreate, UserUpdate
```

This gives the agent a navigable map (small tokens) before deciding which files to load (large tokens).

---

## 6. Onboarding an Agent to Your Project

### What a project context file (CLAUDE.md) should contain

Think of this as the onboarding doc you'd write for a new engineer on day one. It covers:

```markdown
# Project: My FastAPI App

## What this project does
A REST API for user authentication and task management.

## Tech stack
- Python 3.11, FastAPI, SQLAlchemy, PostgreSQL
- pytest for tests, alembic for migrations
- Docker for local dev

## Project structure
src/
  auth/       — authentication (JWT, validators, routes)
  users/      — user CRUD
  tasks/      — task CRUD
  main.py     — app entry point
tests/        — mirrors src/ structure
alembic/      — database migrations

## Key conventions
- All routes return Pydantic models, never raw dicts
- DB sessions injected via Depends(get_db)
- Auth: all protected routes use Depends(get_current_user)
- Tests: use fixtures from tests/conftest.py, never real DB

## How to run
  uvicorn src.main:app --reload
  pytest tests/

## How to add a new endpoint
1. Define Pydantic request/response models in models.py
2. Write the route in router.py
3. Register the router in main.py
4. Write tests in tests/test_<module>.py

## Do not
- Modify alembic/versions/ files directly
- Use sync db calls (always async)
- Import from tests/ in src/
```

### What to include vs exclude in CLAUDE.md

| Include | Exclude |
|---------|---------|
| Tech stack + versions | Install instructions (use README) |
| File/folder purpose | Full API documentation |
| Naming + coding conventions | Every edge case and exception |
| How to add a new X (patterns) | Implementation details (in code) |
| What NOT to do (guardrails) | Obvious things ("write tests") |
| How to run and test | CI/CD pipeline details |

**Keep it under 2,000 tokens.** An agent that reads a 10,000-token CLAUDE.md will lose key details to the lost-in-the-middle problem.

### Placing CLAUDE.md in your project

```
my-project/
├── CLAUDE.md          ← root level, loaded for every task
├── src/
│   ├── auth/
│   │   └── CLAUDE.md  ← optional: module-level context loaded when auth/ is in scope
│   └── users/
├── tests/
└── ...
```

Module-level CLAUDE.md files let you have deep context for complex modules without bloating the root file.

---

## 7. Building a Context Pipeline from Scratch

### Architecture overview

```
Task (user input)
      │
      ▼
┌─────────────────┐
│  1. Parse task  │  Extract: file mentions, error type, task type (bug/feature)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. Retrieve    │  Load: relevant files, past memories, codebase map
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. Assemble    │  Build the final context: system prompt + retrieved + task
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  4. Call LLM    │  Send assembled context to the model
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  5. Apply +     │  Parse diff, apply to files, run tests
│     Verify      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  6. Save memory │  Record outcome → episodic memory
└─────────────────┘
```

### Step-by-step implementation

#### Step 1: Set up the project

```bash
mkdir my-agent && cd my-agent
pip install anthropic llama-index-core llama-index-readers-file python-dotenv
```

```
my-agent/
├── agent.py           ← main agent loop
├── context.py         ← context assembly
├── memory.py          ← episodic memory
├── tools.py           ← file read/write tools
├── .agent-memory/     ← persisted memory store
└── target-project/    ← the project your agent works on
    └── CLAUDE.md
```

#### Step 2: Build context assembly (context.py)

```python
from pathlib import Path
import re

def load_project_context(project_root: str) -> str:
    """Load the CLAUDE.md project overview."""
    claude_md = Path(project_root) / "CLAUDE.md"
    if claude_md.exists():
        return claude_md.read_text()
    return ""

def extract_file_mentions(text: str, project_root: str) -> list[str]:
    """Find file paths mentioned in text."""
    pattern = r'[\w/.-]+\.py'
    candidates = re.findall(pattern, text)
    existing = []
    for c in candidates:
        full = Path(project_root) / c
        if full.exists():
            existing.append(str(full))
    return list(set(existing))

def load_files(paths: list[str]) -> str:
    """Load file contents with headers."""
    parts = []
    for path in paths:
        content = Path(path).read_text()
        parts.append(f"=== {path} ===\n{content}")
    return "\n\n".join(parts)

def assemble_context(
    task: str,
    project_root: str,
    error_trace: str = None,
    memories: list[dict] = None
) -> str:
    parts = []

    # Zone 1: Project overview
    project_ctx = load_project_context(project_root)
    if project_ctx:
        parts.append(f"=== PROJECT CONTEXT ===\n{project_ctx}")

    # Zone 2: Relevant files
    file_mentions = extract_file_mentions(task + (error_trace or ""), project_root)
    if file_mentions:
        parts.append(load_files(file_mentions))

    # Zone 2: Error trace
    if error_trace:
        parts.append(f"=== ERROR TRACE ===\n{error_trace}")

    # Zone 2: Past memories
    if memories:
        mem_text = "\n".join(
            f"- [{m['outcome']}] {m['task']} (files: {', '.join(m['files_changed'])})"
            for m in memories
        )
        parts.append(f"=== RELEVANT PAST EXPERIENCE ===\n{mem_text}")

    # Zone 3: Current task
    parts.append(f"=== CURRENT TASK ===\n{task}")

    return "\n\n".join(parts)
```

#### Step 3: Build memory (memory.py)

```python
import json
from pathlib import Path
from datetime import date

MEMORY_FILE = Path(".agent-memory/episodes.jsonl")

def save_episode(task: str, outcome: str, files_changed: list[str]):
    MEMORY_FILE.parent.mkdir(exist_ok=True)
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps({
            "date": str(date.today()),
            "task": task,
            "outcome": outcome,
            "files_changed": files_changed
        }) + "\n")

def get_relevant_episodes(task: str, files: list[str], n: int = 3) -> list[dict]:
    if not MEMORY_FILE.exists():
        return []
    episodes = [json.loads(l) for l in MEMORY_FILE.read_text().strip().splitlines()]
    scored = []
    for ep in episodes:
        # Score by file overlap
        overlap = len(set(files) & set(ep["files_changed"]))
        if overlap > 0:
            scored.append((overlap, ep))
    scored.sort(reverse=True)
    return [ep for _, ep in scored[:n]]
```

#### Step 4: Build the agent loop (agent.py)

```python
import anthropic
from context import assemble_context
from memory import save_episode, get_relevant_episodes
from pathlib import Path
import re

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a senior Python engineer.
When fixing bugs or adding features:
- First explain your plan in 2-3 sentences
- Then provide changes as unified diffs only
- Do not include unchanged lines in diffs
- After your diff, list any follow-up actions needed
"""

def run_agent(task: str, project_root: str, error_trace: str = None):
    print(f"\n=== Task: {task} ===\n")

    # Find relevant files and memories
    from context import extract_file_mentions
    files = extract_file_mentions(task + (error_trace or ""), project_root)
    memories = get_relevant_episodes(task, files)

    # Assemble context
    context = assemble_context(task, project_root, error_trace, memories)

    print(f"Context assembled: {len(context)} chars, {len(files)} files loaded")

    # Call the LLM
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=4000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": context}]
    )

    result = response.content[0].text
    print("\n=== Agent Response ===\n")
    print(result)

    # Save to memory
    save_episode(task, "completed", files)

    return result

# Try it
if __name__ == "__main__":
    run_agent(
        task="Fix the NullPointerException in src/auth/validator.py line 47",
        project_root="./target-project",
        error_trace="""
File "src/auth/validator.py", line 47, in validate_token
    return db.get_user(token).user_id
AttributeError: 'NoneType' object has no attribute 'user_id'
        """
    )
```

#### Step 5: Debug what your agent actually sees

Add this before the LLM call to inspect the full assembled context:

```python
def debug_context(context: str, token_estimate: bool = True):
    """Print context with token estimate and zone breakdown."""
    print("=" * 60)
    print("ASSEMBLED CONTEXT (what the agent sees)")
    print("=" * 60)
    print(context)
    print("=" * 60)
    # Rough token estimate: ~4 chars per token
    estimated_tokens = len(context) // 4
    print(f"Estimated tokens: {estimated_tokens:,}")
    print("=" * 60)
```

---

## 8. Worked Example A: Bug-Fix Agent

**Project:** A FastAPI app with a bug in auth.  
**Task:** `"Fix the AttributeError in src/auth/validator.py line 47"`

### Step 1: What context gets assembled

```
=== PROJECT CONTEXT ===
# Project: FastAPI Auth App
[... CLAUDE.md contents ...]

=== src/auth/validator.py ===
from database import db

def validate_token(token: str):
    return db.get_user(token).user_id   # line 47 — the bug

=== src/auth/router.py ===
from auth.validator import validate_token
...

=== ERROR TRACE ===
File "src/auth/validator.py", line 47, in validate_token
    return db.get_user(token).user_id
AttributeError: 'NoneType' object has no attribute 'user_id'

=== CURRENT TASK ===
Fix the AttributeError in src/auth/validator.py line 47
```

### Step 2: What the agent reasons

The agent sees:
- `db.get_user(token)` can return `None` (the error tells it this)
- The function returns `user_id` directly without a null check
- The project uses `HTTPException` for error responses (from CLAUDE.md)

### Step 3: What the agent outputs

```diff
--- a/src/auth/validator.py
+++ b/src/auth/validator.py
@@ -44,5 +44,10 @@
 from fastapi import HTTPException
 
 def validate_token(token: str) -> int:
-    return db.get_user(token).user_id
+    user = db.get_user(token)
+    if user is None:
+        raise HTTPException(status_code=401, detail="Invalid or expired token")
+    return user.user_id
```

### Step 4: Apply, test, save memory

```python
# Apply the diff
apply_diff(result, project_root="./target-project")

# Run tests
import subprocess
test_result = subprocess.run(["pytest", "tests/test_auth.py", "-v"], capture_output=True, text=True)
print(test_result.stdout)

# Save outcome
outcome = "success" if test_result.returncode == 0 else "failed"
save_episode(
    task="Fix AttributeError in validator.py line 47",
    outcome=outcome,
    files_changed=["src/auth/validator.py"]
)
```

### Step 5: What gets stored in memory

```json
{
  "date": "2026-08-09",
  "task": "Fix AttributeError in validator.py line 47",
  "outcome": "success",
  "files_changed": ["src/auth/validator.py"]
}
```

Next time the agent touches `validator.py`, it retrieves this episode and knows: "last time I worked on this file, I fixed a null check issue — be alert for similar patterns."

---

## 9. Worked Example B: Feature-Building Agent

**Project:** Same FastAPI app.  
**Task:** `"Add a POST /tasks endpoint that creates a new task for the current user"`

### Step 1: What context gets assembled

```
=== PROJECT CONTEXT ===
# Project: FastAPI Auth App
## How to add a new endpoint:
1. Define Pydantic models in models.py
2. Write the route in router.py
3. Register the router in main.py
4. Write tests in tests/test_<module>.py
[...]

=== src/tasks/models.py ===
(existing models, if any)

=== src/tasks/router.py ===
(existing routes, if any)

=== src/users/models.py ===
class User(Base):
    id: int
    email: str
    ...

=== RELEVANT PAST EXPERIENCE ===
- [success] Add GET /users endpoint → src/users/router.py

=== CURRENT TASK ===
Add a POST /tasks endpoint that creates a new task for the current user
```

### Step 2: Agent's plan (first part of response)

```
Plan:
1. Add TaskCreate and TaskResponse Pydantic models to src/tasks/models.py
2. Add POST /tasks route to src/tasks/router.py — protected by get_current_user
3. Register /tasks router in main.py
4. Write test: test_create_task_success and test_create_task_unauthorized
```

### Step 3: Agent outputs multiple diffs

```diff
--- a/src/tasks/models.py
+++ b/src/tasks/models.py
@@ -1,3 +1,12 @@
 from pydantic import BaseModel
+from datetime import datetime
+
+class TaskCreate(BaseModel):
+    title: str
+    description: str = ""
+
+class TaskResponse(BaseModel):
+    id: int
+    title: str
+    description: str
+    owner_id: int
+    created_at: datetime
```

```diff
--- a/src/tasks/router.py
+++ b/src/tasks/router.py
@@ -1,4 +1,19 @@
 from fastapi import APIRouter, Depends
+from sqlalchemy.orm import Session
+from database import get_db
+from auth.validator import get_current_user
+from .models import TaskCreate, TaskResponse
+from .service import create_task
+
 router = APIRouter(prefix="/tasks")
+
+@router.post("/", response_model=TaskResponse)
+async def create_task_endpoint(
+    task: TaskCreate,
+    current_user=Depends(get_current_user),
+    db: Session = Depends(get_db)
+):
+    return create_task(db, task, owner_id=current_user.id)
```

### Step 4: Context on the next turn (retry loop)

If tests fail after applying the first diffs, the agent's next context includes:

```
=== PREVIOUS ATTEMPT ===
Applied diffs from previous turn.

=== TEST FAILURE ===
FAILED tests/test_tasks.py::test_create_task_success
ImportError: cannot import name 'create_task' from 'src.tasks.service'
  (module does not exist yet)

=== CURRENT TASK ===
Fix the import error — create src/tasks/service.py with the create_task function
```

The agent now knows exactly what's missing and adds the service layer. Each turn, the context is rebuilt fresh with the latest state.

---

## 10. What to Do Next

### Practice sequence (do these in order)

1. **Write a CLAUDE.md** for a project you already have. Keep it under 1,500 tokens.
2. **Run the context assembly code** from Step 7 against your project. Print what the agent would see for a real task.
3. **Add episodic memory** to the agent. Run two tasks on the same file and verify the second run retrieves the first episode.
4. **Build the full pipeline** end-to-end: assemble context → call LLM → parse diff → apply → run tests → save memory.
5. **Experiment with context size**: Remove the CLAUDE.md and see how response quality drops. Add irrelevant files and observe the noise effect.

### Key principles to remember

| Principle | Why it matters |
|-----------|---------------|
| Context failures cause most agent failures | Fix context before blaming the model |
| Reserve response space first | Never let the window overflow |
| Put critical info at start or end | Lost-in-the-middle is real |
| Selective loading beats full loading | Focused context → better results |
| RAG + Memory are both required | Knowledge ≠ continuity |
| CLAUDE.md is your agent's onboarding doc | Write it before the first task |
| Debug by printing what the agent sees | Invisible context = invisible bugs |

### Tools and libraries worth knowing

| Tool | Purpose |
|------|---------|
| [LlamaIndex](https://llamaindex.ai) | RAG pipelines, document indexing, retrieval |
| [LangChain](https://langchain.com) | Agent orchestration, tool use, chains |
| [Mem0](https://mem0.ai) | Persistent cross-session agent memory |
| [LangGraph](https://langchain.com/langgraph) | Stateful multi-step agent graphs |
| [Anthropic SDK](https://docs.anthropic.com) | Direct LLM API with tool use |

---

*Run `/kb-ingest` on this guide to index it as a wiki note.*
