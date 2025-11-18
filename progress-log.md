# Progress Log
## **2025-11-17**
### AI agent dev
- No progress today due to overworking at the office. 

## **2025-11-09**

### 🧠 LeetCode
- ✅ Solved LeetCode #9: Palindrome Number – Added via GitHub Actions.
- ✅ Solved LeetCode #13: Roman To Integer – Added via GitHub Actions.


## **2025-06-18**

### 🧠 LeetCode
- ✅ Solved LeetCode #1046: Last Stone Weight – Added via GitHub Actions.
- ✅ Solved LeetCode #104: Maximum Depth Of Binary Tree – Added via GitHub Actions.
- ✅ Solved LeetCode #141: Linked List – Added via GitHub Actions.
- ✅ Solved LeetCode #242: Valid Anagram – Added via GitHub Actions.

### 🐳 GitHub Actions
- ✅ Updated the `update_progress_log.py` script to insert new logs **below** the `# Progress Log` title, as requested.
- ✅ Extended support for `leetcode/medium` and `leetcode/hard` directories (previously only `easy/` was supported).
- ✅ Implemented duplicate detection to skip logging files already recorded in `progress-log.md`.
- ✅ Learned and executed `git pull origin main --rebase` to avoid merge conflicts when local progress is behind.
- ✅ Diagnosed a push failure in GitHub Actions due to insufficient permissions.
- ✅ Corrected the root cause by setting `Workflow permissions` to `Read and write permissions` under repository settings.
- 🧠 Learned that this is essential for enabling GitHub Actions to push updates to `progress-log.md`.


## **2025-06-11**

### 🧠 LeetCode
- ✅ Solved LeetCode #53: Maximum Subarray
- Learned Kadane’s Algorithm and how to track max subarray sum dynamically.

### 🐳 GitHub Actions
- ✅ Drafted logic for detecting new LeetCode files and updating progress-log.md.
- Planned the update script and decided on workflow trigger conditions.


## **2025-06-10**

### 🧠 LeetCode
- ✅ Solved LeetCode #0217: Contains Duplicate
  - Used `set()` to detect duplicates efficiently in O(n) time.
    - Used `set()` because it can be remove duplicates.
  - Learned the benefit of using set for quick membership checks.
- ✅ Solved LeetCode #0383: Ransom Note
  - Applied `collections.Counter` to compare character frequencies.
    - Used `collections.Counter` because the key is the needs of use letters from the magazine to ransom Note.
    - This problem can be solved if we can confirm that the number of occurrencies of each letter is also in magazine.
  - Understood how to subtract one Counter from another and use the result to determine feasibility.


## **2025-06-05**

### 🧠 LeetCode
- ✅ Solved LeetCode #136: Single Number
- Learned the power of XOR: same numbers cancel each other out, leaving the unique number.
- Impressed by how XOR enables constant space and O(n) time solution.

### 🐳 Docker / DevOps
- (No updates today)

## **2025-06-03**

