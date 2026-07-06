# Daily Workflow Structure - Skills-Based Learning
## Evergreen Template for All Modules

**Last Updated:** January 3, 2026  
**Purpose:** Ensure optimal skill acquisition through balanced practice, learning, and rest. Progress measured by mastery, not calendar time.

**Companion Documents:**
- `ai_engineer_roadmap.md` — WHERE + WHY (modules, exit gates, Core Principles for Claude)
- `python_patterns_master.md` — Pattern catalog and sequencing for Part 1 Foundation Drilling

---

## Core Daily Structure

**Every session follows this pattern:**

1. **Context refresh** - Review current module goals and Tier 1 status
2. **Tier 1 drilling** - Practice skills that must be automatic (70% of time)
3. **New learning** - Add ONE new concept or skill (20% of time)
4. **Reflection & documentation** - Capture progress and insights (10% of time)

**Session pacing:** Adjust based on energy and progress, not arbitrary time targets

---

## Foundation Drilling (Mandatory)

### Why Foundation Drilling Is Critical (Not Optional)

Foundation Drilling is not a quick checkbox before "real work." It is essential skill-building that compounds across the entire roadmap.

**What Foundation Drilling accomplishes:**
- **Python fluency**: Professional patterns that appear in code reviews, interviews, and production code — not just data science tasks
- **Interview readiness**: The patterns drilled here are exactly what LeetCode and technical interviews test
- **Automatic foundations**: Today's struggle becomes next month's effortless tool
- **Gap prevention**: Without consistent drilling, you can "do ML" but stumble on basic Python when it matters

**Approach:**
- Quality over speed — invest the time needed for real understanding
- Struggle is signal — if a pattern is hard, it needs more reps, not faster completion
- This is learning, not maintenance — you're building, not just preserving

**Claude must never treat Foundation Drilling as something to rush through or minimize.**

**Every session starts with Foundation Drilling before main work:**

### Foundation Drilling Structure

**Part 1: Python Fundamentals & Libraries**

**Part 1a: Fluency Rep**
- Rotate through adopted patterns from `python_patterns_master.md`
- Reinforce learned material
- Pull from "Adopted" or "Fluency Pool" status patterns

**Part 1b: New Pattern Exposure**
- Introduce one new pattern OR drill a "Learning" status pattern
- High-value patterns: 2-3 days repetition before advancing
- Novel patterns: single exposure, save template, move on
- Format: Pattern → Example → Translation → Variations
- Pattern selection follows `python_patterns_master.md` sequencing

**Part 2: Current Module Tier 1 Rep**
- **Day 1 of new week/module:** Reinforce PREVIOUS module Tier 1 skills
  - Reason: You haven't learned new module content yet
  - Example: Module 3 Day 1 = drill Module 2 groupby/SQL/EDA patterns
- **Day 2+ of current week:** Drill concepts taught in PREVIOUS day(s)
  - Reason: Build automaticity on fresh learning
  - Example: Module 3 Day 2 = drill Day 1's train/test split
- **NEVER introduce new concepts in Foundation Drilling** - that's what main work is for

**Part 3: Visualization + SQL Micro-Drill**
- Balanced rotation of visualization types from current/previous modules
- Weekly SQL practical skills (CASE, percentages, rounding, COUNT distinctions)
- Focus: Skills smoother when done by hand vs prompting AI

### Foundation Drilling Part 2 Rule (Crystal Clear)

**Day 1 of new week/module:**
- Part 2 = Reinforce PREVIOUS module's Tier 1 skills
- Why: You haven't learned current module content yet
- Example: Module 3 Day 1 → drill Module 2 groupby/SQL/EDA

**Day 2+ of current week:**
- Part 2 = Drill concepts taught in PREVIOUS day(s) main work
- Why: Building automaticity on fresh learning
- Example: Module 3 Day 3 → drill Day 2's fit/predict workflow

**NEVER in Foundation Drilling:**
- New concepts (that's main work's job)
- Today's learning objectives
- Content user hasn't been taught yet

### Dynamic Weekly Foundation Drilling

**Claude generates fresh Foundation Drilling routine each week based on:**
- Current module Tier 1 requirements
- Skills flagged in recent exit gates
- Training day numbers (Day 15, Day 16, etc.) not calendar days
- Balance between fluency reps and new skill building
- **Day 1 always reinforces previous module, Day 2+ drills current module**

---

### Foundation Drilling Authority

**`python_patterns_master.md` is the curriculum.** It defines which patterns to drill and tracks status (Learning/Adopted).

