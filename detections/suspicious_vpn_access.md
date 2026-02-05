# Suspicious VPN Access Detection

## 1. Overview
This detection identifies potentially unauthorized VPN access by analyzing unusual login behavior such as access during abnormal hours or repeated connections from unfamiliar source locations.

## 2. Detection Objective
- Detect anomalous VPN login behavior
- Identify potential unauthorized remote access
- Support analyst investigation and response

## 3. Log Source
- VPN access logs
- Remote access gateway logs
- Firewall VPN logs (conceptual)

## 4. Detection Logic
The detection triggers when VPN access occurs outside of expected usage patterns.

### Detection Conditions

| Condition | Value |
|----------|------|
| Login time | Outside normal business hours |
| Source IP | Previously unseen or rare |
| Frequency | Multiple connections in short time |

## 5. Example SIEM Query (Splunk)

    index=vpn_logs action="login"
    | stats count by user, src_ip
    | where count > 3

## 6. Alert Severity
Medium to High

## 7. Analyst Investigation Steps
1. Identify the user account associated with the VPN access
2. Review login times and geographic indicators
3. Correlate with authentication and endpoint activity
4. Confirm with the user if access was legitimate

## 8. Recommended Response Actions
- Temporarily disable VPN access if suspicious
- Require multi-factor authentication verification
- Reset credentials if compromise is suspected
- Escalate to incident response if necessary

## 9. MITRE ATT&CK Mapping

| Tactic | Technique |
|------|----------|
| Initial Access | Valid Accounts (T1078) |