### 🧠 LeetCode
- ✅ Solved LeetCode #35: Search Insert Position
- **GitHub**: [0035_search_insert_position.py](https://github.com/isms01/backend-evolve/blob/main/leetcode/easy/0035_search_insert_position.py)
- **What I learned**:
  - Practiced binary search and edge handling (e.g., inserting before/after all elements).
  - Used loop-based and bisect-based approaches.
  - Realized the importance of handling sorted input efficiently (O(log n)).

### 🐳 Docker
- ✅ Ran `docker run -it python:3.10` to enter interactive Python shell
- ✅ Mounted host directory and executed a Python script:
  ```bash
  docker run -it -v $(pwd):/app -w /app python:3.10 python hello.py
- What I learned
  - What containers and images are, and how to launch lightweight dev environments.


## **2025-05-29**

### 🧠 LeetCode
- ✅ Solved LeetCode #746: Min Cost Climbing Stairs
- Implemented a dynamic programming solution using an array.
- Compared with an optimized solution using two variables (`prev1`, `prev2`) instead of a full array.
- Learned the trade-off between memory usage and readability. Constant space DP is elegant and efficient.

### 🐳 Docker / GitHub
- 🤒 No code updates due to feeling unwell.
- Only updated the progress log for the day.


## **2025-05-27** (Midnight)

### 🧠 LeetCode
- ✅ Solved LeetCode #509: Fibonacci Number
- Implemented a clean recursive solution with base cases for 0 and 1.
- ✅ Solved LeetCode #1137: N-th Tribonacci Number
- Initially encountered TLE using naive recursion.
- Resolved the issue by applying `@lru_cache(maxsize=None)` to memoize previously computed results.
- Deepened understanding of:
  - Recursive function structure with base case and decomposition
  - Exponential time complexity and how caching mitigates it
  - Python’s `@lru_cache` and its internal hash-based caching mechanism

### 🐳 Docker / Backend-evolve
- 💡 Decided to use pandas DataFrame to manage event data in memory
- 💾 Chose JSON format as the persistent storage format
- Planned: read/write integration with `pandas.read_json()` / `to_json()` and CLI interface enhancements


## **2025-05-27** 

### 🧠 LeetCode
- ✅ Solved LeetCode #412: Fizz Buzz
- Used a boolean flag and string concatenation to produce "Fizz", "Buzz", or "FizzBuzz" based on divisibility.
- Reinforced control flow basics with conditional checks and list appending.

### 🐳 Docker / Backend-evolve
- ✅ Created `scheduler.py` with `Scheduler` class to add and list events
- ✅ Implemented `main.py` CLI loop to register schedule input (e.g., "2025-05-31 Watch movie GodFather")
- ✅ Handled input errors with `try-except` blocks, including ValueError and EOFError
- ✅ Understood `f-string` pitfalls with quote usage and resolved syntax error
- ✅ Ran program via `python -m app.main` successfully
- Learned:
  - How to parse and split user input
  - How to gracefully handle runtime interruptions (EOFError)
  - Why Python CLI apps need error tolerance and safe exit handling


## **2025-05-26**

### 🧠 LeetCode
- ✅ Solved LeetCode #1672: Richest Customer Wealth  
  [🔗 Submission Link](https://leetcode.com/problems/richest-customer-wealth/submissions/1644168345/)
- Practiced nested loops and max value tracking across rows in a 2D list.

### 🐳 Docker
- ✅ Added `ENV APP_ENV=development` to Dockerfile
- ✅ Modified `main.py` to print current environment from `os.environ`
- Verified environment-specific behavior:
  - On local execution, defaulted to `"production"` mode
  - On Docker container execution, showed `"development"` mode as set in Dockerfile
- Understood path resolution differences between local and container environments:
  - `main.py` is located at `/app`, so direct `python main.py` works inside the container


## **2025-05-25**

### 🧠 LeetCode
- ✅ Organized and committed LeetCode #283: Move Zeroes
- Reflected on the technique: Two-Pointer Compaction
  - Shift non-zero elements forward while maintaining their order
  - Fill the remaining positions with zeroes
  - In-place operation with O(n) time and O(1) space
- Clearly understood the technique and explained it in my own words
  > “Skip zeros, shift non-zero values forward, then zero-fill”

### 🐳 Docker
- Confirm ENV command to change environment variable value

### 💡 Key Takeaways
- Not just solving the problem, but understanding *why* it works and *when* to use it
- Writing and organizing knowledge improves clarity and recall
- Keeping a single `progress-log.md` file makes daily tracking more efficient

### ✅ Next step
- Solve LeetCode #1672 and reflect on the `sum-max for 2D list` pattern



## **2025-05-22**

### 🧠 LeetCode
- ✅ Solved LeetCode #88: Merge Sorted Array
- Learned the difference between `sorted(nums1)` (non-destructive) and `nums1.sort()` (in-place).
- Realized that `sorted()` does not modify the original list, which caused the LeetCode checker to fail the result.
- Discussed and explored Timsort, the algorithm behind `sorted()`, and gained a better understanding of how Python sorts work.


### 🐳 Docker
- ✅ Edited the Dockerfile to include a new `RUN echo` step.
- Rebuilt the image and confirmed that `/echo_test.txt` exists within the container.
- Understood the difference between Docker image and container state:
  - Files created during `docker build` persist in all containers spawned from the image.
  - Changes inside a running container do not persist unless the container is kept alive or committed.
- ✅ Learned the correct development workflow:
  - Use `docker run` once to start a container
  - Use `docker exec` for further access to that same container without restarting


## **2025-05-21**

### 🧠 LeetCode
- ✅ Solved LeetCode #125: Valid Palindrome
  - Cleaned and normalized input string
  - Used slicing and alphanumeric filtering to verify palindrome
  - Learned about generator expressions and `[::-1]` slicing
  - Simple is best. Pythonic and elegant.

### 🐳 Docker
- No new changes today. Environment verified yesterday.

## **2025-05-20**

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

## **2025-05-19**

- ✅ Solved LeetCode #20: Valid Parentheses  
  - Used a stack to match open and close brackets.  
  - Realized it's very similar to MTG’s stack resolution—LIFO behavior.  
  - Code became elegant (possibly AI-influenced), but I fully understood the logic.  
  - `return not stack` means all open brackets have been matched and removed. 
  - I learned LIFO behavior by coding and could image clearly than before.

## **2025-05-18**

- Solved LeetCode #1 Two Sum and fully understood hash map approach.
- Felt very sleepy, so postponed the second problem to tomorrow. (#20 Valid Parentheses)

## **2025-05-17**

- Learned the conceptual difference between Docker Image (like a class) and Container (like an instance).
- Understood why devcontainers in VS Code trigger `docker build` automatically.
- Learned that Docker containers and images accumulate and consume disk space if not cleaned.

