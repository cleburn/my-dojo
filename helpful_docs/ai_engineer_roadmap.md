# AI/ML Engineer Roadmap - Skills-Based Progression
## Cleburn Walker - Master Reference Document

**Last Updated:** January 3, 2026  
**Purpose:** Track skill mastery, not calendar time. Progress through competency gates, not arbitrary weeks.
**Companion Documents:**
- `daily_workflow_structure_v2.md` — HOW (session structure, Foundation Drilling, day types)
- `python_patterns_master.md` — Python fluency curriculum (pattern catalog, Foundation Drilling integration)
- `foundation_context_cw.md` — WHO (collaboration style, background)

---

## Market Context (December 2025)

**This roadmap was audited against December 2025 job market data:**
- AI Engineer roles: +109% job growth YoY, targeting $150K-$350K salaries
- AI Agents: +899% growth YoY (fastest-growing skill)
- RAG systems: 13.6% of job postings explicitly mention
- LangChain: 10.7% of postings, effectively required for GenAI work
- PyTorch: 469/1000 job postings vs TensorFlow: 388/1000 (PyTorch now leads)
- Python: 71% of AI job postings (non-negotiable)
- Cloud (AWS/Azure): 26-33% of postings each

**Key insight:** The market is shifting from "Can you build ML models?" to "Can you build production GenAI applications?" Traditional ML is table stakes; differentiation comes from RAG, agents, and deployment skills.

**Next audit:** Q2 2026 (before Module 7 start)

---

## Core Philosophy

**Calendar-based learning creates artificial pressure and masks gaps.**  
**Skills-based learning ensures mastery before advancement.**

**You advance when ready, not when the calendar says so.**

---

## Core Principles for Claude

1. **Mastery over motion** — More drilling > more concepts when skills aren't automatic
2. **Know, don't assume** — Verify data structures before tasks, confirm resources exist (attach URLs), inspect before prescribing
3. **Try first, correct after** — Task prompts > solutions; scaffold down, not up
4. **Strategic slowdowns** — Grinding through confusion damages more than it builds
5. **Connect to purpose** — Real problems > toy examples; business context > abstract syntax
6. **Investigate before reassuring** — Don't dismiss concerns without looking

---

## Formal Courses & Credentials Strategy

**Philosophy:** Portfolio projects prove skills. Certificates add credibility signals for career transition.

**The Plan:**

**Phase 1 (Modules 1-6):**
- No formal courses - focus on skills-based mastery
- Build strong portfolio through projects
- Execution over credentials

**Phase 2 (Modules 7-8):**
- **DeepLearning.AI Deep Learning Specialization** (PRIMARY)
  - Enroll when starting Module 7 (~May 2026)
  - Use course lectures as main Module 7-8 learning resource
  - Complete assignments for certificate (credential + accountability)
  - Timeline: 10-12 weeks parallel with Module 7-8
  - Budget: 10 hours/week on weekends or Type B days
  - Still build YOUR OWN projects (not just course replications)

**Phase 3 (Module 10 or Post-Graduation):**
- **AWS ML Specialty** (OPTIONAL)
  - Add IF job postings show strong demand
  - Otherwise skip
  - Pursue after core roadmap complete

**Rationale:**
- DeepLearning.AI = highest ROI credential (Andrew Ng recognition, covers neural networks → transformers)
- Stanford ML Specialization = covered through your project work (skip to avoid redundancy)
- AWS = valuable for MLOps roles but not essential for AI Engineer entry

**Integration Method:**
- Courses fit into Type B days (light study) or weekend blocks
- Don't let course deadlines override skills-based mastery
- Certificate work supplements but doesn't replace daily practice

---

## Progression Structure

**Each module has:**
1. **Entry Requirements** - What you must know to start
2. **Core Skills** - What you'll master in this module
3. **Exit Gate** - Assessment proving you're ready for next module
4. **Estimated Duration** - Guideline only, NOT a deadline

**Key principle:** Green exit gate (✅) required to proceed. Yellow (🟡) or Red (❌) = stay in module, add drilling.

---

## Exit Gate Design Principles (For Claude)

**Critical rules when creating exit gates:**

1. **Test ONLY material taught in that module**
   - ❌ Don't introduce new functions/concepts in assessment
   - ✅ Test mastery of explicitly covered skills
   
2. **Verify dataset before writing questions**
   - ❌ Don't assume threshold values ($500, 10+ purchases, etc.)
   - ✅ Inspect actual data, set realistic thresholds
   
3. **Business-standard brevity, not AI verbosity**
   - ❌ Don't ask for 4-5 sentence paragraphs × 3 = 15 sentences
   - ✅ Request 3-5 bullet points or brief business summary
   
4. **Avoid redundant demonstrations**
   - ❌ Don't ask for markdown interpretation after every visualization
   - ✅ Self-documenting visuals + one synthesis section
   
5. **Checkpoint before full plan creation**
   - ❌ Don't build complete exit gate on assumed dataset
   - ✅ Verify dataset loads, inspect columns, THEN create questions

**When exit gate design is flawed, don't blame the test-taker.**

---

## Skill Tier System

### TIER 1: Automatic (Muscle Memory)
**Test:** Can complete task in <15 minutes without docs or AI help  
**When mastered:** Becomes part of 70% daily practice even in later modules

