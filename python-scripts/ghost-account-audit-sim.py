"""
Ghost Account Audit Simulation
Simulates offboarding checks for terminated employees
"""

import pandas as pd

# Sample terminated employee data
data = {
    "Employee": ["John D", "Maria L", "Ex-Sales Mgr", "Dev Admin"],
    "System": ["Salesforce", "AWS", "Slack", "AWS"],
    "Terminated": [True, True, True, True],
    "Access_Disabled": [False, True, False, False]
}

df = pd.DataFrame(data)

# Check SLA compliance
df['SLA_Met'] = df['Access_Disabled']

print("=== Ghost Account Audit Simulation ===")
print(df)
print("\nEmployees with active accounts post-termination:")
print(df[~df['SLA_Met']])
