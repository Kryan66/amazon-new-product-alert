# amazon-new-product-alert

This Python automation script tracks new product listings on Amazon based on a given keyword and sends an email alert when new products are found.

## 🔧 Features
- Searches Amazon for a specific keyword
- Extracts new product listings (title + link)
- Sends an email notification with the product summary

## 📁 Project Structure
amazon-new-product-alert/  
├── amazon_alert.py       # Main script  
├── .env                  # Contains email credentials  
└── README.md             # Project documentation  

## 🔐 Environment Setup (.env file)
Create a `.env` file in the project directory with this content:
> Gmail users: Use a Google App Password instead of your regular email password.

## ✅ How to Run
```bash
# Step 1: Activate virtual environment
source venv310/bin/activate

# Step 2: Install dependencies
pip install requests beautifulsoup4 python-dotenv

# Step 3: Run the script
python amazon_alert.py