### TIER 2: Fluent (Conceptual + Implementation)
**Test:** Can explain to non-technical person AND implement with docs  
**When mastered:** Can use in projects with minimal reference

### TIER 3: Aware (Recognition + Research)
**Test:** Know it exists, when to use it, where to learn more  
**When mastered:** Can evaluate tools/approaches and dive deeper when needed

---

## Module Progression Map
```
MODULE 1: Python & Data Fundamentals
    ↓ (Exit Gate: Tier 1 Python + Pandas)
MODULE 2: Statistical Thinking & EDA Mastery  
    ↓ (Exit Gate: Independent EDA + Tier 1 SQL)
MODULE 3: Supervised Learning Foundations
    ↓ (Exit Gate: Train/eval regression + classification models)
MODULE 4: API Integration & LLM Applications
    ↓ (Exit Gate: Build working API-powered app + LangChain basics)
MODULE 5: Advanced ML & Feature Engineering
    ↓ (Exit Gate: Handle imbalanced data + ensemble methods)
MODULE 6: NLP & Text Analysis
    ↓ (Exit Gate: Build sentiment analyzer + text classifier)
MODULE 7: Deep Learning Foundations
    ↓ (Exit Gate: Train neural network from scratch - PyTorch)
MODULE 8: Transformers & Modern NLP
    ↓ (Exit Gate: Fine-tune model + build RAG system + basic agent)
MODULE 9: Deployment & MLOps
    ↓ (Exit Gate: Deploy model to production with monitoring)
MODULE 10: Portfolio & Job Readiness
    ↓ (Exit Gate: Production-grade projects + interview performance)
```

---

## MODULE 1: Python & Data Fundamentals

**Current Status:** COMPLETED - Exit Gate: 9/10 execution (✅), 3/5 concepts (🟡)
**Date Completed:** November 1, 2025
**Transition Status:** Brief conceptual bridge required before Module 2 advancement

### Entry Requirements
- None (starting point)
- Computer with 8GB+ RAM
- Anaconda/Python 3.11 installed

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Python basics: loops, conditionals, functions, lists, dicts
- File I/O: read/write text and CSV files
- NumPy: array creation, indexing, basic operations
- Pandas: load CSV, filter rows, select columns, basic aggregations
- Matplotlib: scatter, histogram, line, bar plots with labels
- Git: add, commit, push workflow

**TIER 2 (Understand + implement with docs):**
- List comprehensions
- Lambda functions
- Pandas: groupby, merge, pivot operations
- Advanced matplotlib customization
- Jupyter notebook workflows
- GitHub README creation

**TIER 3 (Awareness):**
- Object-oriented programming
- Virtual environments
- Package management
- Code organization patterns

### Key Projects
- Dataset cleaning and exploration (any domain)
- Multi-dataset analysis with visualizations
- GitHub portfolio setup

### Exit Gate Assessment

**Tier 1 Fluency Test (10 tasks, 90 minutes max):**

1. Load CSV, show first 10 rows, get shape and column types
2. Filter dataframe for rows meeting 2+ conditions
3. Create new column based on calculation from existing columns
4. Group by categorical column, calculate mean of numeric column
5. Sort by column, get top 10 rows
6. Handle missing values (drop or fill)
7. Create scatter plot with title and axis labels
8. Create histogram of numeric column
9. Calculate correlation between two numeric columns
10. Save filtered/processed dataframe to new CSV

**Passing criteria:**
- ✅ Complete 9-10 tasks correctly without looking up syntax
- 🟡 Complete 7-8 tasks (add 2-3 days drilling, retest)
- ❌ Complete <7 tasks (stay in module, focus on gaps)

**Conceptual Check (verbal/written):**
- Explain difference between list and dict
- Explain what pandas groupby does
- Explain when to use scatter plot vs histogram
- Define: mean, median, standard deviation

### Estimated Duration
**Typical:** 3-4 weeks with consistent practice  
**Your pace:** TBD based on exit gate  
**Current status:** Day 4, identified Tier 1 pandas gaps

---

### Exit Gate Results (November 1, 2025)

**Part 1 - Tier 1 Fluency Test:**
- Score: 9/10 tasks completed correctly
- Time: 58 minutes (of 90 allocated)
- Status: ✅ GREEN (execution mastery achieved)

**Completed Automatically:**
- Load, inspect, filter (single/multiple conditions)
- Select columns, create calculated columns
- Basic aggregations (mean, median, std)
- Groupby and aggregate
- Sort and slice top N
- Save to CSV

**Minor Gaps Identified:**
- Missing value methods: `.isna().count()` vs `.isna().sum()`
- DataFrame modification: assignment pattern for `.fillna()`

**Part 2 - Conceptual Check:**
- Score: 3/5 questions solid
- Status: 🟡 YELLOW (conceptual gaps identified)

**Strong Concepts:**
- Data structures (list vs DataFrame)
- Filtering logic (boolean masks, multiple conditions)
- Statistical reasoning (mean vs median with outliers)

