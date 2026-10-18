# Multi-Agent System Implementation Runbook: Non-Development Work

**Version:** 1.0  
**Date:** October 18, 2026  
**Related PRD:** [Non-Development PRD](./unified-multi-agent-system-non-dev-prd.md)

---

## Goal

Implement a production-ready multi-agent system for knowledge work (content creation, research, data analysis) that:
- Scales to 20-30+ concurrent agents
- Produces high-quality content through systematic review
- Maintains consistent voice and style
- Reduces time by 40-50% through parallel work and reuse
- Works with multiple LLM providers

---

## Acceptance Criteria

### Phase 1: Foundation (MVP)
- ✅ Document storage system operational
- ✅ Basic coordinator spawning content agents
- ✅ Research ladder enforced (reuse before create)
- ✅ Simple quality review working
- ✅ CLI interface functional
- ✅ Single LLM provider integrated

### Phase 2: Specialization
- ✅ Specialized agents (Researcher, Writer, Analyst, Editor) operational
- ✅ Knowledge base with full-text search
- ✅ Fact verification system working
- ✅ Style consistency checking
- ✅ Approval workflows implemented

### Phase 3: Monitoring
- ✅ Quality metrics dashboard live
- ✅ Content reuse tracking active
- ✅ Token efficiency monitoring
- ✅ Plagiarism detection working

### Phase 4: Scale
- ✅ 20+ concurrent agents supported
- ✅ Multiple content types (research, blog, docs, marketing)
- ✅ 40%+ time reduction achieved
- ✅ 30%+ reuse rate achieved

---

## Prerequisites

### System Requirements
- **OS:** Linux, macOS, or Windows with WSL2
- **Memory:** 8GB RAM minimum, 16GB recommended
- **Storage:** 20GB free space (for knowledge base)
- **Network:** Stable internet connection

### Software Requirements
- **Runtime:** Python 3.10+ OR Node.js 18+
- **Database:** SQLite 3.35+ (embedded) OR PostgreSQL 14+ (production)
- **Search Engine:** Elasticsearch 8+ (optional, for advanced search)
- **Document Processing:** Pandoc 2.19+ (for format conversion)

### LLM Provider Access
At least one of:
- **Anthropic Claude:** API key with Claude 3.5 Sonnet access
- **OpenAI:** API key with GPT-4 access
- **Google Gemini:** API key with Gemini 1.5 Pro access (good for long research)
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
# Expected: src/, config/, docs/, tests/, scripts/, knowledge-base/
```

### Step 2: Install Dependencies

**For Python Implementation:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-nondev.txt

# Install document processing tools
pip install pandoc pypandoc markdown beautifulsoup4

# Verify installation
python -m system.cli --version
```

**For Node.js Implementation:**
```bash
# Install dependencies
npm install

# Install document processing
npm install marked turndown cheerio

# Verify installation
npm run cli -- --version
```

### Step 3: Configure LLM Providers

```bash
# Copy example configuration
cp config/llm-providers-nondev.example.yaml config/llm-providers.yaml

# Edit configuration
nano config/llm-providers.yaml
```

**Configuration Template:**
```yaml
# config/llm-providers.yaml
providers:
  anthropic:
    enabled: true
    api_key: ${ANTHROPIC_API_KEY}
    models:
      coordinator: claude-3-5-sonnet-20241022
      researcher: claude-3-5-sonnet-20241022
      writer: claude-3-5-sonnet-20241022
      editor: claude-3-5-sonnet-20241022
    
  google:
    enabled: true  # Good for research (long context)
    api_key: ${GOOGLE_API_KEY}
    models:
      researcher: gemini-1.5-pro  # 1M token context
      
  openai:
    enabled: false
    api_key: ${OPENAI_API_KEY}
    models:
      writer: gpt-4-turbo-preview
      editor: gpt-4-turbo-preview

# Default provider
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
export GOOGLE_API_KEY="your-api-key-here"

# Reload shell
source ~/.bashrc
```

### Step 4: Initialize System

