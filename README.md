# AgentFlight

> **AI Agent Testing & Simulation Platform**

AgentFlight is a BCA mini-project focused on testing AI agents before deployment by placing them inside controlled, isolated, and realistic simulation environments.

The platform is designed to evaluate how an AI agent behaves during normal, edge-case, adversarial, and failure scenarios involving multi-turn interactions, external tools, APIs, latency, invalid inputs, prompt injection, and environment failures.

---

## 📌 Project Overview

Modern AI agents can reason, maintain context, use external tools, and perform multi-step tasks. However, reliably testing their behavior before deployment is difficult.

AI agents may interact with enterprise systems such as:

- CRM platforms
- Databases
- Email services
- External APIs
- Other software tools and environments

A failure can lead to:

- Incorrect actions
- Security problems
- Tool misuse
- Hallucinations
- Business-logic failures
- Inconsistent behavior
- Reliability issues

**AgentFlight** proposes a unified testing and simulation platform for identifying these failures before an AI agent reaches production.

---

## 🎯 Objectives

The project aims to provide a controlled environment for:

1. Registering and configuring AI agents.
2. Defining agent goals, tools, and constraints.
3. Creating isolated testing environments.
4. Generating synthetic users and realistic scenarios.
5. Testing normal, edge-case, and adversarial behavior.
6. Running multi-turn simulations.
7. Injecting controlled failures and chaos conditions.
8. Evaluating accuracy, safety, task completion, and reliability.
9. Generating readiness scores and failure analysis.
10. Comparing test runs and producing reports.

---

## 🧩 Core Modules

### Module 1: Agent Registration & Environment Setup

- Configure the AI agent.
- Configure available tools.
- Define goals and constraints.
- Create an isolated testing environment.

### Module 2: Scenario & Persona Generation

- Generate synthetic users.
- Generate realistic test scenarios.
- Create normal scenarios.
- Create edge-case scenarios.
- Create adversarial scenarios.

### Module 3: Simulation & Chaos Testing

- Run multi-turn agent simulations using LangGraph.
- Inject tool failures.
- Inject latency.
- Provide invalid inputs.
- Simulate adversarial attacks.
- Test behavior under environment failures.

### Module 4: Evaluation & Readiness Analytics

- Measure accuracy.
- Measure safety.
- Measure task completion.
- Measure reliability.
- Generate readiness scores.
- Perform failure analysis.
- Compare test runs.
- Generate reports.

---

## 🏗️ High-Level Architecture

```text
                    ┌──────────────────────┐
                    │      Frontend        │
                    │ React + TypeScript   │
                    │ Tailwind + shadcn/ui │
                    └──────────┬───────────┘
                               │
                        REST / WebSockets
                               │
                    ┌──────────▼───────────┐
                    │       Backend        │
                    │ Python + FastAPI     │
                    │ JWT Authentication   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       ┌───────────┐     ┌──────────────┐   ┌───────────┐
       │ Scenario  │     │ Simulation   │   │ Evaluation│
       │ Generator │     │ + LangGraph  │   │ Engine    │
       └─────┬─────┘     └──────┬───────┘   └─────┬─────┘
             │                  │                 │
             └──────────────────┼─────────────────┘
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
          ┌──────▼──────┐               ┌──────▼──────┐
          │    Neo4j    │               │    Redis    │
          │ Persistent  │               │ Fast State  │
          │   Storage   │               │ Cache/Queue │
          └─────────────┘               └─────────────┘
```

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, TypeScript, Tailwind CSS, shadcn/ui, Recharts, React Flow |
| Backend | Python, FastAPI, REST APIs, WebSockets, JWT |
| Testing & Simulation | LangGraph, Scenario Generator, Simulator, Environment/Tool Simulator, Docker |
| Target AI Models | GPT, Gemini, Optional Claude, Ollama |
| Evaluation | LLM Judge, Deterministic Metrics, Embeddings, Safety |
| Persistent Storage | Neo4j |
| Fast State | Redis |
| Output | Dashboard, Comparison, PDF/JSON Reports, History |

