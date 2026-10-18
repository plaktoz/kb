# Multi-Agent System Implementation Runbook

**Version:** 1.0  
**Date:** October 18, 2026  
**Related PRDs:** 
- [Development PRD](./unified-multi-agent-system-prd.md)
- [Non-Development PRD](./unified-multi-agent-system-non-dev-prd.md)

---

## Goal

Implement a production-ready multi-agent system for both development and non-development work that:
- Scales to 20-30+ concurrent agents
- Persists context across crashes
- Works with multiple LLM providers
- Reduces cost by 40-60% through token efficiency
- Maintains high quality through systematic verification

---

## Acceptance Criteria

### Phase 1: Foundation (MVP)
- ✅ Version-controlled state storage (hooks) working
- ✅ Basic task tracking database operational
- ✅ Coordinator agent spawning worker agents
- ✅ Minimalism ladder enforced
- ✅ Basic merge queue processing
- ✅ CLI interface functional
- ✅ Single LLM provider integrated

### Phase 2: Specialization
- ✅ Specialized agents (PM, Architect, UX, Dev, Analyst) operational
- ✅ Knowledge base with search working
- ✅ Quality review framework implemented
- ✅ Fact verification for non-dev content
- ✅ Code review for dev work

### Phase 3: Monitoring
- ✅ Three-tier watchdog system running
- ✅ Quality metrics dashboard live
- ✅ Token efficiency monitoring active
- ✅ Escalation system functional

### Phase 4: Scale
- ✅ 20+ concurrent agents supported
- ✅ Multiple LLM providers integrated
- ✅ Token efficiency >40% improvement
- ✅ Cost reduction >25% achieved

---

## Prerequisites

### System Requirements
- **OS:** Linux, macOS, or Windows with WSL2
- **Memory:** 8GB RAM minimum, 16GB recommended
- **Storage:** 10GB free space
- **Network:** Stable internet connection

### Software Requirements
- **Version Control:** Git 2.30+
- **Runtime:** Python 3.10+ OR Node.js 18+ (depending on implementation)
- **Database:** SQLite 3.35+ (embedded) OR PostgreSQL 14+ (production)
- **Container Runtime:** Docker 20+ (optional, for isolated agents)

### LLM Provider Access
At least one of:
- **Anthropic Claude:** API key with Claude 3.5 Sonnet access
- **OpenAI:** API key with GPT-4 access
- **Google Gemini:** API key with Gemini 1.5 Pro access
- **Local LLM:** Ollama with llama3 or similar (for development)

---

## Installation Guide

### Step 1: Clone Repository

```bash
# Clone the system repository
git clone https://github.com/your-org/multi-agent-system.git
cd multi-agent-system

# Verify structure
ls -la
# Expected: src/, config/, docs/, tests/, scripts/
```

### Step 2: Install Dependencies

**For Python Implementation:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m system.cli --version
```

**For Node.js Implementation:**
```bash
# Install dependencies
npm install

# Verify installation
npm run cli -- --version
```

### Step 3: Configure LLM Providers

```bash
# Copy example configuration
cp config/llm-providers.example.yaml config/llm-providers.yaml

# Edit configuration
nano config/llm-providers.yaml
```

**Configuration Template:**
```yaml
# config/llm-providers.yaml
providers:
  anthropic:
    enabled: true
    api_key: ${ANTHROPIC_API_KEY}  # From environment variable
    models:
      coordinator: claude-3-5-sonnet-20241022
      worker: claude-3-5-sonnet-20241022
      reviewer: claude-3-5-sonnet-20241022
    
  openai:
    enabled: false
    api_key: ${OPENAI_API_KEY}
    models:
      coordinator: gpt-4-turbo-preview
      worker: gpt-4-turbo-preview
      reviewer: gpt-4-turbo-preview
  
  local:
    enabled: true  # For development
    endpoint: http://localhost:11434
    models:
      coordinator: llama3:70b
      worker: llama3:8b
      reviewer: llama3:70b

# Default provider (used when not specified)
default_provider: anthropic

# Token efficiency settings
token_efficiency:
  compression_level: full  # lite, full, ultra
  context_compression: true
  lazy_loading: true
