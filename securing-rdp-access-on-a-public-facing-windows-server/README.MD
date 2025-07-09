# 🛡️ Secure Remote Desktop Exposure – Windows Server Lab Project

This project demonstrates how to securely expose **Remote Desktop Protocol (RDP)** on a **Windows Server 2019** machine accessible over the internet.  
It focuses on reducing risk, monitoring access, and applying real-world cybersecurity controls.

---

## 🔧 Configuration Summary

- **Operating System:** Windows Server 2019  
- **Local IP Address:** `192.168.1.139`  
- **Port Forwarding:**  
  - External Port: `50001`  
  - Internal Port: `3389`  
- **Remote Desktop Enabled:** ✅  
- **Network Level Authentication (NLA):** ✅ Enabled  
- **User Account:** `Administrator` with a strong password  
- **Public Access:** Verified via RDP client using `PUBLIC_IP:50001`

---

## 🔐 Hardening Measures Implemented

### ✅ Step 1: Enable RDP Login Auditing
- Enabled auditing via:

