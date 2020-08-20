import os
import pyttsx3

print("Welcome To Genie Voice Assistant Version 0.1\n")
pyttsx3.speak("Welcome To Genie Voice Assistant Version 0.1")

print("Please Before Using This Program Open 'Read Me' Text File for Better Understanding Of Features of This Program.\n")
pyttsx3.speak("Please Before Using This Program Open Read Me Text File for Better Understanding Of Features of This Program.")

print("Which Operation do you want to Run?\n")
pyttsx3.speak("Which Operation do you want to Run")
print("1. Control Panel Program Shortcuts")
print("2. Commonly Used Windows Tools")
print("3. Microsoft System Configurations")
print("4. Other Windows Tools")
print("5. System File Checker Utility")
print("6. Applications (if installed)\n")

while True:
	print("Enter Your Operation: ", end='')
	x = input()
	
	if ("1" in x) or ("Control" in x) or ("Panel" in x) or ("Shortcuts" in x) or ("control" in x) or ("panel" in x) or ("shortcuts" in x):
		print("You Have Chosen Control Panel Program Shortcuts")
		pyttsx3.speak("You Have Chosen Control Panel Program Shortcuts")
		print("Hence, These are the Options You Get\n")
		pyttsx3.speak("Hence, These are the Options You Get")
		print("1. Control Panel")
		print("2. Personalization - Color and Appearance")	
		print("3. File Explorer & Folders Properties")
		print("4. Keyboard Properties")
		print("5. Mouse Properties")
		print("6. Network Connections")
		print("7. Devices & Printers")
		print("8. Manage Current User Account")
		print("9. Manage All User Accounts")
		print("10. Windows Update")
		print("11. Administrative Tools")
		print("12. Task Scheduler")
		print("13. Application Wizard (Program & Features)")
		print("14. Power Options or Configuration")
		print("15. Date & Time Properties")
		print("16. Display - Screen Resolution")
		print("17. Regional Setting")
		print("18. Sound Properties")
		print("19. Internet Propeties")
		print("20. Security & Maintenance")
		print("21. System Properties")
		print("22. Ease of Access")
		print("23. Windows Defender Firewall\n")
		
		print("Choose Which One You Want To Run: ", end='')
		pyttsx3.speak("Choose Which One You Want To Run")
		a = input()
		
		if ("Control" in a) or ("control" in a) or ("Panel" in a) or ("panel" in a):
			pyttsx3.speak("Control Panel is Launching...")
			os.system("control")
		elif ("Personalization" in a) or ("personalization" in a) or ("Color" in a) or ("color" in a) or ("Appearance" in a) or ("apperance" in a):
			pyttsx3.speak("Personalization - Color and Appearance is Launching...")
			os.system("control color")
		elif ("File" in a) or ("file" in a) or ("Explorer" in a) or ("explorer" in a) or ("Folders" in a) or ("folders" in a):
			pyttsx3.speak("File Explorer & Folders Properties is Launching...")
			os.system("control folders")
		elif ("Keyboard" in a) or ("keyboard" in a):
			pyttsx3.speak("Keyboard Properties is Launching...")
			os.system("control keyboard")
		elif ("Mouse" in a) or ("mouse" in a):
			pyttsx3.speak("Mouse Properties is Launching...")
			os.system("control mouse")
		elif ("Network" in a) or ("network" in a) or ("Connections" in a) or ("connections" in a) or ("connection" in a):
			pyttsx3.speak("Network Connections is Launching...")
			os.system("control netconnections")
		elif ("Devices" in a) or ("devices" in a) or ("device" in a) or ("Printers" in a) or ("printers" in a) or ("printer" in a):
			pyttsx3.speak("Devices & Printers is Launching")
			os.system("control printers")
		elif ("Current" in a) or ("current" in a):
			pyttsx3.speak("Current User Account Setting is Launching...")
			os.system("control userpasswords")
		elif ("All" in a) or ("all" in a):
			pyttsx3.speak("All User Account Setting is Launching...")
			os.system("control userpasswords2")
		elif ("Windows" in a) or ("windows" in a) or ("Window" in a) or ("window" in a) or ("Update" in a) or ("update" in a):
			pyttsx3.speak("Windows Updates is Launching...")
			os.system("control update")
		elif ("Administrative" in a) or ("administrative" in a) or ("Admin" in a) or ("admin" in a):
			pyttsx3.speak("Administrative Tools is Launching...")
			os.system("control admintools")
		elif ("Task" in a) or ("task" in a) or ("Scheduler" in a) or ("scheduler" in a):
			pyttsx3.speak("Task Scheduler is Launching...")
			os.system("control schedtasks")
		elif ("Application" in a) or ("applications" in a) or ("App" in a) or ("app" in a) or ("Program" in a) or ("program" in a):
			pyttsx3.speak("Application Wizard Aka Program & Features is Launching...")
			os.system("appwiz.cpl")
		elif ("Power" in a) or ("power" in a):
			pyttsx3.speak("Power Options is Launching...")
			os.system("powercfg.cpl")
		elif ("date" in a) or ("Date" in a) or ("Time" in a) or ("time" in a):
			pyttsx3.speak("Date & Time Properties is Launching...")
			os.system("timedate.cpl")
		elif ("Display" in a) or ("Screen" in a) or ("display" in a) or ("screen" in a) or ("Resolution" in a) or ("resolution" in a):
			pyttsx3.speak("Display & Screen Resolution Setting is Launching...")
			os.system("desk.cpl")
		elif ("Regional" in a) or ("regional" in a) or ("Region" in a) or ("region" in a):
			pyttsx3.speak("Regional Setting is Launching...")
			os.system("intl.cpl")
		elif ("Sound" in a) or ("sound" in a) or ("audio" in a):
			pyttsx3.speak("Sound Properties is Launching...")
			os.system("mmsys.cpl")
		elif ("Internet" in a) or ("internet" in a):
			pyttsx3.speak("Internet Properties is Launching...")
			os.system("inetcpl.cpl")
		elif ("Security" in a) or ("security" in a) or ("Maintenance" in a) or ("maintnance" in a):
			pyttsx3.speak("Security & Maintenance is Launching...")
			os.system("wscui.cpl")
		elif ("System" in a) or ("system" in a):
			pyttsx3.speak("System Properties is Launching...")
			os.system("sysdm.cpl")
		elif ("Ease" in a) or ("ease" in a) or ("Access" in a) or ("access" in a):
			pyttsx3.speak("Ease Of Access is Launching...")
			os.system("utilman")
		elif ("Windows" in a) or ("windows" in a) or ("Firewall" in a) or ("firewall" in a):
			pyttsx3.speak("Windows Defender is Launching...")
			os.system("firewall.cpl")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")
	
	elif ("2" in x) or (("Commonly" in x) or ("common" in x)) and (("Windows" in x) or ("windows" in x)):
		print("You Have chosen Commonly Used Windows Tools")
		pyttsx3.speak("You Have chosen Commonly Used Windows Tools")
		print("Hence, These are the Options You Get\n")
		pyttsx3.speak("Hence, These are the Options You Get")
		print("1. Windows Explorer")
		print("2. Explorer C: Drive")
		print("3. Registory Editor")
		print("4. Windows Services")
		print("5. Task Manager")
		print("6. System Configuration Utility")
		print("7. Remote Desktop Connection Utility")
		print("8. Log Off Windows")
		print("9. Shuts Down Windows")
		print("10. Calculator")
		print("11. Command Prompt")
		print("12. Notepad\n")
		
		print("Choose Which One You Want To Run: ", end='')
		pyttsx3.speak("Choose Which One You Want To Run")
		b = input()
	
		if (("Windows" in b) or ("windows" in b) or ("window" in b)) and (("Explorer" in b) or ("explorer" in b)):
			pyttsx3.speak("Windows Explorer is Launching...")
			os.system("explorer")
		elif ("Explorer" in b) or ("explorer" in b) or ("Drive" in b) or ("drive" in b):
			pyttsx3.speak("C Drive is Exploring...")
			os.system("c:")
		elif ("Registory" in b) or ("registory" in b) or ("reg" in b) or ("Editor" in b) or ("editor" in b) or ("edit" in b):
			pyttsx3.speak("registory Editor is Launching...")
			os.system("regedit")
		elif (("Windows" in b) or ("windows" in b) or ("window" in b)) and (("Services" in b) or ("services" in b) or ("service" in b)):
			pyttsx3.speak("Windows Services is Launching...")
			os.system("services.msc")
		elif (("Task" in b) or ("task" in b)) and (("Manager" in b) or ("manager" in b)):
			pyttsx3.speak("Task Manager is Launching...")
			os.system("taskmgr")
		elif ("System" in b) or ("system" in b) or ("Configuration" in b) or ("configuration" in b) or ("Utility" in b) or ("utility" in b):
			pyttsx3.speak("System Configuration Utility is Launching...")
			os.system("msconfig")
		elif ("Remote" in b) or ("remote" in b) or ("Desktop" in b) or ("desktop" in b):
			pyttsx3.speak("Remote Desktop Connection Utility is Launching...")
			os.system("mstsc")
		elif ("Log" in b) or ("log" in b):
			pyttsx3.speak("Windows is Logging Off...")
			os.system("logoff")
		elif ("Shut" in b) or ("shut" in b) or ("Shutdown" in b) or ("shutdown" in b):
			pyttsx3.speak("Windows is Shutting Down...")
			os.system("shutdown")
		elif ("Calc" in b) or ("calc" in b) or ("Calculator" in b) or ("calculator" in b):
			pyttsx3.speak("Calculator is Launching...")
			os.system("calc")
		elif ("cmd" in b) or ("Cmd" in b) or ("Command" in b) or ("command" in b):
			pyttsx3.speak("Command Prompt is Launching...")
			os.system("cmd")
		elif ("Notepad" in b) or ("notepad" in b) or ("editor" in b):
			pyttsx3.speak("Notepad is Launching")
			os.system("notepad")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")
	
	elif ("3" in x) or ((("Microsoft" in x) or ("microsoft" in x)) or (("System" in x) or ("system" in x))) and (("Config" in x) or ("config" in x)):
		print("You Have chosen Microsoft System Configurations")
		pyttsx3.speak("You Have chosen Microsoft System Configurations")
		print("Hence, These are the Options You Get\n")
		pyttsx3.speak("Hence, These are the Options You Get")
		print("1. Device Management")
		print("2. Event Viewer")
		print("3. Computer Management including System Tools, Storage, Services and Applications")
		print("4. Disk Management")
		print("5. Component Services")
		print("6. Group Policy Editor")
		print("7. Local Security Policy Settings")
		print("8. Local Users and Groups")
		print("9. Performance Monitor")
		print("10. Shared Folders\n")
		
		print("Choose Which One You Want To Run: ", end='')
		pyttsx3.speak("Choose Which One You Want To Run")
		c = input()
	
		if ("Device" in c) or ("device" in c):
			pyttsx3.speak("Device Management is Launching...")
			os.system("devmgmt.msc")
		elif ("Event" in c) or ("event" in c) or ("Viewer" in c) or ("viewer" in c) or ("View" in c) or ("view" in c):
			pyttsx3.speak("Event Viewer is Launching")
			os.system("eventvwr.msc")
		elif (("Computer" in c) or ("computer" in c)) and (("Management" in c) or ("management" in c)):
			pyttsx3.speak("Computer Management is Launching...")
			os.system("compmgmt.msc")
		elif ("Disk" in c) or ("disk" in c):
			pyttsx3.speak("Disk Partition Manager is Launching...")
			os.system("diskmgmt.msc")
		elif ("Component" in c) or ("component" in c):
			pyttsx3.speak("Component Services is Launching...")
			os.system("dcomcnfg")
		elif (("Group" in c) or ("group" in c)) and (("Policy" in c) or ("policy" in c)):
			pyttsx3.speak("Group Policy Editor is Launching")
			os.system("gpedit.msc")
		elif ((("Local" in c) or ("local" in c)) or (("Security" in c) or ("security" in c))) and (("Policy" in c) or ("policy" in c)):
			pyttsx3.speak("Loacl Security Policy Editor Setting is Launching...")
			os.system("secpol.msc")
		elif (("Local" in c) or ("local" in c)) and ((("User" in c) or ("user" in c)) or (("Group" in c) or ("group" in c))):
			pyttsx3.speak("Local User and Groups is Launching...")
			os.system("lusrmgr.msc")
		elif ("Performance" in c) or ("performance" in c) or ("Monitor" in c) or ("monitor" in c):
			pyttsx3.speak("Performance Monitor is Launching...")
			os.system("perfmon.msc")
		elif (("Shared" in c) or ("shared" in c)) and (("Folder" in c) or ("folder" in c)):
			pyttsx3.speak("Shared Folders is Launching")
			os.system("fsmgmt.msc")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")
	
	elif ("4" in x) or ((("Windows" in x) or ("window" in x)) and (("Tools" in x) or ("tool" in x))):
		print("You Have chosen Other Windows Tools")
		pyttsx3.speak("You Have chosen Other Windows Tools")
		print("Hence, These are the Options You Get\n")
		pyttsx3.speak("Hence, These are the Options You Get")
		print("1. Create a Shared Folder Wizard")
		print("2. Direct X Diagnostic Tool")
		print("3. Disk Cleanup Utility")
		print("4. Windows Installer Details")
		print("5. Windows Magnifier")
		print("6. On Screen Keyboard")
		print("7. System Information")
		print("8. Volume Control")
		print("9. Windows Version")
		print("10. Compare Files")
		print("11. MS-Dos FTP")
		print("12. Volume Serial Number for C:")
		print("13. File Signature Verification Tool")
		print("14. Game Controllerss")
		print("15. Malicious Software Removal Tool")
		print("16. Private Chracter Editor\n")
		
		print("Choose Which One You Want To Run: ", end='')
		pyttsx3.speak("Choose Which One You Want To Run")
		d = input()
	
		if ("Shared" in d) or ("shared" in d):
			pyttsx3.speak("Chared Folder Wizard Creation Tool is Launching...")
			os.system("shrpubw")
		elif ("Direct" in d) or ("direct" in d) or ("Directx" in d) or ("DirectX" in d) or ("directx" in d):
			pyttsx3.speak("Direct X Dignostic Tool is Launching...")
			os.system("dxdiag")
		elif ("Disk" in d) or ("disk" in d) or ("Cleanup" in d) or ("cleanup" in d):
			pyttsx3.speak("Disk Cleanup Utility is Launching...")
			os.system("cleanmgr")
		elif (("Windows" in d) or ("windows" in d)) and (("Installer" in d) or ("installer" in d)):
			pyttsx3.speak("Windows Installer Details is Launching...")
			os.system("msiexec")
		elif ("Screen" in d) or ("screen" in d) or ("Keyboard" in d) or ("keyboard" in d):
			pyttsx3.speak("On Screen keyboard is Launching...")
			os.system("osk")
		elif (("System" in d) or ("system" in d)) and (("Information" in d) or ("information" in d) or ("Info" in d) or ("info" in d)):
			pyttsx3.speak("System Information is Launching...")
			os.system("msinfo32")
		elif (("Voulme" in d) or ("volume" in d)) and (("control" in d) or ("Control" in d)):
			pyttsx3.speak("Volume Control is Launching...")
			os.system("sndvol")
		elif ((("Windows" in d) or ("windows" in d)) or (("window" in d) or ("Window" in d))) and (("Version" in d) or ("version" in d)):
			pyttsx3.speak("Windows Version is launching...")
			os.system("winver")
		elif ("Compare" in d) or ("compare" in d):
			pyttsx3.speak("Compare Files Tool is Launching...")
			os.system("comp")
		elif ("ftp" in d) or ("Ftp" in d) or ("Transfer" in d) or ("transfer" in d):
			pyttsx3.speak("MS-DOS File Transfer Protocol is Launching...")
			os.system("ftp")
		elif ("Serial" in d) or ("serial" in d):
			pyttsx3.speak("Volume Serial Number For C: Tool is Launching...")
			os.system("label")
		elif ("Singature" in d) or ("signature" in d) or ("verification" in d) or ("verification" in d):
			pyttsx3.speak("File Signature Verification Tool is Launching...")
			os.system("sigverif")
		elif ("Game" in d) or ("game" in d) or ("Controller" in d) or ("controller" in d):
			pyttsx3.speak("Game Controller Setting is Launching...")
			os.system("joy.cpl")
		elif ("Malicious" in d) or ("malicious" in d) or ("Remove" in d) or ("remove" in d):
			pyttsx3.speak("Malicious Software Removal Tool is Launching...")
			os.system("mrt")
		elif ("Private" in d) or ("private" in d) or ("Char" in d) or ("char" in d):
			pyttsx3.speak("Private Chracter Editor is Launching...")
			os.system("eudcedit")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")
	
	elif ("5" in x) or ((("System" in x) or ("system" in x)) or (("file" in x) or ("File" in x))) and (("check" in x) or ("Check" in x)):
		print("You Have Chosen System File Checker Utility")
		pyttsx3.speak("You Have Chosen System File Checker Utility")
		print("Hence, These are the Options You Get\n")
		pyttsx3.speak("Hence, These are the Options You Get")
		print("1. Scan Immediately")
		print("2. Scan Once at Next Boot")
		print("3. Scan On Every Boot")
		print("4. Return to Default Setting")
		print("5. Purge File Cache")
	#	print("6. Set Chache Size to Size:\n") "This Option Doesn't Works Now"
	
		print("Choose Which One You Want To Run: ", end='')
		pyttsx3.speak("Choose Which One You Want To Run")
		e = input()
	
		if ("Immediate" in e) or ("immediate" in e):
			pyttsx3.speak("Scan Immediately is Launching...")
			os.system("sfc /scannow")
		elif ("Next" in e) or ("next" in e):
			pyttsx3.speak("Scan Once at Next Boot is Set...")
			os.system("sfc /scannow")
		elif ("Every" in e) or ("every" in e):
			pyttsx3.speak("Scan On Every Boot is Set...")
			os.system("sfc/ scanboot")
		elif (("Return" in e) or ("return" in e)) or ("default" in e) or ("Default" in e):
			pyttsx3.speak("Return to Default Setting is Set...")
			os.system("sfc /revert")
		elif ("Purge" in e) or ("purge" in e):
			pyttsx3.speak("Purge File Cache is Performing...")
			os.system("sfc /purgecache")
	#	elif (("Set" in e) or ("set" in e)) and (("Cache" in e) or ("cache" in e)):
			pyttsx3.speak("Enter The Value in MegaBytes To Set Cache Size...")
			print(": ", end='')
			w = input()
			os.system("sfc /cachesize= w")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")

	elif ("6" in x) or ("App" in x) or ("app" in x) or ("Application" in x) or ("application" in x):
		print("You Have chosen Applications to Run, Before Running Any Application You Must Set The Enviornmets Variables Otherwise This will not Work.")
		pyttsx3.speak("You Have chosen Applications to Run, Before Running Any Application You Must Set The Enviornmets Variables Otherwise This will not Work.")
		print("So, These are the Applications You Get\n")
		pyttsx3.speak("So, These are the Applications You Get")
		print("1. Adobe Photoshop 2020")
		print("2. Google Chrome")
		print("3. Internet Explorer")
		print("4. iTunes")
		print("5. Internet Download Manager")
		print("6. Tor browser")
		print("7. VLC")
		print("8. Windows Media Player\n")
	
		print("Choose Which Application You Want To Run: ", end='')
		pyttsx3.speak("Choose Which Application You Want To Run")
		f = input()
	
		if ("Adobe" in f) or ("adobe" in f) or ("Photoshop" in f) or ("photoshop" in f) or ("PS" in f) or ("ps" in f):
			pyttsx3.speak("Adobe Photoshop 2020 is Launching...")
			os.system("photoshop")
		elif ("Google" in f) or ("google" in f) or ("Chrome" in f) or ("chrome" in f) or ("Browser" in f) or ("browser" in f):
			pyttsx3.speak("Google Chrome is Launching...")
			os.system("chrome")
		elif (("Internet" in f) or ("internet" in f)) and ((("Ie" in f) or ("ie" in f)) or (("explorer" in f) or ("Explorer" in f))):
			pyttsx3.speak("Internet Explorer is Launching...")
			os.system("iexplore")
		elif ("iTunes" in f) or ("itunes" in f):
			pyttsx3.speak("iTunes is Launching...")
			os.system("iTunes")
		elif ("Download" in f) or ("download" in f) or ("Downloader" in f) or ("downloader" in f) or ("IDM" in f) or ("idm" in f):
			pyttsx3.speak("Internet Download Manager is Launching...")
			os.system("idman")
		elif ("Tor" in f) or ("tor" in f):
			pyttsx3.speak("TOR Browser is Launching...")
			os.system("firefox")
		elif ("VLC" in f) or ("Vlc" in f) or ("vlc" in f):
			pyttsx3.speak("VLC Media Player is Launching...")
			os.system("vlc")
		elif (("Windows" in f) or ("window" in f)) and (("media" in f) or ("player" in f)):
			pyttsx3.speak("Windows Media Player is Launching...")
			os.system("wmplayer")
		else:
			print("You Have Done Wrong Choice")
			pyttsx3.speak("You Have Done Wrong Choice")

	elif ("quit" in x) or ("Quit" in x) or ("close" in x) or ("Close" in x) or ("Exit" in x) or ("exit" in x) or ("no" in x) or ("bye" in x):
		print("Thank You For Using Genie Voice Assistant Version 0.1")
		pyttsx3.speak("Thank You For Using Genie Voice Assistant Version 0.1")
		break;
	
	else:
		print("You Have Done Wrong Choice,Try Again,")
		pyttsx3.speak("You Have Done Wrong Choice, Try Again,")


# Coder Note: Whatever i learned till today i used all of them in this program. The More I Learn Python Langauge The More Features I'll Implement. Till Then Enjoy ;)
# This one Took me Approx 10 Hours to Write From Sacrtch & This is still in beta version.
# Regards: #dcgmechanics
#Telegram:- t.me/dcgmechanics
#Discord:- dcgmechanics#0422
