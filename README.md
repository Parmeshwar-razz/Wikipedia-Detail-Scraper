🧠 Wikipedia Info Finder

A simple Streamlit web app that finds and displays Wikipedia information about any person or topic using Selenium and BeautifulSoup.

⚙️ Setup Instructions
1️⃣ Clone this repository
git clone https://github.com/Parmeshwar-razz/Wikipedia-Detail-Scraper.git
cd Wikipedia_Info_Finder

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run code/Details_finder.py

🧩 How It Works

User enters a name in the input box.

The app searches Google for the Wikipedia link using Selenium.

BeautifulSoup extracts and displays the Wikipedia content in a scrollable text area.

Streamlit’s session_state is used to keep the driver active between reruns.

🧰 Tech Used
Tool	Purpose
Streamlit	Web UI
Selenium	Browser automation
BeautifulSoup	HTML parsing
ChromeDriver Auto Installer	Auto-manages browser driver

📁 Project Structure
Wikipedia_Info_Finder/
│
├── code/
│   └── Details_finder.py
├── requirements.txt
└── README.md

💡 Example Usage

Run the app.

Enter a name, e.g., Elon Musk.

Click “Find Details” → The Wikipedia link appears.

Click “Visit” → Full Wikipedia info shows in scrollable view.

![Wikipedia Info Finder Screenshot](Wikipedia%20details%20finder/Wikipedia%20Scraper.png)

🙋 Author

Parmeshwar Rajpurohit
Aspiring Data Scientist | Python Developer
