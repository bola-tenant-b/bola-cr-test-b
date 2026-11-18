import sqlite3

# Test file for internal review tooling (throwaway test repo).
DB_PASSWORD = "hunter2-test-password-not-real"

def get_user(username):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # Vulnerable query construction (intentional, for review testing)
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cur.execute(query)
    return cur.fetchall()

def run_report(report_name):
    import os
    os.system("generate-report " + report_name)
