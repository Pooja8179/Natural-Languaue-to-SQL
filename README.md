🌟 Text-to-SQL App using Gemini + Streamlit + SQLite

This project is a simple web app where you can ask questions in normal English, and the app automatically converts them into SQL queries using Google Gemini.
The SQL is then executed on a SQLite database, and the results are shown instantly on the screen.

🚀 Features

Convert English sentences to SQL automatically

Uses Google Gemini for natural language understanding

Executes SQL queries on a SQLite database

Clean and simple Streamlit web interface

Works for question-based SQL retrieval (SELECT queries)

🛠️ Technologies Used

Python

Streamlit

Google Gemini API

SQLite

dotenv

📂 Project Structure
project/
│── app.py
│── student.db
│── .env
│── requirements.txt
│── README.md

📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

3️⃣ Install the required packages
pip install -r requirements.txt

4️⃣ Add your Gemini API key

Create a .env file:

GOOGLE_API_KEY=your_api_key_here

▶️ Run the Application
streamlit run app.py


Then open the link shown in the terminal (e.g., http://localhost:8501).

🧪 How It Works

You type a question in English

Gemini converts it to an SQL query

The SQL query is executed on student.db

The database results are shown on the webpage

💡 Example

You ask:

“How many students are in Data Science?”

Gemini generates:

SELECT COUNT(*) FROM STUDENT WHERE CLASS="Data Science";


Output shown:
6

📘 Future Improvements

Support INSERT, UPDATE, DELETE queries

Add authentication

Add multiple tables support

Add charts/visualizations

🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

📄 License

This project is open-source and free to use.
