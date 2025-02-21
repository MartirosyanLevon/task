## 📌 Prerequisites
Before running tests, ensure you have:
- Python **3.8+** installed
- Required dependencies installed:
  ```sh
  pip install -r requirements.txt


~~📌 Locust Performance Testing for User Registration & Login

This project uses Locust to perform load testing on the Cinema API endpoints:

User Registration: /user/register

User Login: /user/login

🚀 Setup & Installation

1️⃣ Install Dependencies

Ensure you have Python 3.7+ installed, then run:

pip install locust faker

2️⃣ Create locustfile.py

Make sure the locustfile.py is placed in your project directory.

3️⃣ Run Locust (With UI)

locust -f locustfile.py 

Opens Locust Web UI at http://localhost:8089

Enter Number of Users & Spawn Rate, then start the test.


4️⃣ Run Locust (Headless Mode)

For automated command-line execution:

locust -f locustfile.py --host=https://cinema.xdatagroup.dev/api/v1/cinema -u 10 -r 2 --headless --run-time 1m

-u 10 → Simulates 10 concurrent users

-r 2 → Spawns 2 new users per second

--headless → Runs without UI

--run-time 1m → Runs for 1 minute



