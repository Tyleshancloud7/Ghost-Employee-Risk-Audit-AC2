# Termination SLA Audit Testing

1. Pull terminated employees from HRIS (last 90 days)
2. Compare against Active Directory
3. Validate disablement timestamp
4. Document exceptions
5. Escalate deviations

| Employee | Termination Date | Disabled Date | Within SLA? | Notes |
|----------|-----------------|--------------|------------|-------|
| John D | Feb 1 | Feb 5 | ❌ | Late by 4 days |
| Maria L | Feb 3 | Feb 3 | ✅ | On time |
| Ex-Sales Mgr | Dec 1 | Dec 10 | ❌ | Escalated |
