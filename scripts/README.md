# SIEM Brute Force Detection & Authentication Monitoring

## 📌 Overview
This project demonstrates a simplified Security Information and Event Management (SIEM) pipeline that simulates authentication activity, ingests logs into Elastic SIEM, detects brute force login behavior, and visualizes security events in a SOC-style dashboard.

The system generates realistic login attempts, forwards them to Elasticsearch, applies detection rules, and displays insights using Kibana dashboards.

---

## 🏗 Architecture

Python Log Generator  
→ Elasticsearch Index (soc-logs)  
→ Detection Rules (Brute Force Threshold)  
→ Kibana Dashboards & Alerts  

---

## 🔧 Technologies Used

- Python  
- Elasticsearch Cloud  
- Kibana (Elastic Security & Dashboards)  
- KQL (Kibana Query Language)  
- REST APIs  

---

## ⚙️ Features

- Simulated authentication log generation  
- Failed vs successful login tracking  
- Brute force detection rule (threshold-based)  
- Real-time alert generation  
- Dashboards for monitoring:
  - Failed login attempts over time  
  - Top source IPs for failed logins  
  - Authentication event distribution  

---

## 🚨 Detection Logic

Brute force activity is detected when:

- Multiple failed authentication attempts  
- From the same source IP  
- Within a short time window  

KQL used:

```kql
event.category: "authentication" and event.outcome: "failed"
