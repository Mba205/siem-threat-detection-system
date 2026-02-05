# Brute-Force Authentication Detection

## 1. Overview
This detection identifies potential brute-force or credential-stuffing attacks by monitoring repeated failed authentication attempts against user accounts within a short time window. Such activity is commonly associated with unauthorized access attempts and represents a high-priority SOC alert.

## 2. Detection Objective
- Detect repeated failed login attempts
- Identify user accounts under attack
- Enable rapid analyst investigation and response

## 3. Log Source
- Authentication logs
- Identity provider logs
- Active Directory / SSO logs (conceptual)

## 4. Detection Logic
The detection triggers when multiple failed login attempts are observed for the same user account within a defined time window.

### Detection Conditions

| Condition | Value |
|---------|------|
| Failed login attempts | ≥ 5 |
| Time window | 5 minutes |
| Target | Same user account |

## 5. Example SIEM Query (Splunk)

    index=authentication_logs action="failure"
    | stats count by user, src_ip
    | where count >= 5

## 6. Alert Severity
High

## 7. Analyst Investigation Steps
1. Identify the affected user account
2. Review source IP addresses associated with the failures
3. Check for successful logins following the failures
4. Correlate with VPN or endpoint activity
5. Determine whether the activity is user error or malicious

## 8. Recommended Response Actions
- Temporarily lock the affected account
- Force a password reset
- Block or monitor suspicious source IPs
- Escalate to incident response if compromise is suspected

## 9. MITRE ATT&CK Mapping

| Tactic | Technique |
|------|----------|
| Credential Access | Brute Force (T1110) |

