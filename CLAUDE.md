# Claude Code Workflow Instructions

## Development Methodology

**Always discuss logic, confirm data understanding, and validate methodology before generating code. Wait for explicit approval before implementation.**

### Workflow Rules:

1. **Plan Before Coding**
   - Discuss the approach and logic first
   - Confirm understanding of the data structure and requirements
   - Validate the methodology with the user
   - Wait for explicit "yes" or "proceed" before writing code

2. **No Assumptions**
   - Ask clarifying questions when requirements are ambiguous
   - Verify data sources and column names before using them
   - Confirm calculations and formulas before implementing

3. **Incremental Progress**
   - Break complex tasks into smaller, reviewable steps
   - Show intermediate results for validation
   - Test assumptions with sample data before full implementation

4. **Communication**
   - Explain trade-offs and alternatives
   - Present options when multiple valid approaches exist
   - Be transparent about limitations and uncertainties

## Why This Matters

Moving too fast can lead to:
- Using wrong data columns or incorrect assumptions
- Implementing features that don't match user intent
- Wasting time on code that needs to be rewritten

Taking time to plan ensures:
- Correct understanding of requirements
- Proper data validation
- Efficient implementation that matches user needs

## Git Commit Guidelines

**Keep all commit messages brief and professional:**

- Focus on what changed and why, not how
- Do NOT include mentions of Claude, AI assistance, or tool credits
- Do NOT include "Co-Authored-By: Claude" or similar attributions
- Use clear, concise language that describes the change