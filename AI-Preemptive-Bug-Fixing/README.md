# AI: Preemptive Bug Fixing

## Objective
To analyze and fix logical and memory safety issues in a C linked list function using AI.

## AI Tool Used
ChatGPT

## Issues Found
- Incorrect linked list traversal logic
- Missing malloc NULL check
- Memory leak risk

## Fixes Applied
- Fixed traversal using current->next
- Added NULL check after malloc
- Properly linked new node to list

## Outcome
The function now safely adds a node at the end of a singly linked list without memory errors.
