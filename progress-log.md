# Progress Log

## 2025-05-17

- Learned the conceptual difference between Docker Image (like a class) and Container (like an instance).
- Understood why devcontainers in VS Code trigger `docker build` automatically.
- Learned that Docker containers and images accumulate and consume disk space if not cleaned.

## 2025-05-18

- Solved LeetCode #1 Two Sum and fully understood hash map approach.
- Felt very sleepy, so postponed the second problem to tomorrow. (#20 Valid Parentheses)

## 2025-05-19

- ✅ Solved LeetCode #20: Valid Parentheses  
  - Used a stack to match open and close brackets.  
  - Realized it's very similar to MTG’s stack resolution—LIFO behavior.  
  - Code became elegant (possibly AI-influenced), but I fully understood the logic.  
  - `return not stack` means all open brackets have been matched and removed. 
  - I learned LIFO behavior by coding and could image clearly than before.

## 2025-05-20

### 🧠 LeetCode

- ✅ Solved LeetCode #121: Best Time to Buy and Sell Stock  
  - Explored multiple strategies, and chose the cleanest O(n) solution using a min_price tracker.  
- 🎯 Reached the third LeetCode goal for Week 1  
- 🧠 Deeply reflected on efficiency vs readability and testability  
  - Simple is best.（結局、シンプルが最強。）  
  - 凝ったロジックよりも、わかりやすさ・テストしやすさが実務では勝る。

### 🐳 Docker

- ✅ Resolved Docker Desktop issues via reinstallation  
- ✅ Successfully built and ran Docker container with custom main.py  
  - Output confirmed: "Hello, Docker!"
  - First hands-on Docker experience achieved. Container basics now understood.
  - Simple is best. One small build for a container, one giant leap for reproducibility.