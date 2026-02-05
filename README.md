# SIEM Threat Detection System

## 1. Overview

This project demonstrates a **Security Information and Event Management (SIEM) Threat Detection System** focused on identifying suspicious authentication and remote access activity. The project is designed to showcase practical SIEM workflows, threat detection logic, and security analysis using a combination of **Splunk**, **Python**, and detection best practices.

The system focuses on **realistic SOC use cases** rather than large-scale infrastructure, emphasizing detection logic, alerting, and response.

---

## 2. Objectives

The objectives of this project are to:

- Demonstrate understanding of SIEM workflows
- Design effective threat detection use cases
- Simulate realistic security events using Python
- Analyze authentication and VPN activity
- Map detections to common attack techniques

---

## 3. Architecture Overview

The SIEM architecture implemented in this project includes:

- **Log sources:** Authentication logs and VPN access logs
- **Ingestion:** Logs ingested into Splunk
- **Detection:** Rule-based searches identifying suspicious behavior
- **Alerting:** Threshold-based alerts triggered on detection conditions
- **Response:** Analyst-driven investigation and remediation recommendations

> Note: Detection logic is tool-agnostic and includes conceptual mapping for ELK Stack implementations.

---

## 4. Technologies Used

- Splunk (SIEM)
- Python (log generation and enrichment)
- ELK Stack (conceptual mapping)
- Threat detection and SOC analysis

---

## 5. Detection Use Cases

This project currently includes the following detection scenarios:

1. **Brute-Force Authentication Attempts**
   - Identifies repeated failed login attempts within a short time window
   - Detects potential credential-stuffing or brute-force attacks

2. **Suspicious VPN Access Behavior**
   - Identifies anomalous VPN logins based on timing or source indicators
   - Highlights potential unauthorized remote access

Detailed detection logic and queries are documented in the `detections/` directory.

---

## 6. Log Simulation

To support detection testing without enterprise infrastructure, this project uses **Python-generated sample logs** that simulate:

- Successful and failed authentication attempts
- VPN connection and disconnection events
- Normal and suspicious user behavior

These logs are located in the `logs/` directory and can be ingested into Splunk for testing.

---

## 7. Alerting and Response

For each detection use case, the following is documented:

- Detection logic and thresholds
- Alert trigger conditions
- Recommended analyst investigation steps
- Suggested remediation actions

---

## 8. Mapping to Attack Techniques

Detection logic is mapped to common attack techniques, including:

- Credential Access
- Initial Access
- Persistence

This mapping supports analyst understanding and prioritization.

---

## 9. Future Enhancements

Potential enhancements include:

- Additional detection use cases
- Integration with enrichment sources
- Expanded ELK Stack implementations
- Visualization dashboards

---

## 10. References

Authoritative sources and references are documented in the `references/` directory.
