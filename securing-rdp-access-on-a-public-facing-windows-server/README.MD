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

Enabled auditing via:

```powershell
AuditPol /set /subcategory:"Logon" /success:enable /failure:enable
```

Relevant logs:
- `Event ID 4624` → Successful logon  
- `LogonType 10` → Indicates RDP login

---

### ✅ Step 2: Restrict RDP by IP Address (Firewall Rule)

```powershell
New-NetFirewallRule -DisplayName "Allow RDP from My IP" `
-Direction Inbound -Protocol TCP -LocalPort 3389 `
-RemoteAddress YOUR.PUBLIC.IP.HERE -Action Allow

Disable-NetFirewallRule -DisplayName "Remote Desktop - User Mode (TCP-In)"
```

---

### ✅ Step 3: Monitor Active RDP Connections

Run the command below to view active RDP connections:

```powershell
netstat -an | findstr :3389
```

---

### ✅ Step 4: Create Event Viewer XML Filter for RDP Logons

Paste this XML into Event Viewer → Filter → XML tab:

```xml
<QueryList>
  <Query Id="0" Path="Security">
    <Select Path="Security">
      *[System[(EventID=4624)]]
      and
      *[EventData[Data[@Name='LogonType']='10']]
    </Select>
  </Query>
</QueryList>
```

---

### ✅ Step 5: Export RDP Logons via PowerShell

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} |
  Where-Object { $_.ToXml().ToString() -match '<LogonType>10</LogonType>' } |
  ForEach-Object {
    [xml]$xml = $_.ToXml()
    $ip = $xml.Event.EventData.Data | Where-Object {$_.Name -eq 'IpAddress'} | Select-Object -ExpandProperty '#text'
    "$($_.TimeCreated): $ip"
  } | Out-File "$env:USERPROFILE\Desktop\RDP_Logins.txt"
```

### ✅ Step 6: Show all public ip in RDP Logons

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} |
  Where-Object { $_.ToXml().ToString() -match '<LogonType>10</LogonType>' } |
  ForEach-Object {
    [xml]$xml = $_.ToXml()
    $ip = $xml.Event.EventData.Data | Where-Object {$_.Name -eq 'IpAddress'} | Select-Object -ExpandProperty '#text'
    "$($_.TimeCreated): $ip"
  }
```


## 🔐 Sysmon Integration

Sysmon was installed and configured to track system activity
All logons, process creations, and file writes are now recorded
Log analysis can be done via Event Viewer or exported for correlation

After you download sysmon use this command for install it ```powershell
.\sysmon.exe -i ```


## 🔐 Enable **2FA for RDP** via Duo  

Duo Security was integrated to require 2FA before allowing RDP login

Duo Client + Application created and configured

Only after a successful push notification approval, the user is allowed to log in

💡 This mitigates credential theft risks even if the password is leaked.
 
## 🔐 Set up an **RDP honeypot** to collect attacker behavior  
  

---

## 🎯 Purpose

This lab simulates real-world attack surfaces and demonstrates proper security hardening for remote access scenarios.  
It can be used to:

- Practice monitoring & defense  
- Build a cybersecurity lab portfolio  
- Understand how attackers probe public RDP endpoints  

---

## 🧠 Credits

Project by [Your Name] – cybersecurity learner & practitioner.  
Feel free to contribute or fork!
