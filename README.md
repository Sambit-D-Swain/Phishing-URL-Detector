#FishDetec - Phishing Detection System

FishDetec is a Python-based tool designed to detect phishing URLs and identify whether they are legitimate or potentially dangerous. This project is aimed at improving cybersecurity awareness by helping users stay safe online. The tool checks the provided URLs against a list of legitimate domains and can be extended with more advanced features like machine learning and real-time phishing detection.


---

Table of Contents

Installation

Usage

Future Features

License

Contributing



---

Installation

To get started with FishDetec, follow the steps below to install the required dependencies:

1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/your-username/FishDetec.git
cd FishDetec

2. Install Required Packages

Install the required Python libraries by running:

pip install -r requirements.txt

This will install the necessary packages such as pyfiglet, termcolor, tldextract, etc.

3. Python 3.6+

Make sure you are using Python 3.6 or higher for compatibility with the libraries used in this project.


---

Usage

1. Running the Tool

To run FishDetec, open a terminal and execute the following command:

python phishing_detector.py

2. Checking URLs

Once the program starts, it will prompt you to enter a URL to check. You can input a URL, and the program will detect if it is legitimate or a phishing attempt.

Legitimate URLs will be displayed in green.

Suspicious URLs will be displayed in red.


You can check multiple URLs without restarting the program. To exit the program, press Ctrl+Z.

Example usage:

$ python phishing_detector.py
Welcome to the Phishing Detection System!
Enter the URL to check: http://google.com
This seems to be a legitimate URL.

Enter the URL to check: http://phishingsite.com
Suspicious URL detected: http://phishingsite.com
This is likely a phishing URL.

Enter the URL to check: exit
Exiting the program. Goodbye!


---

Future Features

In the future, we plan to add the following features to FishDetec:

1. Machine Learning-based Phishing Detection: We will implement a machine learning model to classify URLs as phishing or legitimate based on URL features.


2. Google Safe Browsing API Integration: We plan to integrate the Google Safe Browsing API for real-time phishing detection.


3. Web Interface: A simple web-based interface will be developed for users who prefer a graphical user interface (GUI).


4. Browser Extension: A browser extension for Chrome/Firefox that can automatically check URLs in real time.


5. User Feedback System: Users can submit URLs they believe to be phishing but are not detected by the system.


6. Phishing Database: Real-time updating of phishing URLs from external sources.




---

License

This project is licensed under the MIT License.


---

Contributing

We welcome contributions to FishDetec! To contribute, follow these steps:

1. Fork this repository.


2. Create a new branch.


3. Make your changes.


4. Test your changes.


5. Submit a pull request with a description of your changes.




---
