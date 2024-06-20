# Key Loggers
- Short for "keystroke logger", is a program or device that records everything you type on your computer or mobile device.
- Typically used by criminals to steal sensitive information such as passwords, credit card numbers and other personal data. This data is then used for identity theft, financial fraud, etc.

#### General Algorithm
1. **Initialization**
    1. *Import Libraries* ⇒ Depending on the programming language, the keylogger would import libraries to handle keyboard events.
    2. *Define Log File* ⇒ Cretae a file to store the keystrokes
2. **Capture Keystrokes**
    1. *Event Listener* ⇒ Program sets up an event listener to listen for key press events from the operating system
    2. *Capture key data* ⇒ When a key is pressed, the event listener retrieves information about the key, which might include the pressed key itself, any special keys like shift or alter, and potentially even key timings.
3. **Process Key Data**
    1. *Basic Keys* ⇒ For standard letter and number keys, the program simply adds the character to the log file
    2. *Special Keys* ⇒ Special keys (Shift, Caps Lock, etc) might be noted in the log but not directly added as a character. Enter, tab, backspace, etc would likely be added as special characters.
4. **Store Keystrokes** ⇒ The program writes the captured key data to the log file
5. **Maintain stealth** ⇒ The program might try to hide itself from running processes to avoid detection.
6. **Loop** ⇒ The program loops back to step 2 to continuously listen for capture keystrokes.

#### Types of Key Loggers
1. **Software Keyloggers**
 - Programs that run in the background on your devices, secretly recording your keystrokes.
 - Tricky to detect because they don't leave any physical signs of being installed.
2. **Hardware Keyloggers**
 - Small devices that are physical attached to your keyboard or computer.
 - Less common, but more difficult to detect because they are not software programs that can be scanned for by antivirus softwares.

#### Methods of Installing or Downloading Keyloggers
1. **Deceptive Downloads**
    1. *Phishing Emails* ⇒ These emails appear to be from legitimate sources but contain malicious attachments or links. Clicking on theses attachements or links can install a keylogger disguised as a document or pograms.
    2. *Malicious Software Downloads* ⇒ Downloading software from untrusted sources like peer-to-peer networks or clicking on misleading ads can lead to unkowingly installing a keylogger bundled with the desired software.
2. **Tricking Users into running malicious code (Drive-by Downloads)** ⇒ Visiting a compromised website can inject malicious code into your browser. This code might exploit vulnerabilities to download a key loggers in the background without your knowledge
3. **Physical Access (Hardware Keyloggers)** ⇒ Small devices are physically attached to your keyboard cable or USB port. Less common but used if someone has physical access to your device.
4. **Remote Access Tools** ⇒ Remote access tools can be exploited by attackers to install a keylogger if they gain access to your device.

#### Signs of a Keylogger
1. **Unusual Behavior**
    1. *Slow performance* ⇒ Keyloggers can use system resources in the background, leading to a sluggish device, slower browsing, and programs taking longer to launch.
    2. *Random Restarts* ⇒ In some cases, a keylogger might cause unexpected crashes or restarts on your device.
    3. *Battery Drain* ⇒ The extra processes running from the keylogger can lead to increased battery consumption on your phone or laptop.
2. **Suspicious Software Behavior**
    1. *Unknown Programs* ⇒ If you find unfamiliar programs running in your task manager (Windows) or Activity Monitor (Mac), it's worth investigating further.
    2. *Delayed Typing* ⇒ Do you notice a slight lag between pressing a key and the character appearing on the screen? This could be a sign of a keylogger recording your keystrokes.
    3. *Cursor Anomalies* ⇒ A disappearing cursor or unexpected cursor movements could indicate a keylogger interfering with your normal input.
3. **Login Issues**
    1. *Failed Login Attempts* ⇒ If you're experiencing unusual login attempts on your accounts, it could be because someone has stolen your credentials through a keylogger.
    2. *Unusual Account Activity* ⇒ Monitor your online accounts for any suspicious activity, such as unauthorized purchases or changes to your profile information.
4. **General Awareness**
    1. *Phishing Attempts* ⇒ An increase in phishing emails or deceptive links could be a sign that someone is trying to install a keylogger.
    2. *Missing Security Software* ⇒ Not having reputable antivirus or anti-malware software leaves your device vulnerable to various threats, including keyloggers.

#### How to remove a Keylogger?
1. **Boot into Safe Mode**
    - This starts your device with only the essential programs loaded, potentially bypassing the keylogger if it relies on startup processes.
    - Safe mode instructions vary depending on your operating system (Windows, Mac, Android), so a quick web search for "[Your OS] Safe Mode" will provide specific steps.
2. **Run a Security Scan**
    - Use your existing antivirus or anti-malware software to perform a full system scan. If possible, update the software's definitions before the scan to ensure it has the latest threat detection capabilities.
    - Consider running a scan with a reputable secondary security software program to get a broader perspective. There may be free trials available for some programs.
3. **Manual Check for Suspicious Programs**
    - Open your task manager (Windows) or Activity Monitor (Mac) and look for unfamiliar programs running in the background.
    - Search the program names online to see if they are legitimate or flagged as malware.
    - If you find something suspicious, you can try to end the process, but be cautious not to terminate crucial system programs.
4. **Check Startup Programs**
    - Keyloggers might add themselves to startup programs to run automatically when you boot your device.
    - In Windows, search for "Startup Apps" and disable any programs you don't recognize or trust.
5. **Consider a Password Reset (After removing keylogger)**
    - Once you've hopefully removed the keylogger, it's a good security practice to change your passwords for all important accounts (banking, email, social media, etc.).
    - Use strong and unique passwords for each account. A password manager can be a helpful tool for this.