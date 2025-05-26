# Progress Log

## **2025-05-27**

### 🧠 LeetCode
- ✅ Solved LeetCode #412: Fizz Buzz
- Used boolean flag to avoid else logic; added "Fizz"/"Buzz" using string concatenation.
- Learned to build up output step by step and handle multiple conditions cleanly.

### 🐳 Docker
- [ ] (Planned) Create `scheduler.py` with basic Scheduler class
- [ ] (Planned) Add CLI input in `main.py` to register a simple schedule


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