```bash
# Initialize database and knowledge base
system-cli init \
  --database sqlite://./data/content-system.db \
  --knowledge-base ./knowledge-base

# Create first project
system-cli project create \
  --name "content-hub" \
  --type non-development \
  --path ./projects/content-hub

# Set up style guide
system-cli style-guide create \
  --project content-hub \
  --tone "professional yet approachable" \
  --voice "active, clear, concrete"

# Verify initialization
system-cli status
```

**Expected Output:**
```
✓ Database initialized
✓ Knowledge base created (0 documents)
✓ Project created: content-hub
✓ Style guide configured
✓ Coordinator ready
✓ 0/30 agents active
```

### Step 5: Populate Knowledge Base

```bash
# Import existing content
system-cli knowledge-base import \
  --from ./existing-content \
  --format markdown

# Create templates
system-cli templates create \
  --type blog-post \
  --structure "Hook → Problem → Solution → CTA"

system-cli templates create \
  --type research-report \
  --structure "Abstract → Intro → Findings → Analysis → Conclusion"

# Verify knowledge base
system-cli knowledge-base stats
```

**Expected Output:**
```
✓ Imported 47 documents
✓ Created 2 templates
✓ Knowledge base: 47 documents, 125K words
✓ Reusable sections: 23
✓ Templates: 2
```

### Step 6: Start System Services

```bash
# Start all services
system-cli start-all --project content-hub

# Check status
system-cli status --verbose
```

### Step 7: Verify Installation

```bash
# Run health check
system-cli health-check

# Expected output:
# ✓ Daemon running
# ✓ Coordinator responsive
# ✓ Database accessible
# ✓ Knowledge base indexed
# ✓ LLM provider: anthropic (OK)
# ✓ Document processing: pandoc (OK)
```

---

## Quick Start: Content Creation

### Example 1: Blog Post

```bash
# Request blog post
system-cli request "Write blog post: 10 AI productivity tips" \
  --type blog-post \
  --length 1200 \
  --tone conversational

# System will:
# 1. Check knowledge base for existing tips
# 2. Researcher gathers new tips
# 3. Writer drafts post (reuses 30% from KB)
# 4. SEO Specialist optimizes
# 5. Editor polishes
# 6. Routes to approval

# Monitor progress
system-cli watch --task-id <task-id>

# Preview draft
system-cli preview --task-id <task-id>
```

### Example 2: Research Report

```bash
# Request research report
system-cli request "Research AI regulation trends in EU" \
  --type research-report \
  --length 3000 \
  --sources-min 20

# System will:
# 1. Researcher gathers 20+ sources
# 2. Analyst analyzes trends
# 3. Writer drafts report
# 4. Fact-Checker verifies all claims
# 5. Editor finalizes
# 6. Routes to approval

# View research progress
system-cli research status --task-id <task-id>

# View sources collected
system-cli research sources --task-id <task-id>
```

### Example 3: Content Series

```bash
# Request content series
system-cli request "Create 5-part series on remote work best practices" \
  --type blog-post \
  --count 5 \
  --parallel

# System will:
# 1. Coordinator creates work bundle
# 2. Spawns 5 Writer agents in parallel
# 3. Each checks KB for reusable content
# 4. All drafts reviewed together
# 5. Batch approval workflow

# View series progress
system-cli work-bundle show remote-work-series
```

---

## Configuration Guide

### Project Configuration

```yaml
# projects/content-hub/config.yaml
project:
  name: content-hub
  type: non-development
  
  content_types:
    - blog-post
    - research-report
    - technical-docs
    - marketing-copy
    - social-media
  
  quality:
    min_score: 8.0  # Out of 10
    fact_check_required: true
    plagiarism_check: true
    
  style:
    tone: "professional yet approachable"
    voice: "active, clear, concrete"
    avoid: ["jargon", "passive voice", "buzzwords"]
    
  reuse:
    target_percentage: 30
    similarity_threshold: 0.85
    
  token_efficiency:
    compression: full
    budget_per_task: 80000
```

### Content Type Templates

