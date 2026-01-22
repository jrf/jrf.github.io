---
title: "prompt"
---

Here are practical ways to prompt the agents:

Direct Task Requests

Parse exercises from a book:
Parse the exercises from "Understanding Analysis.md" and identify which ones can be formalized in Lean

Formalize a specific exercise:
Formalize Exercise 1.2.5 (De Morgan's Laws) from Understanding Analysis into Lean 4

Work through a section:
Work through Section 1.2 of Understanding Analysis and create Lean proofs for all exercises that have worked
solutions

Workflow-Oriented Prompts

Start a formalization session:
I want to formalize exercises from Understanding Analysis. Start with Section 1.3 - show me what exercises are
there and which can be formalized.

Continue existing work:
What exercises from Understanding Analysis still need to be formalized? Pick the next one and create a Lean
proof.

Check progress:
Run `just list` and `just incomplete` to show the current formalization status

Specific Examples
┌─────────────────┬───────────────────────────────────────────────────────────────────────────────┐
│      Goal       │                                    Prompt                                     │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ Single exercise │ "Formalize Exercise 2.3.1 from Understanding Analysis"                        │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ Batch work      │ "Formalize all the set theory exercises in Section 1.2"                       │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ Investigate     │ "What Mathlib lemmas would help prove the triangle inequality?"               │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ Debug           │ "The proof for S1_2_5 isn't compiling - help me fix it"                       │
├─────────────────┼───────────────────────────────────────────────────────────────────────────────┤
│ New book        │ "Set up formalization for Linear Algebra Done Right and start with Chapter 1" │
└─────────────────┴───────────────────────────────────────────────────────────────────────────────┘
The agents provide context, but you drive the work by describing what you want formalized. The more specific you are about which exercise and what approach to take, the better.