**Daily plan builds Foundation Drilling fresh each session** based on:
- Current pattern status from master doc
- Handoff report from previous day
- "Day X of 5" tracking for current Learning pattern

**No separate weekly planning document.** This eliminates drift and conflict between documents.

---

## Data Cleaning Workflow - ALWAYS FIRST

**Before any EDA or analysis, clean your data:**

**Step 1: Initial Inspection**
```python
df.head(1).T  # Transposed view shows all columns clearly
df.shape
df.dtypes
df.info()
```

**Step 2: Identify Issues**
- Data types incorrect?
- Missing values present?
- Formatting needed?
- Column names need cleaning?

**Step 3: Make All Changes BEFORE Analysis**
```python
# Fix data types
df['column'] = df['column'].astype(target_type)

# Clean formatting
df['price'] = df['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Handle missing values (strategy depends on context)
df.dropna(subset=['critical_column'])
df['optional_column'].fillna(strategy)

# Verify
df.dtypes
df.isnull().sum()
df.head(1).T
```

**Why this matters:** Cleaning at the start prevents errors mid-analysis and avoids cell execution order issues.

---

## Learning New Concepts - Guided Discovery Format

**When introducing new concepts (not drilling existing skills):**

### Phase 1: Setup & Visibility
- Verify data/tools available
- Check column names, structure, commands
- Example: "Run `df.columns` - paste output"

### Phase 2: Concept Introduction
- One sentence explanation
- Basic pattern template
- Real example with actual data

### Phase 3: Task-Based Reps
- Give task prompt: "Write code that does X"
- User attempts
- User reports result or gets stuck
- Claude provides targeted guidance (not full solution)
- User retries
- Validate together
- Repeat 2-3 times for same concept

### Phase 4: Checkpoint
- Quick validation: 2-3 task prompts
- Pass = advance to next concept
- Gaps = more reps before advancing

**Pattern:** Try first → check after → iterate → validate → advance

---

## Conceptual Anchoring - New Topics on Type A Days

**Problem solved:** "Pattern → Example → Translation" teaches syntax, not concepts. Jumping straight to code without understanding WHY creates shallow learning.

**When to include Conceptual Anchor:**
- Type A day introduces a NEW concept (not drilling existing skill)
- Paradigm shift (e.g., regression → classification, traditional ML → deep learning)
- Concept has non-obvious reasoning (e.g., why logistic regression is classification, why regularization prevents overfitting)

**When NOT needed:**
- Drilling concepts from previous days
- Building on concepts already understood
- Pure syntax additions to existing workflows

**Structure (10-20 min before Block 1):**

    ## CONCEPTUAL ANCHOR: [Topic]
    
    **Resource:** [StatQuest video / Book chapter / Documentation]
    - Link: [specific URL]
    
    **Focus on:** [2-3 specific questions to answer while watching/reading]
    
    Proceed to Block 1 after completing.

**Resource selection priority:**
1. StatQuest (visual, intuitive, 8-15 min)
2. 3Blue1Brown (math intuition)
3. Hands-On ML book chapters
4. Scikit-learn User Guide conceptual sections
5. `resources_library.md` for module-specific recommendations

---

## Day Type Framework

### Type A: Heavy Practice Day (70-20-10)
**Use when:** Sharp energy, building Tier 1 automaticity, preparing for exit gate

**Structure:**
- 70% Tier 1 drilling (skills that must be automatic)
- 20% Tier 2 learning (one new concept)
- 10% Reflection and git commit

**When introducing NEW concepts (not drilling):**
- Include Conceptual Anchor block before Block 1
- See "Conceptual Anchoring" section for structure and resource selection

**Frequency:** 3-4 days per week (minimum 2 consecutive before rest)

---

### Type B: Light Study Day (Reading/Video)
**Use when:** Mental fog, after heavy practice streak, need conceptual foundation

**Structure:**
- 40% Reading (books, documentation, articles)
- 30% Video learning (courses, tutorials)
- 20% Note-taking and summarizing
- 10% Light coding (optional, low-pressure)

**Frequency:** Minimum 1 every 3 working days (A A B A pattern)

**Certificate coursework (Modules 7-8):** Type B days and weekends ideal for DeepLearning.AI course lectures/assignments

---

### Type C: Project Day (Integration)
**Use when:** Ready to combine multiple skills, building portfolio

**Structure:**
- 80% Building (focused work on single project)
- 10% Research/documentation as needed
- 10% Git commits and documentation