```yaml
# config/content-types.yaml
content_types:
  blog-post:
    length: 800-1500
    structure: "Hook → Problem → Solution → CTA"
    sources_min: 3
    seo_required: true
    review_stages: [style, seo, quality]
    
  research-report:
    length: 2000-5000
    structure: "Abstract → Intro → Findings → Analysis → Conclusion"
    sources_min: 15
    fact_check_required: true
    review_stages: [fact-check, quality, peer-review]
    
  technical-docs:
    length: variable
    structure: "Overview → Setup → Usage → Examples → Troubleshooting"
    accuracy_critical: true
    review_stages: [accuracy, completeness, clarity]
    
  marketing-copy:
    length: 100-500
    structure: "Headline → Benefits → Features → CTA"
    brand_alignment_required: true
    review_stages: [brand, persuasiveness, legal]
```

---

## Multi-LLM Setup for Content Work

### Scenario 1: Optimize for Research

```yaml
# Use long-context model for research, standard for writing
providers:
  google:
    enabled: true
    models:
      researcher: gemini-1.5-pro  # 1M token context for deep research
      
  anthropic:
    enabled: true
    models:
      writer: claude-3-5-sonnet-20241022
      editor: claude-3-5-sonnet-20241022
      fact_checker: claude-3-5-sonnet-20241022
```

### Scenario 2: Cost Optimization

```yaml
# Use expensive model for quality-critical, cheap for routine
providers:
  anthropic:
    enabled: true
    models:
      editor: claude-3-5-sonnet-20241022      # Quality critical
      fact_checker: claude-3-5-sonnet-20241022  # Accuracy critical
      
  openai:
    enabled: true
    models:
      writer: gpt-4o-mini          # Routine drafting
      seo_specialist: gpt-4o-mini  # Routine optimization
```

### Scenario 3: Specialization by Content Type

```yaml
# Different models for different content types
providers:
  anthropic:
    enabled: true
    content_types:
      research-report: claude-3-5-sonnet-20241022  # Deep analysis
      technical-docs: claude-3-5-sonnet-20241022   # Accuracy
      
  openai:
    enabled: true
    content_types:
      blog-post: gpt-4-turbo-preview      # Creative writing
      marketing-copy: gpt-4-turbo-preview # Persuasive copy
```

---

## Knowledge Base Management

### Adding Content

```bash
# Import single document
system-cli knowledge-base add \
  --file ./content/company-overview.md \
  --tags "about,company,intro"

# Import directory
system-cli knowledge-base import \
  --from ./content/blog-posts \
  --tags "blog,published"

# Add reusable section
system-cli knowledge-base add-section \
  --title "Company Introduction" \
  --content "Our company was founded..." \
  --tags "about,reusable"
```

### Searching Knowledge Base

```bash
# Full-text search
system-cli knowledge-base search "AI productivity tips"

# Search by tags
system-cli knowledge-base search --tags "blog,ai"

# Find similar content
system-cli knowledge-base similar \
  --to "draft-123.md" \
  --threshold 0.8
```

### Maintaining Knowledge Base

```bash
# Update document
system-cli knowledge-base update \
  --id doc-456 \
  --file ./updated-content.md

# Remove outdated content
system-cli knowledge-base remove \
  --older-than 365d \
  --tag "outdated"

# Reindex for search
system-cli knowledge-base reindex
```

---

## Quality Control

### Setting Quality Standards

```yaml
# config/quality-standards.yaml
quality_standards:
  blog-post:
    min_score: 8.0
    criteria:
      accuracy: 9.0
      clarity: 8.5
      engagement: 8.0
      seo: 7.5
      
  research-report:
    min_score: 9.0
    criteria:
      accuracy: 9.5
      completeness: 9.0
      citations: 9.5
      clarity: 8.5
```

### Review Workflow

```bash
# View pending reviews
system-cli reviews pending

# Review content
system-cli review --task-id task-123

# Approve content
system-cli review approve --task-id task-123

# Request revisions
system-cli review revise --task-id task-123 \
  --feedback "Add more concrete examples in section 3"
```

### Fact Verification

```bash
# Run fact check
system-cli fact-check --task-id task-123

# View fact check report
system-cli fact-check report --task-id task-123

# Expected output:
# ✓ 47 claims verified
# ⚠ 2 claims need sources
# ✗ 1 claim contradicts source
```

