# Freshworks Issue Tracking & Security Workflow

## 1. Issue Tracking Lifecycle
* **Ticket Creation**: All project tasks, feature requests, and bug reports must be created as tickets in Freshworks before work begins.
* **Assignment & Prioritization**: Tickets are assigned to team members and categorized by priority (Low, Medium, High, Critical).
* **Status Transitions**: Tickets move through standard stages: `Open` -> `In Progress` -> `In Review` -> `Resolved`.
* **Git Commit Linking**: Commits must reference their corresponding Freshworks ticket ID in the commit message for full traceability (e.g., `git commit -m "feat(vuln_scanner): check file permissions [FW-101]"`).

## 2. Security Guidelines & Governance
* **Branch Protection**: Direct pushes to `main` and `development` are restricted to prevent unauthorized or untested code changes.
* **Peer Approvals**: A minimum of **1 peer approval** is required on Pull Requests (PRs) before merging code into `development` or `main`.
* **Code Audit**: All script modifications undergo security reviews to verify file handling, permission controls, and input validation.
