import os
import pyfiglet
from termcolor import colored
import tldextract

# List of known legitimate domains for comparison
legitimate_domains = ["google.com", "facebook.com", "amazon.com", "twitter.com"]

# Function to check if the URL is suspicious
def check_suspicious_url(url):
    # Extract domain using tldextract (splits the URL into subdomain, domain, and suffix)
    parsed_url = tldextract.extract(url)
    
    domain = parsed_url.domain + "." + parsed_url.suffix
    
    # Check if the domain is in the legitimate domain list
    if domain not in legitimate_domains:
        print(colored(f"Suspicious URL detected: {url}", 'red'))
        return True
    else:
        print(colored(f"This seems to be a legitimate URL: {url}", 'green'))
        return False

# Function to clear the screen and print the logo and name
def clear_screen_and_print_banner():
    # Clear the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # FishDetec ASCII art logo
    banner = pyfiglet.figlet_format("FishDetec")
    print(colored(banner, 'cyan'))
    
    # Author Name
    print(colored("By: Sambit D Swain", 'yellow'))
    
    # Welcome message
    print(colored("Welcome to the Phishing Detection System!", 'blue'))
    print(colored("This system will check if a URL is legitimate or a phishing attempt.", 'magenta'))
    print(colored("You can check multiple URLs. To exit, press Ctrl+Z.", 'yellow'))
    print(colored("Please enter a URL to check.", 'magenta'))

# Main function
def main():
    clear_screen_and_print_banner()
    
    # Loop to allow checking multiple URLs
    while True:
        # Ask user for the URL to check
        url = input(colored("Enter the URL to check: ", 'green'))
        
        if url.lower() == 'exit':
            print(colored("Exiting the program. Goodbye!", 'yellow'))
            break
        
        # Check if the URL is suspicious
        if check_suspicious_url(url):
            print(colored("This is likely a phishing URL.", 'red'))
        else:
            print(colored("This seems to be a legitimate URL.", 'green'))

# Start the program
if __name__ == "__main__":
    main()
