import requests #Used for sending HTTP request to Roku API
import colorful as cf #used to desing the strings 


#desing 
banner=f"""                                                                        
                                                                                
██████   ██████  ██   ██ ██    ██ 
██   ██ ██    ██ ██  ██  ██    ██ 
██████  ██    ██ █████   ██    ██ 
██   ██ ██    ██ ██  ██  ██    ██ 
██   ██  ██████  ██   ██  ██████  
"""                                                              
info = f"""
{cf.red("====================================")}
       {cf.green("MADE BY WOOBENSKY ")}

Build  : {cf.cyan("v1.0")}   Author : {cf.yellow("WOOBENSKY")} 
{cf.red("====================================")}
""" 
print(cf.red(banner)+info)

ip = input(f"Enter Roku IP:\n>")

#IP address of the Roku device**
TV_ip =f"{ip}:8060"

#this cheks if Tv is online 
def check_conn():
 try:
  print(cf.yellow(f"[*] checking status...\n"))
  response = requests.get(f"http://{TV_ip}/device-image.png",timeout=5)
  
 
  if response.status_code == 200:
     print(cf.green("[+]Roku connected."))
     print(f"IP:{TV_ip}")
  else:
    print(cf.red("[-]Tv offline "))
 except requests.exceptions.RequestException:
   print(f"{cf.red("[*-]Device")} {cf.red("offline")}")


check_conn()
 
#converts user input into Roku API request
def send_command(command):
  try:
    if command == 1:
       one = f"http://{TV_ip}/keypress/Home"
       requests.post(one)
       

    elif command == 2:
      two = f"http://{TV_ip}/keypress/volumeup"
      requests.post(two)
    elif command == 3:
      three = f"http://{TV_ip}/keypress/volumedown"
      requests.post(three)
    elif command == 4:
      four = f"http://{TV_ip}/keypress/left"
      requests.post(four)
    elif command == 5: 
      five = f"http://{TV_ip}/keypress/right"
      requests.post(five)
    elif command == 6:
      six = f"http://{TV_ip}/keypress/up"
      requests.post(six)
    elif command == 7:
      seven = f"http://{TV_ip}/keypress/down"
      requests.post(seven)
    elif command == 8:
      eight = f"http://{TV_ip}/launch/837"
      requests.post(eight)
    elif command ==9:
      nine = f"http://{TV_ip}/launch/12"
      requests.post(nine)


    print(cf.green(f"command {command} is successfully executed."))
  except:
          print(cf.yellow("Error/TRY AGAIN / CONNECTION STATUS MUST BE CONNECTED!!!"))

#this is menue desing         
app =f"""
{cf.cyan("==========CONTROLER BELOW======================APPS====================")}

{cf.green("[1]")}Home  {cf.green("[2]")}Volume up  {cf.green("[3]")}Volume down  {cf.cyan("[P]Poweron")}  |    {cf.green("[8]")}Youtube  {cf.green("[9]")}Netflix

{cf.green("[4]")}LeftSide  {cf.green("[5]")}RightSide  {cf.green("[6]")}Up   {cf.green("[7]")}Down {cf.red("[X]Poweroff")} |{cf.purple("[C]Click")}|    {cf.red("[-]")}exit

======================{cf.yellow("[TYPE EXIT TO QUIT]")}==================================
    """
print(app)

p = f"http://{TV_ip}/keypress/poweron"
o = f"http://{TV_ip}/keypress/poweroff"

#keeps the remote running until the user exits
while True:
   try:
    
    inp = (input(f"\rchoose: "))
    if inp.lower() =="exit":
      print(cf.red(f"\n[-]Goodbye thanks for using {cf.yellow("@woobensky")} tool!!\n"))
      break
    elif inp.lower() =="p":
      requests.post(p)
      print(f"{cf.green("[+]")}TV {cf.green("was successfully powered on.")}")
      continue
    elif inp.lower() =="x":
        requests.post(o)
        print(f"{cf.red("[-]")}TV was {cf.red("powered off")}")
        continue
    elif inp.lower() == "c":
      click = f"http://{TV_ip}/keypress/select"
      requests.post(click)
      print(cf.green("click was successfull"))
      continue

    inp = int(inp)
    send_command(inp)
   except ValueError:
    print(cf.red("you must chose a number"))
   except KeyboardInterrupt:
    print(cf.red(f"\n[-]exit"))
    break
 