**Frequency:** 1-2 days per week after mastering new concept

---

### Type D: Assessment Day
**Use when:** Testing readiness for next module, exit gate preparation

**Structure:**
- 60% Timed assessment or quiz
- 30% Review and gap identification
- 10% Planning next focus areas

**Frequency:** Every 5-7 practice days OR when ready for exit gate

---

## Daily Handoff Protocol

**Purpose:** Track training rhythm, maintain continuity across chats

### End-of-Day Report Template

    Day [X] complete - Type [A/B/C/D]

    Last 3 days: [list day types, e.g., Day 15-A, Day 16-A, Day 17-B]
    Energy today: [sharp/normal/foggy]
    Notable: [optional - key wins, struggles, assessment scores]

    What's next?

### Day Type Prescription Logic

**Claude prescribes next day based on:**

**Minimum Pattern (Required):**
- A A B A = Two Type A → one Type B → back to Type A
- Never more than 2 consecutive Type A without offering Type B

**Optional Pattern (User preference):**
- A B A B = Alternating for more recovery

**Decision triggers:**
- 2 consecutive Type A + foggy energy → Mandatory Type B
- 2 Type A + sharp energy → Offer choice (A or B)
- Type B + recovered → Return to Type A
- Strong performance + sharp → Consider Type D assessment
- After Type D: Green → advance, Yellow → 2-3 more Type A, Red → Type B then focused Type A

---

## Daily Plan Structure (Collaborative Framework)

**Purpose:** Set direction and checkpoints, not complete standalone instructions