```

**Set Environment Variables:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="your-api-key-here"
export OPENAI_API_KEY="your-api-key-here"

# Reload shell
source ~/.bashrc
```

### Step 4: Initialize System

```bash
# Initialize database
system-cli init --database sqlite://./data/system.db

# Create first project
system-cli project create \
  --name "my-first-project" \
  --type development \
  --path ./projects/my-first-project

# Verify initialization
system-cli status
```

**Expected Output:**
```
✓ Database initialized
✓ Project created: my-first-project
✓ Coordinator ready
✓ 0/30 agents active
✓ Token budget: 0/1M used today
```

### Step 5: Start System Services

**Option A: Foreground (Development)**
```bash
# Start daemon
system-cli daemon start --foreground

# In another terminal, start coordinator
system-cli coordinator start --project my-first-project
```

**Option B: Background (Production)**
```bash
# Start all services
system-cli start-all --project my-first-project

# Check status
system-cli status --verbose
```

### Step 6: Verify Installation

```bash
# Run health check
system-cli health-check

# Expected output:
# ✓ Daemon running (PID: 12345)
# ✓ Coordinator responsive
# ✓ Database accessible
# ✓ LLM provider: anthropic (OK)
# ✓ Token budget: Available
# ✓ Disk space: 45GB free
```

---

## Quick Start: Development Work

### Example 1: Simple Feature Implementation

```bash
# Request feature
system-cli request "Add rate limiting to login endpoint"

# System will:
# 1. Coordinator analyzes request
# 2. Spawns worker agent
# 3. Agent climbs minimalism ladder
# 4. Implements minimal solution
# 5. Runs tests
# 6. Submits to merge queue
# 7. Merges to main

# Monitor progress
system-cli watch --task-id <task-id>
```

### Example 2: Complex Feature with Specialized Agents

```bash
# Request complex feature
system-cli request "Build authentication system with OAuth2"

# Coordinator will:
# 1. Spawn Architect agent → Design system
# 2. Spawn PM agent → Define requirements
# 3. Spawn multiple Worker agents → Implement in parallel
# 4. Spawn Reviewer agent → Review code
# 5. Merge queue → Batch merge all PRs

# View work breakdown
system-cli work-bundle show auth-system
```

---

## Quick Start: Non-Development Work

### Example 1: Research Report

```bash
# Request research report
system-cli request "Research report on AI regulation trends" \
  --type research-report \
  --length 3000

# System will:
# 1. Researcher agent → Gather sources
# 2. Analyst agent → Analyze findings
# 3. Writer agent → Draft report
# 4. Fact-Checker agent → Verify claims
# 5. Editor agent → Polish final version

# Monitor progress
system-cli watch --task-id <task-id>
```

### Example 2: Blog Post Series

```bash
# Request blog post series
system-cli request "Write 5 blog posts on AI productivity tips" \
  --type blog-post \
  --count 5

# System will:
# 1. Check knowledge base for existing content
# 2. Spawn 5 parallel Writer agents
# 3. SEO Specialist optimizes each
# 4. Editor reviews all
# 5. Batch approval workflow

# View progress
system-cli work-bundle show ai-productivity-series
```

---

## Configuration Guide

### Project Configuration

```yaml
# projects/my-project/config.yaml
project:
  name: my-project
  type: development  # or non-development
  
  minimalism:
    level: full  # lite, full, ultra
    enforce: true
    
  testing:
    coverage_target: 95
    tdd_required: true
    
  review:
    required: true
    auto_merge: false
    
  token_efficiency:
    compression: full
    budget_per_task: 100000
    
  llm_provider:
    default: anthropic
    fallback: openai
```

### Agent Configuration

```yaml
# config/agents.yaml
agents:
  coordinator:
    model: claude-3-5-sonnet-20241022
    token_limit: 50000
    compression: lite
    
  worker:
    model: claude-3-5-sonnet-20241022
    token_limit: 150000
    compression: full
    handoff_threshold: 0.90
    
  specialized:
    architect:
      model: claude-3-5-sonnet-20241022
      token_limit: 100000
      compression: full
      
    reviewer:
      model: claude-3-5-sonnet-20241022
      token_limit: 75000
      compression: full
```

