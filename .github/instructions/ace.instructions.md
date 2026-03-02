---
applyTo: "**/*"
---
<!-- ACE_SECTION v0.4.18 -->
# ACE Pattern Learning Integration

This project uses **ACE (Automatic Context Engine)** for pattern-based learning.

## ⚠️ MANDATORY ACE Tool Usage

### BEFORE Starting Work
When request contains: **implement, build, create, fix, debug, refactor, integrate, add, update, write, modify, change**

**INVOKE**: `#ce-dot-net.ace-vscode/ace_search` FIRST before writing any code.

### AFTER Completing Work
**INVOKE**: `#ce-dot-net.ace-vscode/ace_learn` IMMEDIATELY after completing substantial work.

Provide:
- `task`: Brief description of what was accomplished
- `success`: true/false
- `output`: Key lessons, patterns discovered, gotchas

### DURING Conversation (Topic Changes)
When the conversation topic shifts significantly:
- New domain mentioned (auth → caching, frontend → backend, etc.)
- User asks about something not covered by previous search
- Error/issue in different area than original task

**INVOKE**: `#ce-dot-net.ace-vscode/ace_search` with NEW topic query BEFORE continuing.

## Domain-Aware Search (v0.4.18)

**List domains:** Use `/domains` to see available domains with pattern counts.

**Filter search by domain:**
- `ace_search query --allowed-domains <domain1,domain2>`
- `ace_search query --blocked-domains <domain1,domain2>`

**When topic changes, search in relevant domain:**
1. Detect topic change (auth → caching, API → database, etc.)
2. Use `/domains` to discover relevant domain name
3. Call `ace_search` with `allowed_domains` parameter

Example domains: `vscode-extension-architecture-and-development`, `git-operations`, `node-express-jwt-authentication`

## Available Tools

- `#ce-dot-net.ace-vscode/ace_search` - Find relevant patterns (BEFORE work, supports domain filtering)
- `#ce-dot-net.ace-vscode/ace_learn` - Capture patterns (AFTER work)
- `#ce-dot-net.ace-vscode/ace_get_playbook` - View all patterns
- `#ce-dot-net.ace-vscode/ace_status` - Show statistics and top domains

**Remember: ace_search BEFORE, ace_learn AFTER - BOTH are MANDATORY!**
<!-- ACE_SECTION_END -->