---

## Monitoring and Metrics

### Quality Metrics

```bash
# Overall quality dashboard
system-cli metrics quality

# Expected output:
# Average Quality Score: 8.7/10
# First-Pass Approval: 73%
# Fact-Check Pass Rate: 96%
# Plagiarism Issues: 0
```

### Efficiency Metrics

```bash
# Content production metrics
system-cli metrics production

# Expected output:
# Content Produced: 127 pieces
# Avg Time per Piece: 2.3 hours
# Reuse Rate: 34%
# Token Efficiency: 52% reduction
```

### Agent Performance

```bash
# Agent efficiency report
system-cli metrics agents

# Expected output:
# Top Performers:
# 1. writer-alice: 8.9 avg quality, 1.8h avg time
# 2. researcher-bob: 9.2 research depth, 23 avg sources
# 3. editor-charlie: 8.7 polish quality, 0.5h avg time
```

---

## Troubleshooting

### Issue: Low Quality Scores

**Symptoms:** Content consistently scoring below threshold

**Solution:**
```bash
# Review quality criteria
system-cli quality-standards show

# Analyze low-scoring content
system-cli metrics quality --filter "score<8.0"

# Adjust agent prompts
system-cli agents configure writer \
  --emphasis "concrete examples, clear structure"

# Increase review strictness
system-cli config set quality.min_score 8.5
```

### Issue: High Plagiarism Detection

**Symptoms:** Content flagged as too similar to existing work

**Solution:**
```bash
# Review flagged content
system-cli plagiarism report --last-7-days

# Increase originality requirement
system-cli config set plagiarism.max_similarity 0.15

# Emphasize originality in prompts
system-cli agents configure writer \
  --instruction "Paraphrase all sources, add original insights"
```

### Issue: Fact-Check Failures

**Symptoms:** Claims failing verification

**Solution:**
```bash
# Review failed claims
system-cli fact-check failures --last-7-days

# Update fact-check sources
system-cli fact-check add-source \
  --url "https://trusted-source.com" \
  --credibility high

# Require source citations
system-cli config set fact_check.require_citations true
```

### Issue: Low Reuse Rate

**Symptoms:** Agents not reusing knowledge base content

**Solution:**
```bash
# Check knowledge base coverage
system-cli knowledge-base stats

# Improve search relevance
system-cli knowledge-base reindex

# Lower similarity threshold
system-cli config set reuse.similarity_threshold 0.75

# Add more reusable sections
system-cli knowledge-base extract-sections \
  --from-published
```

---

## Best Practices

### Content Strategy

1. **Build Knowledge Base First:** Import existing content before creating new
2. **Define Style Early:** Create comprehensive style guide upfront
3. **Set Quality Thresholds:** Establish minimum scores per content type
4. **Review Regularly:** Weekly quality metric reviews
5. **Iterate on Prompts:** Refine agent instructions based on output

### Workflow Optimization

1. **Batch Similar Content:** Group similar requests for efficiency
2. **Parallel Processing:** Use parallel agents for content series
3. **Template Everything:** Create templates for recurring content types
4. **Automate Reviews:** Use automated checks before human review
5. **Track Reuse:** Monitor and optimize knowledge base utilization

### Quality Assurance

1. **Fact-Check Critical Content:** Always verify claims in research/technical content
2. **Plagiarism Check:** Run on all external-facing content
3. **Style Consistency:** Regular style guide compliance checks
4. **Peer Review:** Human review for high-stakes content
5. **A/B Testing:** Test different approaches, measure outcomes

---

## Maintenance

### Daily Tasks

```bash
# Check system health
system-cli health-check

# Review pending approvals
system-cli reviews pending

# Monitor quality metrics
system-cli metrics quality --today
```

### Weekly Tasks

```bash
# Review quality trends
system-cli metrics quality --last-7-days

# Update knowledge base
system-cli knowledge-base sync

# Review agent performance
system-cli metrics agents --last-7-days

# Clean up drafts
system-cli cleanup drafts --older-than 7d
```

### Monthly Tasks