---

## Multi-LLM Setup

### Scenario 1: Cost Optimization

```yaml
# Use expensive model for critical decisions, cheap for routine work
providers:
  anthropic:
    enabled: true
    models:
      coordinator: claude-3-5-sonnet-20241022  # Critical
      architect: claude-3-5-sonnet-20241022    # Critical
      
  openai:
    enabled: true
    models:
      worker: gpt-4o-mini      # Routine work
      reviewer: gpt-4o-mini    # Routine review
```

### Scenario 2: Redundancy

```yaml
# Primary + fallback for reliability
providers:
  anthropic:
    enabled: true
    priority: 1
    
  openai:
    enabled: true
    priority: 2  # Fallback if Anthropic unavailable
```

### Scenario 3: Specialization

```yaml
# Different models for different tasks
providers:
  anthropic:
    enabled: true
    models:
      coordinator: claude-3-5-sonnet-20241022
      
  openai:
    enabled: true
    models:
      code_generation: gpt-4-turbo-preview
      
  google:
    enabled: true
    models:
      research: gemini-1.5-pro  # Long context for research
```

---

## Monitoring and Debugging

### View System Status

```bash
# Overall status
system-cli status

# Detailed agent status
system-cli agents list --verbose

# Token usage
system-cli metrics tokens --today

# Cost tracking
system-cli metrics cost --this-week
```

### Debug Agent Issues

```bash
# View agent logs
system-cli logs --agent worker-alice --tail 100

# Replay agent session
system-cli debug replay --session session-123

# Inspect agent context
system-cli debug context --session session-123 --step 42
```

### Performance Monitoring

```bash
# Token efficiency report
system-cli metrics token-efficiency --last-7-days

# Quality metrics
system-cli metrics quality --project my-project

# Agent performance
system-cli metrics agents --sort-by efficiency
```

---

## Troubleshooting

### Issue: Agent Stuck

**Symptoms:** Agent not progressing, no tool calls

**Solution:**
```bash
# Check agent status
system-cli agents status worker-alice

# Nudge agent
system-cli agents nudge worker-alice

# If still stuck, handoff to new agent
system-cli agents handoff worker-alice --to worker-bob
```

### Issue: High Token Usage

**Symptoms:** Token budget exhausted quickly

**Solution:**
```bash
# Identify token waste
system-cli metrics token-waste

# Increase compression level
system-cli config set token_efficiency.compression ultra

# Review agent prompts
system-cli debug prompts --agent worker-alice
```

### Issue: Merge Queue Blocked

**Symptoms:** PRs not merging, queue growing

**Solution:**
```bash
# Check merge queue status
system-cli merge-queue status

# View failing tests
system-cli merge-queue failures

# Bisect to find culprit
system-cli merge-queue bisect

# Clear queue (emergency)
system-cli merge-queue clear --force
```

### Issue: LLM Provider Down

**Symptoms:** API errors, timeouts

**Solution:**
```bash
# Check provider status
system-cli providers status

# Switch to fallback provider
system-cli config set default_provider openai

# Restart affected agents
system-cli agents restart --all
```

---

## Best Practices

### Development Work

1. **Start Small:** Begin with simple features to validate setup
2. **Monitor Tokens:** Track token usage daily, optimize high-usage agents
3. **Review Quality:** Check code quality metrics weekly
4. **Gradual Scale:** Add agents incrementally, monitor stability
5. **Test Handoffs:** Verify agent handoff works before scaling

### Non-Development Work

1. **Build Knowledge Base:** Populate with reusable content early
2. **Define Style Guides:** Create clear voice/tone guidelines
3. **Fact-Check Setup:** Configure fact verification sources
4. **Quality Thresholds:** Set minimum quality scores per content type
5. **Review Workflow:** Establish approval workflows before production

### Token Efficiency

1. **Compression Level:** Start with "full", adjust based on quality
2. **Context Pruning:** Review handoff context size regularly
3. **Lazy Loading:** Enable lazy loading for large codebases
4. **Cache Strategy:** Cache frequently accessed files/data
5. **Monitor Waste:** Weekly review of token waste sources

---

## Maintenance

### Daily Tasks

```bash
# Check system health
system-cli health-check

# Review escalations
system-cli escalations list --unresolved

# Monitor token budget
system-cli metrics tokens --today
```

### Weekly Tasks

```bash
# Review quality metrics
system-cli metrics quality --last-7-days

# Optimize token efficiency
system-cli metrics token-waste --last-7-days

# Update knowledge base
system-cli knowledge-base sync

# Backup database
system-cli backup create
```

### Monthly Tasks

```bash
# Review agent performance
system-cli metrics agents --last-30-days

# Update LLM models
system-cli providers update-models

# Clean old sessions
system-cli cleanup --older-than 30d

# Generate monthly report
system-cli report generate --month $(date +%Y-%m)
```

---

## Scaling Guide

### From 5 to 20 Agents

1. **Increase Token Budget:**
   ```bash
   system-cli config set token_budget.daily 5000000
   ```

2. **Enable Batch Processing:**
   ```bash
   system-cli config set merge_queue.batch_size 10
   ```

3. **Add Monitoring:**
   ```bash
   system-cli monitoring enable --dashboard
   ```

### From 20 to 30+ Agents

1. **Upgrade Database:**
   ```bash
   # Migrate from SQLite to PostgreSQL
   system-cli migrate --from sqlite --to postgresql
   ```

2. **Enable Federation (Optional):**
   ```bash
   system-cli federation enable
   ```

3. **Add Load Balancing:**
   ```bash
   system-cli config set scheduler.load_balancing true
   ```

---

## Security Considerations

### API Key Management

```bash
# Use environment variables, never hardcode
export ANTHROPIC_API_KEY="sk-..."

# Or use secret management
system-cli secrets set anthropic_api_key --from-vault
```

### Access Control

```yaml
# config/access-control.yaml
roles:
  admin:
    - manage_agents
    - view_all_projects
    - modify_config
    
  developer:
    - spawn_agents
    - view_own_projects
    - submit_requests
    
  viewer:
    - view_metrics
    - view_own_projects
```

### Audit Logging

```bash
# Enable audit logging
system-cli config set audit.enabled true
system-cli config set audit.log_path ./logs/audit.log

# View audit log
system-cli audit log --last-24h
```

---

## Support and Resources

### Documentation
- [Development PRD](./unified-multi-agent-system-prd.md)
- [Non-Development PRD](./unified-multi-agent-system-non-dev-prd.md)
- [API Reference](./API-REFERENCE.md)
- [Architecture Guide](./ARCHITECTURE.md)

### Community
- GitHub Issues: https://github.com/your-org/multi-agent-system/issues
- Discussions: https://github.com/your-org/multi-agent-system/discussions
- Discord: https://discord.gg/your-server

### Getting Help

```bash
# Built-in help
system-cli help

# Command-specific help
system-cli agents --help

# Interactive tutorial
system-cli tutorial start
```

---

## Appendix: CLI Command Reference

### Core Commands

```bash
# System management
system-cli init                    # Initialize system
system-cli start-all              # Start all services
system-cli stop-all               # Stop all services
system-cli status                 # Show system status
system-cli health-check           # Run health check

# Project management
system-cli project create         # Create new project
system-cli project list           # List projects
system-cli project switch         # Switch active project

# Agent management
system-cli agents list            # List all agents
system-cli agents spawn           # Spawn new agent
system-cli agents status          # Check agent status
system-cli agents handoff         # Handoff between agents

# Work management
system-cli request                # Submit work request
system-cli work-bundle show       # Show work bundle
system-cli watch                  # Watch task progress

# Monitoring
system-cli metrics tokens         # Token usage metrics
system-cli metrics cost           # Cost metrics
system-cli metrics quality        # Quality metrics
system-cli metrics agents         # Agent performance

# Debugging
system-cli debug replay           # Replay agent session
system-cli debug context          # Inspect agent context
system-cli logs                   # View logs
```

---

**End of Runbook**