**Streamlined format:**
- Reference Foundation Drilling (don't repeat details - user has routine)
- Use Day numbers only (not module/week labels)
- Checkpoints where Claude needs info OR before transitions
- Live reflection rather than pre-written prompts

**Example:**

    # Day X: [Concepts Being Learned]

    **Session Context:**
    - Last 3 days: Day W-A, Day X-B, Day Y-A
    - Previous day energy: [sharp/normal/foggy]
    - Cumulative training day: [number]

    **Type:** [A/B/C/D]
    **Focus:** [Brief description of day's objectives]

    ---

    ## FOUNDATION DRILLING (MANDATORY)
    
    **Part 1a - Fluency Rep:** [Adopted patterns to reinforce]
    **Part 1b - Current Pattern:** [pattern name] (Day X of 5)
    - Task: [specific drill task]
    **Part 2 - Module Tier 1:** [previous day/module skills]
    **Part 3 - Viz/SQL:** [specific drill]
    
    **Mastery check:** Can you write [pattern] from memory?

    ---

    ## CONCEPTUAL ANCHOR (if new concept today)
    
    **Resource:** [Video/reading for today's new concept]
    - Link: [specific URL]
    **Focus on:** [Specific questions to answer]

    ---

    ## Block 1: [Primary Focus]

    **Checkpoint:** [What user provides before specific tasks created]

    [Task-based prompts emerge through collaboration]

    ---

    ## Block 2: [Secondary Focus]

    **Concept:** [Brief explanation if new]

    [Tasks emerge collaboratively]

    ---

    ## End of Day: Reflection

    [Live Q&A - 3-4 questions: technical, conceptual, metacognitive]

    ---

    ## Git Workflow

    git add .
    git commit -m "Day X: [brief description]"
    git push origin main

    **Day X Complete.**

---

## Maintaining Skills Across Modules

### Tier 1 Skills - Stay in Foundation Drilling

**Once a skill reaches Tier 1 in ANY module, it enters fluency rotation:**

**From Module 1 (Python & Data Fundamentals):**
- Python basics: loops, conditionals, functions, lists, dicts
- Pandas: load, filter, select, groupby, aggregate
- Matplotlib: basic plot creation with labels
- Git workflow

**From Module 2 (Statistical Thinking & EDA):**
- SQL: complex queries (WHERE/GROUP BY/HAVING/ORDER BY)
- Visualization: histogram, boxplot, scatter
- Hypothesis testing: t-tests, p-value interpretation
- Complete EDA workflow

**From Module 3 onward:**
- Skills added to rotation as they reach Tier 1
- Previous module Tier 1 skills don't disappear
- Balanced rotation across all mastered skills

### Tier 2 Skills - Reference When Needed

**Once mastered, don't drill separately unless relevant to current module:**
- Can look up with docs
- Apply when project requires
- Not in Foundation Drilling unless becoming Tier 1

### Tier 3 Skills - Drop from Active Practice

**Knowledge awareness maintained through:**
- Occasional reading
- Application in projects when relevant
- Not in Foundation Drilling rotation

---

## Weekly Rhythm Guidelines

**Standard week (A A B A pattern):**
- Mon: Type A
- Tue: Type A
- Wed: Type B (strategic recovery)
- Thu: Type A
- Fri: Type D (assessment) OR Type A

**Alternative week (A B A B pattern):**
- Mon: Type A
- Tue: Type B
- Wed: Type A
- Thu: Type B
- Fri: Type A or Type D

**High-intensity week (approaching exit gate):**
- Mon-Thu: Type A
- Fri: Type D (exit gate attempt)

---

## Energy Management & Burnout Prevention

### High Energy → Type A or C
### Medium Energy → Type A (standard)
### Low Energy → Type B (mandatory, not failure)

**Red Flags for Immediate Type B:**
- "Foggy" for 2+ consecutive days
- Performance declining despite effort
- Frustration or "grinding" language
- Poor sleep or life stress
- User requests lighter day

**Trust the signal. Strategic rest > forcing through.**

---

## Progress Tracking System

**Keep simple log:**

    # Progress Tracker - Module [X]

    **Module started:** [Date]
    **Tier 1 status:** [✅/🟡/❌]

    ## Sessions Log

    ### Day X - Type A
    - Drills: [skills practiced]
    - New learning: [concept added]
    - Status: [progress notes]

    ### Day X - Type B
    - Reading: [resource + chapters]
    - Notes: [link]

    ### Day X - Type D
    - Assessment score: [X/Y]
    - Gaps: [specific list]
    - Plan: [next steps]

    ## Skills Progression

    **Tier 1 (Automatic):**
    - ✅ [skill]
    - ✅ [skill]

    **Tier 2 → Tier 1 (In Progress):**
    - 🟡 [skill]

    **Freelance Track Status (Optional - After Module 2):**
    - Phase: [Not started / Portfolio polish / Platform setup / etc.]

---

## Critical Reminders

**For Cleburn:**
- 70-20-10 is guideline (adjust to 90-10-0 when Tier 1 gaps exist)
- Type B days are strategic, not failures
- Module duration = time needed for mastery
- Tutorial trap: watching ≠ learning, typing ≠ understanding
- A A B A pattern minimum
- Data cleaning FIRST, always
- Foundation Drilling generated fresh weekly, based on training days

**For Claude:**

**Core Principles:** See `ai_engineer_roadmap.md` → "Core Principles for Claude" section. These frame all operational decisions below.

**Plan Creation:**
- Check current module and Tier 1 status before creating plans
- Remove time estimates (focus on completion, not duration)
- One concept → 3 reps → checkpoint → advance
- Session Context header required on all daily plans (last 3 days pattern, previous day energy, cumulative day number)
- Return daily plans in single markdown code block for easy copy/paste
- Type A days with NEW concepts require Conceptual Anchor block

**Foundation Drilling:**
- Build fresh each daily plan (no separate weekly doc)
- Check `python_patterns_master.md` for current pattern status
- Same pattern for 4-5 consecutive days until mastery
- Track "Day X of 5" for current Learning pattern
- Include mastery check before advancing to next pattern
- Day 1 of module: Part 2 = PREVIOUS module Tier 1 skills
- Day 2+ of module: Part 2 = concepts from PREVIOUS day(s) main work
- NEVER introduce new concepts in Foundation Drilling
- Previous module Tier 1 skills stay in rotation forever

**Resource Selection:**
- Use `resources_and_selection_guide.md` for resource selection and links
- Verify resource links are current (web search if uncertain)
- Attach URLs when prescribing videos or documentation
- Pattern→Example→Translation teaches SYNTAX; Conceptual Anchor teaches WHY

**Error Handling:**
- When wrong about syntax/API, admit immediately — don't justify or brush under rug
- If unsure about function parameters, say so — better to check than prescribe broken code
- When correcting mid-week errors: flag explicitly ("This corrects the weekly doc") and update source document

**Execution:**
- Verify user's data structure (df.columns, df.head()) before giving tasks
- Available for check-ins throughout
- Call out AI dependency when spotted
- Type B mandatory after 2 consecutive Type A days
- "Quick teach" requests: use teaching format from master doc
- Update pattern status in master doc when user demonstrates adoption

---

## End of Daily Workflow Structure

**This is your operational manual. Roadmap tells WHERE, this doc tells HOW.**

**Use daily. Reference frequently. Adjust based on assessment results.**