```bash
# Generate content report
system-cli report generate --month $(date +%Y-%m)

# Review and update style guide
system-cli style-guide review

# Archive old content
system-cli archive --older-than 90d

# Update templates
system-cli templates review
```

---

## Scaling Guide

### From 5 to 20 Agents

1. **Expand Knowledge Base:**
   ```bash
   system-cli knowledge-base import --from ./archive
   ```

2. **Add Content Types:**
   ```bash
   system-cli content-types add social-media
   system-cli content-types add video-scripts
   ```

3. **Enable Advanced Search:**
   ```bash
   system-cli search-engine enable elasticsearch
   ```

### From 20 to 30+ Agents

1. **Upgrade Database:**
   ```bash
   system-cli migrate --to postgresql
   ```

2. **Add Specialized Reviewers:**
   ```bash
   system-cli agents add legal-reviewer
   system-cli agents add brand-specialist
   ```

3. **Enable Batch Processing:**
   ```bash
   system-cli config set batch_processing.enabled true
   system-cli config set batch_processing.size 10
   ```

---

## Content Type Examples

### Blog Post Workflow

```bash
# Request
system-cli request "Blog: Getting started with AI agents" \
  --type blog-post \
  --length 1200 \
  --keywords "AI,agents,automation,productivity"

# Process
# 1. Researcher: Check KB (found 3 related posts, reuse 25%)
# 2. Writer: Draft with hook, problem, solution, CTA
# 3. SEO: Optimize for "AI agents tutorial"
# 4. Editor: Polish, improve readability
# 5. Review: Quality score 8.6/10 → Approved

# Output
# - Draft: ./drafts/ai-agents-getting-started.md
# - SEO report: ./reports/seo-ai-agents.json
# - Quality score: 8.6/10
# - Time: 1.8 hours
# - Reuse: 25%
```

### Research Report Workflow

```bash
# Request
system-cli request "Research: AI safety regulations 2026" \
  --type research-report \
  --length 4000 \
  --sources-min 25

# Process
# 1. Researcher: Gather 28 sources (academic, news, reports)
# 2. Analyst: Identify 5 key trends
# 3. Writer: Draft structured report
# 4. Fact-Checker: Verify 63 claims (2 need revision)
# 5. Writer: Revise claims
# 6. Editor: Finalize
# 7. Review: Quality score 9.1/10 → Approved

# Output
# - Report: ./finals/ai-safety-regulations-2026.md
# - Sources: ./research/ai-safety-sources.bib
# - Fact-check: ./reports/fact-check-ai-safety.json
# - Quality score: 9.1/10
# - Time: 4.2 hours
# - Sources: 28
```

---

## Support and Resources

### Documentation
- [Non-Development PRD](./unified-multi-agent-system-non-dev-prd.md)
- [Development Runbook](./IMPLEMENTATION-RUNBOOK.md)
- [API Reference](./API-REFERENCE.md)

### Community
- GitHub Issues: https://github.com/your-org/multi-agent-system/issues
- Discussions: https://github.com/your-org/multi-agent-system/discussions

### Getting Help

```bash
# Built-in help
system-cli help

# Content-specific help
system-cli content-types --help

# Interactive tutorial
system-cli tutorial start --type non-development
```

---

## Appendix: CLI Command Reference

### Content Management

```bash
# Content requests
system-cli request                # Submit content request
system-cli preview                # Preview draft
system-cli approve                # Approve content
system-cli revise                 # Request revisions

# Knowledge base
system-cli knowledge-base add     # Add document
system-cli knowledge-base search  # Search content
system-cli knowledge-base similar # Find similar content
system-cli knowledge-base stats   # View statistics

# Quality control
system-cli review                 # Review content
system-cli fact-check             # Run fact verification
system-cli plagiarism             # Check plagiarism
system-cli quality-score          # Calculate quality score

# Templates
system-cli templates create       # Create template
system-cli templates list         # List templates
system-cli templates apply        # Apply template

# Style guide
system-cli style-guide create     # Create style guide
system-cli style-guide update     # Update style guide
system-cli style-guide check      # Check compliance
```

---

**End of Runbook**