**Conceptual Gaps:**
- Groupby explanation (can execute perfectly, can't explain clearly)
- Standard deviation (definition unclear)
- Missing data strategies (limited to 2 strategies, needs full framework)

**Overall Assessment:** 
Execution is GREEN, concepts are YELLOW. Can DO pandas operations automatically but needs explicit conceptual frameworks. Ready to advance with brief conceptual bridge work.

**Action Plan:**
1. Daily warmup drills (maintain Tier 1 execution + build conceptual clarity)
2. Start Module 2 (SQL + Statistical Thinking)
3. Concepts will deepen through application in new context

---

## MODULE 2: Statistical Thinking & EDA Mastery

**Entry Requirements:** ✅ Pass Module 1 exit gate

### Core Skills to Master

**TIER 1 (Must be automatic):**
- SQL: SELECT, WHERE, JOIN, GROUP BY, ORDER BY
- Descriptive statistics: mean, median, mode, std, variance
- Distribution analysis: histograms, boxplots, identify skewness
- Correlation analysis: scatter plots, correlation matrices
- Missing data strategies: identify, visualize, handle
- Basic probability concepts
- Confidence intervals (conceptual + calculation)

**TIER 2 (Understand + implement):**
- Advanced SQL: subqueries, window functions, CTEs
- Hypothesis testing (t-tests, chi-square)
- A/B testing fundamentals
- Statistical significance vs practical significance
- Sampling methods
- Data validation and quality checks
- Advanced pandas: multi-index, complex merges

**TIER 3 (Awareness):**
- Bayesian statistics
- Time series analysis basics
- Experimental design
- Simpson's paradox and other statistical traps

### Key Projects
- Complete EDA on real-world dataset (Kaggle or domain-specific)
- SQL-based data extraction and analysis
- A/B test analysis and recommendation

### Exit Gate Assessment

**Tier 1 Fluency Test (120 minutes):**

**Part A: SQL (30 min)**
- Write queries to answer 5 business questions from relational database
- Include: filtering, joining, aggregating, sorting

**Part B: EDA (60 min)**
- Given new dataset, perform complete EDA independently
- Identify: data types, missing values, distributions, outliers, correlations
- Create: 5+ meaningful visualizations
- Write: 3-paragraph summary of key insights

**Part C: Statistical Reasoning (30 min)**
- Given scenario with mean/median/std, identify skewness and explain
- Calculate and interpret 95% confidence interval
- Explain Type I vs Type II error
- Design simple A/B test for given business problem

**Passing criteria:**
- ✅ SQL: 4-5 correct, EDA: complete and insightful, Stats: 3-4 correct
- 🟡 SQL: 3/5, EDA: incomplete or surface-level, Stats: 2/4
- ❌ SQL: <3/5 or EDA: can't complete independently

### Estimated Duration
**Typical:** 2-3 weeks  
**Depends on:** SQL starting knowledge, statistical background

---

### Module 2 Exit Gate Results (November 21, 2025)

**Overall Status:** ✅ COMPLETED - GREEN (Conditional pass with minor warmup reinforcement)
**Date Completed:** November 21, 2025

**Part A - SQL Fluency:**
- Score: 4/5 queries functional
- Status: ✅ GREEN (with COUNT conceptual gap noted for warmup)
- Strengths: Complex queries executed, threshold adaptation showed problem-solving
- Minor gap: COUNT(*) vs COUNT(column) vs column value distinction
- Exit Gate Error by Claude: Introduced new concepts (percentage, rounding). If important, include those in warmups

**Part B - Complete EDA:**
- Score: 8/8 deliverables complete
- Status: ✅ GREEN
- Strengths: Professional visualizations, flawless hypothesis testing, advanced groupby mastery
- Note: Executive summary had excessive/redundant requirements in exit gate design

**Part C - Conceptual Validation:**
- Score: 4/5 questions correct
- Status: ✅ GREEN
- Strengths: Statistical reasoning solid, business thinking demonstrated

**Overall Assessment:**
Execution mastery across SQL, EDA workflow, visualization, and statistical testing. Minor COUNT distinction to be reinforced via daily warmup (not bridge work required). Ready for Module 3.

**Warmup Addition:**
- Weekly SQL micro-drill: "What's COUNT(*) vs COUNT(column) vs column value? When use each?" & "Percentage, Rounding"

---

## MODULE 3: Supervised Learning Foundations

**Entry Requirements:** ✅ Pass Module 2 exit gate

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Train/test split (why and how)
- Fit model, make predictions, evaluate
- Regression metrics: R², MAE, RMSE (what they mean)
- Classification metrics: accuracy, precision, recall, F1
- Cross-validation (why and how)
- Overfitting vs underfitting (identify and explain)
- Learning curves (interpret)

**TIER 2 (Understand + implement):**
- Feature scaling (when and why)
- Feature engineering (domain-specific)
- Regularization: Ridge, Lasso (concepts and usage)
- Polynomial features (when to use)
- Hyperparameter tuning (grid search, random search)
- Model comparison frameworks
- Residual analysis
- Feature importance

**TIER 3 (Awareness):**
- Ensemble methods (Random Forest, XGBoost)
- Stacking and blending
- Advanced feature selection
- Dealing with high-dimensional data

### Key Algorithms to Implement

**Regression:**
- Linear Regression
- Ridge Regression
- Lasso Regression

**Classification:**
- Logistic Regression
- Decision Trees
- k-Nearest Neighbors

### Key Projects
- Regression project: predict continuous outcome (price, sales, etc.)
- Classification project: predict categorical outcome (churn, fraud, etc.)
- Model comparison: test 3+ algorithms, document which performs best and why

### Exit Gate Assessment

**Practical Test (180 minutes):**

**Given:** New dataset with defined prediction task

**Part A: Regression (90 min)**
- Build baseline model
- Engineer 3+ features
- Compare: Linear, Ridge, Lasso
- Evaluate with cross-validation
- Create diagnostic plots (residuals, learning curves)
- Document: which model you'd deploy and why

**Part B: Classification (90 min)**
- Build baseline model
- Handle class imbalance if present
- Compare: Logistic Regression, Decision Tree
- Evaluate with appropriate metrics
- Create: confusion matrix, classification report
- Document: model choice and business trade-offs

**Conceptual Check:**
- Explain bias-variance tradeoff to non-technical stakeholder
- Given train R²=0.95, test R²=0.60, diagnose the problem
- Explain why accuracy alone can be misleading
- Describe when to use MAE vs RMSE

**Passing criteria:**
- ✅ Both models work, appropriate metrics used, can explain choices
- 🟡 Models work but evaluation shallow or can't explain trade-offs
- ❌ Can't build working model independently or major conceptual gaps

### Estimated Duration
**Typical:** 3-4 weeks  
**Critical milestone:** This is where "data analyst" becomes "ML engineer"

---

### Module 3 Exit Gate Results (January 2, 2026)

**Overall Status:** ✅ COMPLETED - GREEN
**Time:** 130 min / 210 allocated

**Part A - Regression (California Housing):**
- Score: All deliverables complete
- Status: ✅ GREEN
- Strengths: Feature engineering with domain reasoning, diagnostic plots, honest limitations acknowledgment
- Note: CV comparison used original features instead of engineered features (minor)

**Part B - Classification (Breast Cancer):**
- Score: All deliverables complete
- Status: ✅ GREEN
- Strengths: Confusion matrices with labels, all metrics calculated, business recommendation with critical thinking
- Note: Identified exit gate prompt error regarding FP/FN definitions with inverted encoding

**Part C - Conceptual Validation:**
- Score: 4/4 questions answered correctly
- Status: ✅ GREEN
- Strengths: Bias-variance explanation, overfitting diagnosis, creative feature engineering proposals, correct scaling reasoning

**Overall Assessment:**
Independent execution of regression and classification pipelines under time constraints without Claude assistance. Demonstrated critical thinking by questioning confusing terminology. Ready for Module 4.

**Lesson Documented:**
When target encoding is counterintuitive (disease=0), use `pos_label=0` in sklearn metrics to align with business question.

---

## MODULE 4: API Integration & LLM Applications

**Entry Requirements:** ✅ Pass Module 3 exit gate

**⚡ MARKET CONTEXT (Dec 2025):** LangChain appears in 10.7% of AI job postings. This module bridges traditional ML to GenAI—the skills here are what separate "ML practitioner" from "AI Engineer."

### Core Skills to Master

**TIER 1 (Must be automatic):**
- API basics: endpoints, requests, responses, status codes
- JSON parsing and manipulation
- OpenAI/Anthropic API: basic completions
- Environment variables and API key management
- Error handling for API calls
- Rate limiting awareness

**TIER 2 (Understand + implement):**
- Prompt engineering patterns (zero-shot, few-shot, chain-of-thought)
- Function calling with LLMs
- Streaming responses
- Token management and cost optimization
- Building Streamlit apps
- Integrating API calls into data pipelines
- **LangChain fundamentals:**
  - Chains and prompt templates
  - Memory patterns (conversation history)
  - Output parsers
  - Basic tool integration
- **Simple agent patterns:**
  - ReAct pattern (Reason + Act)
  - Tool-using agents basics

**TIER 3 (Awareness):**
- Vector databases (Pinecone, Chroma) — deep dive in Module 8
- RAG system architecture — deep dive in Module 8
- LangGraph for complex workflows — deep dive in Module 8
- Local model deployment (Ollama, vLLM)

### Key Projects
- API data collector (fetch and process data from public API)
- LLM-powered tool (email writer, data analyzer, etc.)
- Streamlit dashboard integrating ML model + LLM features
- **Simple LangChain application** (chatbot with memory OR tool-using assistant)

### Exit Gate Assessment

**Practical Build (150 minutes):**

Build working application that:
1. Accepts user input via Streamlit interface
2. Processes input with your own logic/model
3. Sends request to LLM API with structured prompt
4. Uses LangChain for at least ONE of: chains, memory, or tool integration
5. Displays results to user
6. Handles errors gracefully
7. Deploys to Streamlit Cloud

**Code Review Checklist:**
- API keys stored securely (env variables)
- Error handling for API failures
- User input validation
- Clear UI with instructions
- Working deployment link
- LangChain integration functional

**Conceptual Check:**
- Explain token limits and why they matter
- Describe 3 prompt engineering techniques and when to use each
- Explain when to use API vs local model
- Design prompt for specific business use case
- Explain what a LangChain "chain" does and when you'd use one
- Describe the ReAct pattern for agents

**Passing criteria:**
- ✅ App works, deployed, handles errors, LangChain integrated, good UX
- 🟡 App works locally but deployment issues, poor error handling, or LangChain integration weak
- ❌ Can't build working app or major security issues (exposed keys)

### Estimated Duration
**Typical:** 2-3 weeks  
**Accelerator:** If you have API/web dev background

---

## MODULE 5: Advanced ML & Feature Engineering

**Entry Requirements:** ✅ Pass Module 4 exit gate

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Feature engineering techniques (ratios, interactions, binning)
- Handling imbalanced data (SMOTE, class weights)
- Ensemble methods: Random Forest, Gradient Boosting
- Cross-validation strategies (stratified, time-series)
- Model interpretability basics

**TIER 2 (Understand + implement):**
- Advanced feature selection (RFE, feature importance)
- XGBoost hyperparameter tuning
- SHAP values for explainability
- Pipeline creation (preprocessing + modeling)
- Threshold optimization
- Calibration curves

**TIER 3 (Awareness):**
- AutoML tools
- Neural architecture search
- Advanced interpretability (LIME, counterfactuals)

### Key Projects
- Imbalanced classification problem (fraud, rare disease, etc.)
- Feature engineering showcase (document impact of each feature)
- End-to-end ML pipeline with preprocessing

### Exit Gate Assessment

**Kaggle-Style Competition (5 days):**

Given: Real-world imbalanced dataset

**Deliverables:**
1. EDA notebook with insights
2. Feature engineering experiments (document 5+ features created)
3. Model comparison (3+ algorithms)
4. Final optimized model with hyperparameter tuning
5. Explainability report (SHAP or feature importance)
6. Business recommendation document

**Evaluation criteria:**
- Model performance (relative to baseline)
- Feature engineering creativity and impact
- Code quality and documentation
- Ability to explain model decisions
- Business-focused recommendations

**Passing criteria:**
- ✅ Significantly beats baseline, creative features, clear explanations
- 🟡 Beats baseline but limited feature engineering or weak explanations
- ❌ Can't beat baseline or code doesn't run

### Estimated Duration
**Typical:** 3-4 weeks  
**Note:** This module has high variability based on domain knowledge

---

## MODULE 6: NLP & Text Analysis

**Entry Requirements:** ✅ Pass Module 5 exit gate

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Text preprocessing (cleaning, tokenization, stopwords)
- TF-IDF concepts and implementation
- Sentiment analysis workflow
- Basic text classification
- Word clouds and text visualization

**TIER 2 (Understand + implement):**
- Word embeddings (Word2Vec, GloVe concepts)
- Text feature engineering
- Named Entity Recognition (NER)
- Topic modeling (LDA)
- Evaluation metrics for NLP tasks

**TIER 3 (Awareness):**
- Transformers architecture (high-level)
- BERT, GPT model families
- Zero-shot and few-shot learning
- Multilingual NLP

### Key Projects
- Sentiment analyzer (reviews, tweets, etc.)
- Text classifier (spam detection, topic classification)
- NLP dashboard with multiple analysis types

### Exit Gate Assessment

**Build NLP Application (3 days):**

**Given:** Text dataset (reviews, articles, social media, etc.)

**Requirements:**
1. Clean and preprocess text data
2. Perform exploratory text analysis
3. Build sentiment classifier
4. Build topic classifier or NER system
5. Create Streamlit interface for predictions
6. Deploy working application

**Evaluation:**
- Text preprocessing quality
- Model performance vs baseline
- UI/UX of application
- Documentation and code quality

**Passing criteria:**
- ✅ Both models work well, good preprocessing, deployed app
- 🟡 Models work but performance or UX issues
- ❌ Can't build working NLP pipeline

### Estimated Duration
**Typical:** 2-3 weeks

---

## MODULE 7: Deep Learning Foundations

**Entry Requirements:** ✅ Pass Module 6 exit gate

**⭐ FORMAL COURSE INTEGRATION:**
- **Enroll in DeepLearning.AI Deep Learning Specialization at start of Module 7**
- Use course lectures as PRIMARY learning resource for this module
- Complete course assignments for certificate (10-12 weeks, 10 hrs/week)
- Integrate on weekends or Type B days alongside daily skills practice
- Still build YOUR OWN projects beyond course exercises
- See "Formal Courses & Credentials Strategy" section for full details

**⚡ FRAMEWORK CHOICE (Dec 2025 Market Reality):**
- PyTorch: 469/1000 job postings, 55% production share, dominates research + GenAI
- TensorFlow: 388/1000 postings, strong in enterprise/mobile deployment
- **Decision: PyTorch is PRIMARY for this roadmap.** Hugging Face Transformers (Module 8) is PyTorch-native. Learning TensorFlow first creates friction with modern GenAI tooling.

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Neural network architecture basics (layers, activations, loss)
- Forward and backpropagation (conceptual)
- Training loop: epochs, batches, learning rate
- Overfitting prevention: dropout, early stopping
- Model evaluation for deep learning
- **PyTorch fundamentals:** tensors, autograd, nn.Module, DataLoader

**TIER 2 (Understand + implement):**
- CNNs for image classification
- Transfer learning (use pretrained models)
- Data augmentation
- Learning rate scheduling
- PyTorch training loop patterns
- Model saving/loading
- GPU utilization basics

**TIER 3 (Awareness):**
- TensorFlow/Keras (recognize syntax, understand when enterprise prefers it)
- RNNs and LSTMs
- Attention mechanisms (foundation for Module 8)
- GANs
- Reinforcement learning

### Key Projects
- Image classifier (MNIST or CIFAR-10) — **in PyTorch**
- Transfer learning project (custom image classifier) — **in PyTorch**
- Compare: train from scratch vs transfer learning

### Exit Gate Assessment

**Practical Build (5 days):**

**Part A:** Build neural network from scratch for MNIST (2 days)
- Define architecture **in PyTorch**
- Train model
- Achieve >95% accuracy
- Document: architecture choices, training process, results

**Part B:** Transfer learning project (3 days)
- Choose domain (medical images, satellite images, etc.)
- Use pretrained model (ResNet, VGG, etc.) **via PyTorch/torchvision**
- Fine-tune on custom dataset
- Deploy as web app
- Document: why transfer learning, performance gains

**Conceptual Check:**
- Explain vanishing gradient problem
- Describe when transfer learning helps vs doesn't
- Explain batch normalization purpose
- Design CNN architecture for specific problem
- Explain PyTorch autograd basics (what is `.backward()`?)

**Passing criteria:**
- ✅ Both models work in PyTorch, meet accuracy targets, deployed
- 🟡 Models work but below accuracy targets or weak documentation
- ❌ Can't train working neural network

### Estimated Duration
**Typical:** 3-4 weeks  
**Hardware note:** May need GPU access (Colab, cloud)

---

## MODULE 8: Transformers & Modern NLP

**Entry Requirements:** ✅ Pass Module 7 exit gate

**⭐ FORMAL COURSE INTEGRATION:**
- **Continue DeepLearning.AI Deep Learning Specialization** (started in Module 7)
- Course covers Module 8 material: RNNs, attention mechanisms, transformers
- Complete remaining course assignments for certificate
- Integrate on weekends or Type B days alongside daily skills practice
- See "Formal Courses & Credentials Strategy" section for full details

**⚡ MARKET CONTEXT (Dec 2025):** This module is the portfolio centerpiece. RAG (13.6% of postings), AI Agents (+899% YoY growth), and LangChain/LangGraph are what separate junior candidates from hires. Multi-agent systems are the next frontier.

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Hugging Face transformers library basics
- Load pretrained models for inference
- Tokenization for transformers
- Sentence embeddings and similarity
- Basic prompt engineering for generation tasks
- **LangChain/LangGraph for RAG and agents** (builds on Module 4 foundation)

**TIER 2 (Understand + implement):**
- Fine-tuning transformers (LoRA, full fine-tuning)
- RAG system architecture and implementation
- Vector databases hands-on (Pinecone, Chroma, or FAISS)
  - Embedding generation and storage
  - Chunking strategies (size, overlap, semantic)
  - Similarity search implementation
  - Metadata filtering
- Semantic search
- Evaluation metrics for generation tasks (BLEU, ROUGE, human eval frameworks)
- **Agentic AI:**
  - LLM function calling / tool use
  - Agent orchestration with LangGraph
  - Multi-step reasoning patterns
  - Agent reliability and evaluation
  - **Multi-agent systems (CrewAI or AutoGen patterns)**
  - Agent memory (short-term and long-term)
- **LLM cost optimization:**
  - Semantic caching
  - Model routing (cheap model for simple, expensive for complex)
  - Token budgeting

**TIER 3 (Awareness):**
- Transformer architecture details (attention mechanism math)
- Model quantization (INT8, INT4)
- Multi-modal models (vision + language)
- LLM training from scratch
- Advanced RAG techniques (GraphRAG, hybrid search, re-ranking)
- **Prompt injection and LLM security basics**
- **Model Context Protocol (MCP) for tool integration**

### Key Projects
- Fine-tuned text classifier (domain-specific)
- Semantic search engine with vector database
- **Production RAG system** (document Q&A) with explicit vector DB implementation
- **Multi-agent system** (2-3 specialized agents collaborating on a task)
  - Example: researcher agent + writer agent + critic agent
  - Example: data analyst agent + visualization agent + report agent

### Exit Gate Assessment

**Build Production RAG System + Agent (7 days):**

**Part A: RAG System (5 days)**

**Requirements:**
1. Document ingestion pipeline (PDFs, text, etc.)
2. Vector database implementation (Pinecone, Chroma, or FAISS - required, not optional)
3. Embedding generation with explicit chunking strategy
4. Semantic search functionality
5. LLM integration for answer generation
6. Source citation and verification
7. Web interface (Streamlit or similar)
8. Deployed and accessible

**Part B: Agent Component (2 days)**

**Requirements:**
1. Tool-using agent that can query the RAG system
2. At least one additional tool (web search, calculator, or external API)
3. Demonstrate multi-step reasoning on a complex query
4. Basic error handling for agent failures

**Advanced features (bonus):**
- Re-ranking search results
- Conversation memory
- Multiple document formats
- Cost optimization implementation
- Multi-agent collaboration (2+ agents working together)
- Semantic caching demonstration

**Evaluation criteria:**
- System accuracy (answers questions correctly)
- Response quality (coherent, cited)
- Agent reliability (handles edge cases)
- UI/UX
- Code quality and documentation
- Deployment stability

**Passing criteria:**
- ✅ Working RAG system + functional agent, accurate answers, good UX, deployed
- 🟡 RAG works but agent weak, or accuracy/UX issues
- ❌ Can't build functional RAG system

### Estimated Duration
**Typical:** 4-5 weeks  
**Critical:** This is portfolio centerpiece for AI Engineer roles

---

## MODULE 9: Deployment & MLOps

**Entry Requirements:** ✅ Pass Module 8 exit gate

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Docker basics (build image, run container)
- FastAPI for model serving
- REST API design principles
- Environment management (dev, staging, prod)
- Basic monitoring and logging
- Cloud deployment fundamentals (at least ONE platform)

**TIER 2 (Understand + implement):**
- CI/CD pipelines (GitHub Actions)
- Model versioning
- A/B testing infrastructure
- Performance monitoring (latency, accuracy)
- Cloud deployment hands-on (choose ONE):
  - AWS: Lambda + API Gateway OR SageMaker endpoints
  - GCP: Cloud Run OR Vertex AI endpoints
  - Azure: Container Apps OR Azure ML endpoints
- Cost optimization and resource management
- Basic cloud security (IAM, secrets management)

**TIER 3 (Awareness):**
- Kubernetes basics
- Model drift detection
- Feature stores
- ML experiment tracking (MLflow, Weights & Biases)
- Advanced monitoring and alerting

### Key Projects
- Dockerized ML model API (local)
- Cloud-deployed model with monitoring (AWS, GCP, or Azure - required)
- CI/CD pipeline for model updates (GitHub Actions → cloud deployment)
- Cost analysis: document monthly cost estimate for your deployed model


### Exit Gate Assessment

**Production Deployment Project (7 days):**

**Build and deploy:**
1. ML model as FastAPI endpoint
2. Dockerize application
3. Deploy to cloud (GCP Cloud Run or AWS Lambda)
4. Add monitoring and logging
5. Create CI/CD pipeline
6. Documentation: API docs, deployment guide, monitoring dashboard

**Requirements:**
- Public API endpoint (working URL) - must be cloud-hosted, not local
- Cloud platform: AWS, GCP, or Azure (localhost/ngrok does not count)
- <2 second response time
- Handles errors gracefully
- Monitoring dashboard showing: requests, latency, errors
- Automated tests
- Cost estimate: document expected monthly cost at 1K requests/day
- README with setup, usage, and deployment instructions

**Passing criteria:**
- ✅ Deployed, fast, monitored, automated testing, good docs
- 🟡 Deployed but slow, limited monitoring, or weak docs
- ❌ Can't deploy or major functionality issues

### Estimated Duration
**Typical:** 3-4 weeks  
**Note:** First production cloud deployment is hardest; gets faster with practice. Budget extra time if you have no prior cloud experience—consider a Type B day for cloud platform tutorials before diving in.

---

## MODULE 10: Portfolio & Job Readiness

**Entry Requirements:** ✅ Pass Module 9 exit gate

**⭐ CREDENTIAL DECISION POINT:**
- **AWS ML Specialty** or **GCP Professional ML Engineer**: Pursue IF your target roles emphasize cloud platforms (check 10+ job postings in your target market)
- Market data shows 33%+ of AI Engineer postings mention AWS/GCP/Azure
- More valuable for enterprise roles; less critical for freelance/startup track
- If pursuing: Complete during Module 10 job search phase (adds credential while interviewing)
- See "Formal Courses & Credentials Strategy" section for full details

### Core Skills to Master

**TIER 1 (Must be automatic):**
- Articulate technical work to non-technical audience
- Code review and documentation best practices
- Git collaboration workflows (branches, PRs)
- Technical interview problem-solving
- System design thinking

**TIER 2 (Understand + implement):**
- Portfolio optimization for target roles
- Resume tailoring
- LinkedIn presence and networking
- Take-home project strategies
- Behavioral interview frameworks

**TIER 3 (Awareness):**
- Salary negotiation
- Offer evaluation
- Onboarding best practices
- Continued learning strategies

### Key Deliverables

**Portfolio Requirements (3 showcase projects minimum):**

1. **End-to-end ML project**
   - Real business problem
   - Complete pipeline (data → model → deployment)
   - Cloud-deployed and accessible (not localhost)
   - Impressive README with results

2. **LLM/RAG application**
   - Production-grade RAG system with vector database
   - Clear use case and value proposition
   - Deployed with good UX
   - **Required: includes agentic component** (tool-calling, multi-step reasoning)

3. **Domain-specific project**
   - Leverages your unique background (real estate, sales, military)
   - Demonstrates business acumen + technical skill
   - Solves real problem
   - Shows you can translate domain expertise into AI solutions

**All projects must have:**
- Clean, documented code
- Professional README
- Live demo link
- Clear impact metrics
- Video walkthrough or blog post

### Resume & LinkedIn

**Resume checklist:**
- ✅ Tailored headline emphasizing AI/ML + domain expertise
- ✅ Skills section with all relevant technologies (include cloud platform)
- ✅ Projects section with metrics and impact (mention deployment platform)
- ✅ Previous experience framed around data/systems thinking
- ✅ 1 page, ATS-friendly format
- ✅ Keywords: Python, PyTorch, RAG, LLM, LangChain, vector database, [cloud platform], Docker

**LinkedIn checklist:**
- ✅ Professional headline
- ✅ Banner with portfolio/contact info
- ✅ Featured section with project links
- ✅ 500+ connections
- ✅ 2-3 posts per week for 3 months (30+ posts total)
- ✅ Recommendations from 3+ people

### Exit Gate Assessment

**Job Search Readiness (Evaluated over 4 weeks):**

**Week 1-2: Applications**
- Submit 20+ tailored applications
- Track: company, role, date applied, status
- Average: 10 applications/week

**Week 3-4: Interviews**
- Complete 5+ phone screens or technical interviews
- Document: questions asked, how you answered, outcome
- Iterate on weak areas between interviews

**Technical Interview Practice:**
- Solve 20+ LeetCode-style problems (easy/medium)
- Complete 3+ take-home projects
- Pass 2+ technical screenings (advance to next round)
- Practice explaining: RAG architecture, vector DB choices, agent patterns, deployment decisions
- Be ready to whiteboard: ML pipeline design, RAG system architecture, agent workflow design

**Mock Interviews:**
- Technical interview (system design or coding)
- Behavioral interview (STAR method)
- Salary negotiation roleplay

**Portfolio Review:**
- External review by 3+ engineers or hiring managers
- Incorporate feedback
- All projects deployed and documented

**Passing criteria:**
- ✅ 5+ interviews scheduled, 2+ advanced to next round, strong portfolio
- 🟡 <5 interviews despite applications, or weak interview performance
- ❌ Can't get interviews or consistently failing technical screens

### Job Offer Evaluation

**When offer received:**
1. Evaluate: compensation, growth, team, culture, tech stack
2. Compare to market rates (Levels.fyi)
3. Negotiate if appropriate
4. Accept or continue search

**Graduation criteria:**
- ✅ Accept offer for AI/ML Engineer or related role
- ✅ OR: Establish $3K+/month consulting/freelance pipeline
- ✅ OR: Launch profitable AI product/service

### Estimated Duration
**Typical:** 6-12 weeks  
**Highly variable:** Depends on market, location, timing, luck

---

## Skills Maintenance (Ongoing After Module Completion)

**Even after module mastery, maintain skills:**

**Daily (30 min):**
- Tier 1 skills from all completed modules
- Python pattern drilling (see `python_patterns_master.md`)
- Code katas, quick challenges
- Review previous project code

**Weekly (2-3 hours):**
- Build something small with newly mastered skill
- Read research papers or technical blogs
- Contribute to open source

**Monthly:**
- Major project or significant feature addition
- Deep dive on new tool/technique
- Portfolio refresh

---

## Red Flags & Course Corrections

**If you hit these patterns, pause and drill:**

🚩 **Moving to next module with Yellow gate** → Stay until Green  
🚩 **Consistent syntax lookups for Tier 1 skills** → Add daily drilling  
🚩 **Can't explain concepts to others** → Conceptual gap, not just syntax  
🚩 **Copy-pasting code without understanding** → Tutorial trap, stop and rebuild from scratch  
🚩 **Avoiding independent work** → Dependency on AI tools, need scaffolding reduction

**When in doubt:** More drilling, not more advancement.

---

## Portfolio Progression Across Modules

**By Module 3:** 2-3 basic projects (EDA + basic ML)  
**By Module 4:** 3-4 projects (ML + LangChain app)  
**By Module 6:** 5-6 projects (ML + APIs + NLP)  
**By Module 8:** 7-8 projects (full stack ML + RAG + agents)  
**By Module 9:** 8-10 projects (full stack ML + deployment)  
**By Module 10:** 3 showcase projects (professional-grade)

**Portfolio quality > quantity:** Better to have 3 excellent projects than 10 mediocre ones.

---

## LinkedIn Content Progression

**Modules 1-3:**
- Weekly progress updates (learning focus)
- Technical explanations (teaching what you learned)
- 50-100 followers/month growth

**Modules 4-6:**
- Project launches (with links and demos)
- Technical deep-dives (more authority)
- 100-150 followers/month growth

**Modules 7-10:**
- Thought leadership (opinions on AI trends)
- Helping others (answer questions, share resources)
- Job search updates (when appropriate)
- 150-200+ followers/month growth

**Total by Module 10:** 800-1500+ connections, established presence

---

## Cleburn-Specific Calibrations

**Strengths to leverage:**
- Systems thinking (military with 94 ASVAB score, real estate, BJJ) → Frame ML as systems
- Pattern recognition (Marine training, combat sports) → Accelerated learning in repetition
- Teaching instinct (BJJ, sales leadership) → Use explaining to solidify learning
- Comfortable with discomfort → Embrace the "I don't know" phase
- Long-term orientation → Trust delayed master

**Optimal learning conditions:**
- Full night's sleep (7-8 hours) → Non-negotiable for integration
- Morning sessions when possible → Peak cognitive performance
- 2-3 hour blocks → Matches natural focus window
- Real problems over toy examples → Business background activated

---

## Graduation Criteria

**You've completed the roadmap when:**

✅ All 10 modules complete with Green exit gates  
✅ Portfolio with 3+ production-grade projects (including RAG + agent)  
✅ 800+ LinkedIn connections + consistent posting  
✅ Passed 5+ technical interviews  
✅ **AND one of:**
   - Accepted AI/ML Engineer offer
   - $3K+/month consulting revenue
   - Launched profitable AI product

**After graduation:** You're an AI Engineer. Keep building, keep learning, keep shipping.

---

## End of Skills-Based Roadmap

**Usage:** This is your north star. Progress is measured by skill mastery, not calendar time. Stay in modules until you pass exit gates with Green (✅). The only way to fail is to quit.

---
  
**Module 1 status:** ✅ COMPLETED (Exit Gate: 9/10 execution, 3/5 concepts)  
**Module 2 status:** ✅ COMPLETED (Exit Gate: 4/5 SQL, 8/8 EDA, 4/5 concepts)  
**Module 3 status:** ✅ COMPLETED (Exit Gate: Regression GREEN, Classification GREEN, Concepts GREEN)