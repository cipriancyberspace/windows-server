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
- Enabled auditing via: AuditPol /set /subcategory:"Logon" /success:enable /failure:enable

- Relevant logs:  
- `Event ID 4624` → Successful logon  
- `LogonType 10` → Indicates RDP login

### ✅ Step 2: Restrict RDP by IP Address (Firewall Rule)
```powershell
New-NetFirewallRule -DisplayName "Allow RDP from My IP" `
-Direction Inbound -Protocol TCP -LocalPort 3389 `
-RemoteAddress YOUR.PUBLIC.IP.HERE -Action Allow

Disable-NetFirewallRule -DisplayName "Remote Desktop - User Mode (TCP-In)"

### ✅ Step 3: Monitor Active RDP Connections

Run the command `netstat -an | findstr :3389` to view active RDP connections.

### ✅ Step 4 Create Event Viewer XML Filter for RDP Logons

'<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[(EventID=4624)]]
      and
      *[EventData[Data[@Name='LogonType']='10']]
    </Select>
  </Query>
</QueryList>'
