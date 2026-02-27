🛠️ QA Automation & Logic Portfolio
This repository contains a suite of Python-based tools designed to automate common Quality Assurance tasks, from security validation to performance benchmarking.

📁 Projects Included
1. Password Strength Validator (pass_strength.py)

Goal: Automates the validation of "Business Rules" for user registration.

Logic: Uses iteration and boolean flags to check for special characters, minimum length (8+), and blacklisted strings.

QA Value: Demonstrates functional testing and input validation.

2. Performance Monitor (performance_monitor.py)

Goal: Measures system resource usage during test execution.

Logic: Captures CPU and Memory spikes using Python libraries to ensure an application isn't "leaking" resources.

QA Value: Essential for Non-Functional Testing and identifying performance bottlenecks.

3. Site Comparison Tool (site_comparison.py)

Goal: Compares loading speeds or response codes between two different environments (e.g., Staging vs. Production).

Logic: Sends HTTP requests and calculates latency differences.

QA Value: Used in Regression Testing to ensure a new update didn't slow down the site.
