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

1. API tests can find connection problems and errors between the server and database. Unit tests with stubs may not find these problems. However, unit tests are still useful because they are faster and easier to debug.

2. We create a new user for each test to make sure the tests don't affect each other. Using the public token could cause problems if other people use it too. In Project 2, I will create separate test data for each test.

3. We use the same session to keep cookies between requests. Without a session, the server might not recognize the user when logging in. In Step 0.12, all three runs failed with HTTP 401.

4. The defect happened when all 3 tools were excluded. HTTP 500 with an empty body is worse because the client doesn't know what went wrong. We keep the test as xfail so we can check if the bug gets fixed later.

5. Base choice coverage needs 9 tests (1 + 2 + 3 + 1 + 2). All combinations coverage needs 72 tests (3 × 4 × 2 × 3). Base choice uses fewer tests while still covering every input block.

6. I got 400 for GET, 404 for PUT, and 404 for DELETE. I would expect 403 because the user doesn't have permission. The API still blocks access, so I don't think it is a serious defect, but the status codes could be more consistent.

7. I got HTTP 200 OK and a list of ratings, even though I used a made-up token. I think this is a security problem because someone could read ratings without logging in. In a real system, this could expose private data.

8. API tests are better for checking status codes and JSON responses. Web page tests are better for checking the UI and whether users can interact with the website correctly.
