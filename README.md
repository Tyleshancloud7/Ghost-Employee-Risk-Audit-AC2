# Ghost Employee Risk Audit – AC-2 Demo

Check out the demo video here:  
[Watch Demo](https://www.loom.com/share/5f09774b90c24f5c872a270d294060fb)

  add README.md
git commit -m "Add Loom demo link to README"
git push origin main

git add README.md
git commit -m "Polished README with Loom demo and badges"
git push origin main



git add README.md
git commit -m "Add Loom demo link to README"
git push origin main

git add README.md
git commit -m "Polished README with Loom demo and badges"
git push origin main

nano README.md

nh# Ghost Employee Risk Audit – AC-2 Control Implementation

> Kill ghost accounts before they haunt your company 👻💻  
> Operationalized insider access risk audit built on NIST SP 800-53 AC-2

## The Real Problem Companies Face

Ever terminated an employee only to find they still have access to:

- Slack  
- Salesforce  
- AWS console  
- Shared Google Drives  
- Admin privileges  

3 months later…  
👻 They log in.  
👻 Download client lists.  
👻 Potentially leak sensitive data.  

This is the **Ghost Employee Problem**, and it happens in almost every company without automated account management.

## Project Overview

This project demonstrates how to operationalize **AC-2 Account Management** from **NIST SP 800-53**, while also mapping to **ISO/IEC 27001 Annex A** and **ISO/IEC 27002 guidance**.

**Key Goals:**

1. Identify risks from inactive or ghost accounts  
2. Map AC-2 requirements to real-world processes  
3. Track evidence for audits  
4. Build a remediation roadmap  
5. Create a maturity dashboard to measure progress

All outputs are **auditor-ready** and **executive-friendly**.

## Solution Snapshot

**Workbook / Dashboard Tabs:**

| Tab | Purpose |
|-----|--------|
| Risk Register | Identify ghost accounts & quantify risk |
| Control Mapping | Break down AC-2 requirements into actionable tasks |
| Audit Testing | Track termination SLA compliance |
| Evidence Samples | Maintain proof of controls for audit |
| Remediation Roadmap | Plan automation & process fixes |
| Maturity Dashboard | Visualize current vs. target control effectiveness |

**Example: Risk Register Snapshot**

| Employee | System | Terminated? | Access Disabled? | SLA Met? | Risk Level |
|----------|--------|------------|----------------|----------|------------|
| John D | Salesforce | ✅ | ❌ | ❌ | High 🔥 |
| Maria L | AWS | ✅ | ✅ | ✅ | Low ✅ |
| Ex-Sales Mgr | Slack | ✅ | ❌ | ❌ | Critical 💀 |

## How It Works

1. **Identify Risks:** Pull terminated employee list from HRIS  
2. **Map Controls:** Compare each system against AC-2 requirements  
3. **Audit & Evidence:** Check if access was disabled within 24h, document exceptions  
4. **Remediate:** Implement IAM automation, enforce quarterly reviews  
5. **Report:** Generate executive dashboards and maturity scorecards  

This simulates **real-world insider threat mitigation** while demonstrating GRC expertise.

## Maturity Assessment & Remediation Roadmap

**AC-2 Maturity Levels**

| Level | Description |
|-------|------------|
| 1 | Manual offboarding emails |
| 2 | Spreadsheet tracking |
| 3 | Ticket-based workflow |
| 4 | Automated IAM integration |
| 5 | Continuous monitoring & analytics |

**Current State:** 2  
**Target State:** 4

**Remediation Phases:**

- **Phase 1 – Immediate:** Define 24-hour SLA, eliminate shared admin accounts  
- **Phase 2 – Process Integration:** HRIS → ITSM workflow trigger, central account inventory  
- **Phase 3 – Automation:** IAM lifecycle management, auto-disable inactive accounts, privileged access certification

## Why Recruiters Will Stop Scrolling

- Demonstrates **real operationalization** of GRC controls  
- Shows **risk → control → evidence → remediation workflow**  
- Includes **automation & simulation potential**  
- Maps **NIST AC-2 to ISO frameworks**  
- Fun + me

