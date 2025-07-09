# 🛡️ Secure Remote Desktop Exposure – Windows Server Lab

This project demonstrates how to **securely expose RDP (Remote Desktop Protocol)** on a **Windows Server 2019** machine while applying real-world cybersecurity hardening techniques. It also includes **advanced monitoring with Sysmon**, **Duo 2FA integration**, and a custom **RDP honeypot** to simulate attacker behavior.

---

## 🔧 Lab Configuration

| Component             | Value                        |
|-----------------------|------------------------------|
| OS                    | Windows Server 2019          |
| Internal IP           | `192.168.1.139`              |
| RDP Real Access       | `PUBLIC_IP:50001 → 3389`     |
| RDP Honeypot Access   | `PUBLIC_IP:3389 → 33891`     |
| Remote Desktop        | ✅ Enabled                   |
| Network Level Auth    | ✅ Enabled                   |
| Admin Account         | 🔐 Strong password           |

---

## 🔐 Hardening Measures

### ✅ Step 1: Enable RDP Logon Auditing
```powershell
AuditPol /set /subcategory:"Logon" /success:enable /failure:enable
```

- `Event ID 4624` → Successful logon  
- `LogonType 10` → Remote Desktop logon

### ✅ Step 2: Restrict RDP by IP (Firewall)
```powershell
New-NetFirewallRule -DisplayName "Allow RDP from My IP" `
  -Direction Inbound -Protocol TCP -LocalPort 3389 `
  -RemoteAddress YOUR.PUBLIC.IP.HERE -Action Allow

Disable-NetFirewallRule -DisplayName "Remote Desktop - User Mode (TCP-In)"
```

### ✅ Step 3: Monitor Active RDP Sessions
```powershell
netstat -an | findstr :3389
```

### ✅ Step 4: Event Viewer Filter for RDP Logons
Paste this XML in **Event Viewer → Filter → XML tab**:
```xml
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[(EventID=4624)]] and *[EventData[Data[@Name='LogonType']='10']]
    </Select>
  </Query>
</QueryList>
```

### ✅ Step 5: Export RDP Logons with PowerShell
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} |
  Where-Object { $_.ToXml().ToString() -match '<LogonType>10</LogonType>' } |
  ForEach-Object {
    [xml]$xml = $_.ToXml()
    $ip = $xml.Event.EventData.Data | Where-Object {$_.Name -eq 'IpAddress'} | Select-Object -ExpandProperty '#text'
    "$($_.TimeCreated): $ip"
  } | Out-File "$env:USERPROFILE\Desktop\RDP_Logins.txt"
```

---

## 🧪 Sysmon Integration

- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) was installed to capture:
  - Logons
  - Process creations
  - File writes

### ✅ Install Command
```powershell
.\sysmon.exe -i
```

You can view logs under:  
📁 `Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon`

---

## 🔐 Duo 2FA Integration for RDP

- Duo Security was configured to enforce **two-factor authentication**
- RDP logon only succeeds **after a push confirmation via the Duo app**

📌 This prevents unauthorized access even if credentials are compromised.

**Learn more**: [https://duo.com/docs/rdp](https://duo.com/docs/rdp)

---

## 🪤 RDP Honeypot Simulation

A lightweight **Python honeypot** was created to log unauthorized RDP scanning attempts.

### ✅ Configuration

| Role         | IP                 | Port    |
|--------------|--------------------|---------|
| Real RDP     | 192.168.1.139      | 3389    |
| Honeypot     | 192.168.1.139      | 33891   |

Port forwarding:
- **Public 3389** → `192.168.1.139:33891` → Honeypot
- **Public 50001** → `192.168.1.139:3389` → Real RDP

### ✅ Why Port 33891?

> The honeypot script was written in Python. It's just a simulation example, since we can't run two services on the same internal port.  
> Instead of using the same port, I configured the honeypot to listen on **port 33891**.  
> If you want to attract more attackers, you can run it on **port 3389** from a different internal IP address — but not on the same machine that's already using that port.

### ✅ Running the Honeypot
```bash
python rdphoney.py
```

### ✅ Example Output (`rdphoney_log.txt`)
```
2025-07-09 21:47:12 - Connection from: 102.34.55.18
```

---

## ⚙️ Optional: Run Honeypot as a Windows Service

Using [NSSM](https://nssm.cc/download):

```powershell
nssm install rdphoney
# Set path to python.exe
# Set arguments to rdphoney.py
Start-Service rdphoney
```

---

## 📈 Bonus: Analyze Honeypot IPs
```powershell
Get-Content rdphoney_log.txt | ForEach-Object {
  ($_ -split ' - ')[1]
} | Group-Object | Sort-Object Count -Descending
```

---

## 🧠 Purpose

This lab simulates real-world attack surfaces and demonstrates proper security hardening for remote access.  
It's ideal for:

- 🔎 Blue team monitoring & log analysis
- 🛠️ Building a cybersecurity home lab
- 🎓 Learning attacker behavior via honeypots

---

## 📁 Files Included

- `rdphoney.py` – Python RDP honeypot script
- `rdphoney_log.txt` – attacker log file
- `README.md` – full documentation

---

## 👤 Author

**🧠 Caluian Ciprian**  
Cybersecurity enthusiast & practitioner  
Feel free to fork, improve, or contribute!

---
