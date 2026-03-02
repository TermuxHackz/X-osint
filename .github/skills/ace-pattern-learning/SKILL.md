---
name: ace-pattern-learning
description: "Search ACE playbook before implementing, building, fixing, debugging, or refactoring code. Capture patterns after completing substantial coding work."
---
<!-- ACE_SECTION v0.4.18 -->
# ACE Pattern Learning Skill

This skill provides pattern-based learning for coding tasks.

## When This Skill Activates

Copilot will automatically load this skill when your request contains:
- **Implementation**: implement, build, create, add, develop, write
- **Modification**: update, modify, change, edit, enhance, extend
- **Debugging**: debug, fix, troubleshoot, resolve, diagnose
- **Refactoring**: refactor, optimize, improve, restructure
- **Integration**: integrate, connect, setup, configure

## BEFORE Starting Work (MANDATORY)

**INVOKE**: `#ce-dot-net.ace-vscode/ace_search` with relevant query

Search for patterns from previous work before implementing:
- Proven solutions and best practices
- Known gotchas and pitfalls to avoid
- Recommended APIs and libraries

## AFTER Completing Work (MANDATORY)

**INVOKE**: `#ce-dot-net.ace-vscode/ace_learn` with:
- `task`: Brief description of what was accomplished
- `success`: true/false
- `output`: Key lessons, patterns discovered, gotchas

**DO NOT skip this step. DO NOT respond to user without calling ace_learn first.**

## Mid-Conversation Re-Search

If user's follow-up message introduces a NEW topic or domain:
1. Recognize topic shift (auth→caching, API→database, etc.)
2. Call ace_search with the new topic BEFORE continuing
3. Apply newly retrieved patterns

**Examples of topic shifts requiring re-search:**
- "Now let's add caching" (after auth implementation)
- "I'm getting a database error" (after API work)
- "How do I deploy this?" (after coding)
- "Let's add tests" (after implementation)
- "Now handle the error cases" (new domain)

## Domain-Filtered Search (v0.4.18)

After topic change detection, use domain filtering for targeted retrieval:

1. **List domains**: `/domains` to see available domains
2. **Match topic to domain**: Find domain name matching new topic
3. **Filtered search**: `ace_search <query> allowed_domains=<domain>`

## Example Workflow (with Domain Filtering)

```
User: "implement JWT authentication"
    ↓
1. ace_search("JWT authentication") → Find patterns
2. Implement using patterns found
3. ace_learn(task="Implemented JWT auth", success=true, output="Used refresh token rotation")
4. Respond to user

User: "Now add Redis caching for the tokens"
    ↓
1. [Topic shift detected: auth → caching]
2. /domains → sees available domains
3. ace_search("Redis caching" allowed_domains="caching,redis") → Targeted patterns
4. Implement caching using patterns found
5. ace_learn(task="Added Redis token caching", success=true, output="Used TTL matching token expiry")
6. Respond to user
```
<!-- ACE_SECTION_END -->