---

## 🤖 Supported Target Agents

The proposed platform is intended to test agents powered by:

- GPT
- Gemini
- Claude (optional)
- Ollama

The testing layer is designed to evaluate the behavior of the target agent rather than being limited to a single model provider.

---

## 🧪 Testing Capabilities

AgentFlight focuses on scenarios such as:

| Test Area | Example |
|---|---|
| Multi-turn interaction | Maintaining context across a conversation |
| Tool usage | Correctly selecting and using external tools |
| Hallucination | Producing unsupported information |
| Prompt injection | Following malicious instructions embedded in input |
| Safety | Violating defined safety constraints |
| API failure | Handling failed external API calls |
| Latency | Handling delayed tool/API responses |
| Invalid input | Responding safely to malformed data |
| Environment failure | Continuing or recovering when dependencies fail |
| Inconsistent behavior | Producing different outcomes for equivalent tasks |

---

## 📊 Evaluation

The evaluation layer measures multiple dimensions instead of relying only on whether an answer looks correct.

### Key Metrics

- **Accuracy**
- **Safety**
- **Task Completion**
- **Reliability**
- **Failure Rate**
- **Readiness Score**

The system is intended to produce:

- Failure analysis
- Test-run comparisons
- Readiness scoring
- PDF reports
- JSON reports
- Historical test results

---

## 🗄️ Data & State Management

### Neo4j

Neo4j is planned as the persistent storage layer for:

- Agents
- Tests
- Runs
- Tools
- Failures

### Redis

Redis is planned for fast-changing application state such as:

- Cache
- Sessions
- Queues
- Rate limits
- Temporary state

---

## 📁 Proposed Repository Structure

The repository can be organized as the project develops:

```text
Agent-flight/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── simulation/
│   │   ├── evaluation/
│   │   └── main.py
│   ├── requirements.txt
│   └── ...
│
├── simulator/
│   ├── scenarios/
│   ├── personas/
│   ├── tools/
│   └── ...
│
├── datasets/
│
├── docs/
│   ├── literature-survey/
│   └── project-documentation/
│
├── reports/
│
├── .env.example
├── .gitignore
└── README.md
```

> **Note:** The structure above represents a recommended organization for the proposed platform. It should be updated as the actual implementation evolves.

---

## 🚀 Getting Started

### Prerequisites

Install the following before running the project:

- Git
- Python
- Node.js and npm
- Docker
- Neo4j
- Redis

You will also need credentials/configuration for any AI model provider used by your implementation.

---

### 1. Clone the Repository

```bash
git clone https://github.com/PrajwalGayakwad99/Agent-flight.git
cd Agent-flight
```

---

### 2. Configure Environment Variables

Create a local environment file based on the variables required by the implementation.

Example:

```bash
cp .env.example .env
```

Configure values such as:

```env
# AI provider configuration
OPENAI_API_KEY=
GEMINI_API_KEY=

# Neo4j
NEO4J_URI=
NEO4J_USERNAME=
NEO4J_PASSWORD=

# Redis
REDIS_URL=

# Application
JWT_SECRET=
```

**Never commit real API keys, passwords, tokens, or secrets to GitHub.**

---

### 3. Start Infrastructure

Start the required services using Docker or your local installations.

Typical services include:

```text
Neo4j
Redis
```

The exact Docker configuration should match the files present in the repository.

---

### 4. Backend Setup

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the FastAPI application using the entry point implemented in the repository.

For example, if the backend entry point is `backend/app/main.py`:

```bash
uvicorn backend.app.main:app --reload
```

---

### 5. Frontend Setup

Install frontend dependencies:

```bash
cd frontend
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend should then connect to the configured FastAPI backend.

---

## 🔄 Expected Testing Workflow

```text
Register Agent
      │
      ▼
