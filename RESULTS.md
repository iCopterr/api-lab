# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: The Purple Capricciosa
- Step 0.12, results of the three runs without a session (optional):
  - Run 1: FAILED (login returned HTTP 401 instead of 200)
  - Run 2: FAILED (login returned HTTP 401 instead of 200)
  - Run 3: FAILED (login returned HTTP 401 instead of 200)
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, and 3 tools excluded.

## Defect report

- Title: Excluding all available tools causes an internal server error.
- Request: POST /api/pizza with excludedTools containing Knife, Pizza cutter, and Scissors.
- Expected result: HTTP 400 with a JSON error message explaining that no tools are available.
- Actual result: HTTP 500 with an empty response body.
- Severity: Medium — the API fails to handle an invalid input gracefully.

## Part A

- Step A4, status codes when the other user reads, changes and deletes:
  - GET: 400 
  - PUT: 404  
  - DELETE: 404
  
  ## Part B

1. To be completed
2. To be completed
3. To be completed
4. To be completed
5. To be completed
6. To be completed
7. To be completed
8. To be completed
