# Lauren Tan: How to Trust AI Coding Agents (content extract)

- **Video:** "Lauren Tan workshop XAi Grokbot", https://youtu.be/ONeM6YDmvqA
- **Uploader:** AI Agents for Business (a re-upload; the original session is a Maven workshop, "How Cursor turned AI agents into better engineers")
- **Length:** about 50 minutes. 129K views. Posted Sep 11, 2026.
- **Source:** the full auto-generated English transcript, read end to end. Auto-captions misspell some names; the spellings below are corrected.

## Speaker

Lauren Tan ("potatoe" on X). Engineer at Cursor for about 5 months. Before that she was on the React compiler team at Meta, and a tech lead and then an engineering manager at Netflix.

## Big idea

**You can only scale AI agents as far as you trust them.** Managing agents works like managing people. If you don't trust them, you micromanage, and you can't run many at once.

## Key points

1. **The trust curve.** At first you watch every output of one or two agents. As trust grows, you run more agents in parallel. Lauren now lets her agents auto-merge pull requests. She woke up to 20 merged PRs, checked them, and found them good.
2. **The numbers.** She shipped about 1,000 PRs last month, and about 800 by the 12th of this month. Her output rose as her trust grew.
3. **Verification is the most important skill.** Let the agent run the real app, take performance traces and test the result itself. Otherwise you become the bottleneck, pasting screenshots and errors back and forth. Verification doesn't promise good code, but it does give correct code.
4. **The feature map.** Her verification skill ships with a file that tells the agent where every feature lives and how to reach it in the app. With it, even a vague bug report ("a screenshot and ???") makes sense to the agent.
5. **Turn every failure into a skill.** She built her plugin, pstack, one skill at a time. Each time an agent failed (guessing, hallucinating, not reading the code), she wrote a skill to stop it. A new agent is like a skilled hire with zero business context; skills are the onboarding.
6. **Test your skills with evals.** An eval is a unit test for an agent. She has a lead agent write a rubric, spawn sub-agents in neutral folders (agents act differently when they know they're being tested), score the results, and check the score with a judge on a different model. Then she loops until every score is 10/10.
7. **The head-chef analogy.** The engineer no longer cooks every dish. She designs the kitchen, sets up the stations and hands out the tasks.
8. **Start local, then go to the cloud.** Build trust by watching agents on your own machine first. Then move to cloud agents. Her bug agent, "Benny," takes each bug report, reproduces it on its own computer and reports back. In one case it found the bug was already fixed. The whole team benefits.
9. **Don't jump ahead.** Spawning hundreds of agents before you trust one just burns tokens.
10. **Vibe-coded apps need strict rules.** With no guardrails, agents take the shortest path and the codebase spirals. She spent 600+ PRs moving Grok Bot to a strict architecture (code name "Dune"). Now she rarely reads the code.
11. **Make the shortest path the right path.** Agents love shortcuts and copy existing patterns, so design the codebase so that the easy way is also the correct way.
12. **Hard rules beat soft rules.** Hard: architecture, CI checks, lint rules, compiler errors. These turn the build red. Soft: rules files, skills, style guides, AI code review. Agents can forget soft rules. Her CI bans `useEffect`, bans code comments, and blocks imports across the Electron main and renderer folders.
13. **Every code-review comment is a warning sign.** If you keep writing "don't do this" on PRs, turn it into a lint rule or a CI failure instead.
14. **Small, atomic PRs.** Git history is rich context, and small PRs are easy to revert.
15. **Tokens are an ROI question.** Setup costs a lot of tokens up front. It pays back when even small models write good code, and when PMs, designers and GTM staff can ship safely.
16. **Non-engineers ship too.** Grok Bot looks like iMessage. PMs use agents to summarize the night's work, and they send in fixes that get approved as-is.

## Quotable lines

- "When you don't have much trust in your agents, you really can't get the most out of them."
- "If you don't have a verification skill, you are the verifier. You're the bottleneck."
- "Before AI slop, we had human slop."
- "The shortest path is the best path."
- "Every time you have to [enforce a rule in code review], you should consider that a code smell."
- "Agents are all about allowing you to do things that you couldn't do before."

## Possible post angles

- **Leadership:** managing AI agents is managing people; trust decides how far you scale.
- **Career/skills:** your new job is head chef, not line cook.
- **Practical:** 3 steps to trusting AI: verify locally, encode failures as skills, then go to the cloud.
- **Contrarian:** stop reviewing code; turn review comments into rules.
- **Business:** why spending tokens up front can beat hiring.