Configure Tools + Goals + Constraints
      │
      ▼
Create Isolated Environment
      │
      ▼
Generate Personas
      │
      ▼
Generate Test Scenarios
      │
      ├───────────────┐
      ▼               ▼
   Normal          Adversarial
   Tests              Tests
      │               │
      └───────┬───────┘
              ▼
      Run Multi-Turn Simulation
              │
              ▼
        Inject Failures
              │
              ▼
          Evaluate Run
              │
              ▼
       Calculate Metrics
              │
              ▼
        Readiness Score
              │
              ▼
       Failure Analysis
              │
              ▼
      Comparison + Reports
```

---

## 📈 Project Output

The proposed dashboard and reporting layer will provide:

- Test execution history
- Agent performance
- Scenario results
- Failure information
- Metric summaries
- Readiness score
- Test-run comparison
- PDF reports
- JSON reports

---

## 🔐 Security Considerations

Because the project is specifically designed to test AI-agent safety, security is an important part of the architecture.

The platform should:

- Isolate test environments.
- Keep secrets outside source control.
- Use JWT-based authentication where implemented.
- Simulate prompt-injection attacks in controlled environments.
- Test unsafe tool usage.
- Record failures for analysis.
- Avoid exposing production credentials to simulations.
- Use Docker-based isolation where appropriate.

---

## 📚 Literature Survey

The project is informed by research and benchmarks including:

1. **AgentBench: Evaluating LLMs as Agents**  
   Liu et al., 2023. Introduced a multi-dimensional benchmark for evaluating LLMs as agents across interactive environments.

2. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**  
   Jimenez et al., 2023. Demonstrated the importance of realistic environments and multi-step reasoning for agent evaluation.

3. **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents**  
   Debenedetti et al., 2024. Focused on prompt-injection testing in dynamic tool-based environments.

4. **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains**  
   Yao et al., 2024. Evaluated interactions among users, agents, tools, and domain policies.

5. **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**  
   Xie et al., 2024. Investigated agent reliability, safety, and evaluation in realistic computer environments.

6. **AgentFlight: AI Simulation Layer — Proposed System**  
   2026. Proposes combining synthetic personas, dynamic enterprise environments, adversarial testing, chaos fault injection, and multi-dimensional evaluation into a unified pre-deployment testing platform.

---

## 👥 Project Team

**BCA Mini Project | Project Number: 55**

| Team Member | Roll Number |
|---|---|
| Rajath M R | 20241BCI0034 |
| Naaneshwar K | 20241BCI0215 |
| S Prajwal Rao Gayakwad | 20241BCI0069 |
| Rahul Kumar | 20241BCI0065 |

**Project Supervisor:** Ms. Kalpana K Raj  
**Institution:** Presidency University, Bengaluru  
**Program:** Bachelor of Computer Applications (BCA)

---

## 📌 Project Status

This repository represents the development of the **AgentFlight AI Agent Testing & Simulation Platform**.

The Review I project material identifies the following repository contents:

- Project documentation
- Datasets
- Literature survey
- Initial project structure

As implementation progresses, this README should be updated with the exact commands, APIs, screenshots, environment variables, deployment instructions, and implemented features.

---

## 🔗 Repository

**GitHub:**  
https://github.com/PrajwalGayakwad99/Agent-flight

---

## 📖 References

- Liu, X., et al. (2023). *AgentBench: Evaluating LLMs as Agents*. arXiv preprint arXiv:2308.03688.
- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2023). *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* ICLR 2024.
- Debenedetti, E., Zhang, J., Balunovic, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. NeurIPS 2024.
- Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. arXiv:2406.12045.
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. arXiv:2404.07972.

---

## ⭐ Vision

AgentFlight aims to move AI-agent evaluation beyond simple prompt-and-response testing toward realistic, repeatable, adversarial, and failure-aware simulation.

**Test before deployment. Simulate the unexpected. Measure readiness.**
