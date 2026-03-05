 🎒 AI Travel Planner for Students
An intelligent, AI-powered web application that helps students plan budget-friendly trips with personalized itineraries and smart budget optimization.

🌟 Features

Smart Budget Allocation - Automatically distributes budget across accommodation (40%), food (30%), activities (20%), and transport (10%)
Day-wise Itinerary Generation - Creates structured travel plans with activities for each day
Interactive Map Visualization - Displays destination on an interactive map using Folium
User-Friendly Interface - Simple, intuitive design requiring only 3 inputs
Instant Results - Generates complete travel plans in under 2 seconds
Mobile Responsive - Works seamlessly on all devices


🚀 Live Demo
Try the app: AI Travel Planner

📸 Screenshots
1. Homepage
2. Generated Itinerary
3. Budget Breakdown
   

🛠️ Technology Stack

Language: Python 3.10+
Web Framework: Streamlit
Map Visualization: Folium
Development Environment: Google Colab
Deployment: Streamlit Cloud
Version Control: Git & GitHub


📋 Installation & Setup
Prerequisites
bashPython 3.10 or higher
pip package manager
Clone Repository
bashgit clone  https://github.com/AnkitKumar-222/Travel_Planner_Agent
cd ai-travel-planner
Install Dependencies
bashpip install -r requirements.txt
Run Locally
bashstreamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 💻 Usage

1. **Enter Destination** - Type your travel destination (e.g., "Goa", "Manali")
2. **Set Budget** - Enter your total budget in ₹ (minimum ₹1000)
3. **Choose Duration** - Select number of days (1-30 days)
4. **Generate Plan** - Click the button to instantly create your itinerary
5. **View Results** - Get day-wise plans, budget breakdown, and interactive map

---

## 📊 How It Works

### Algorithm Overview
```
User Input → Validation → Budget Calculation → Itinerary Generation → Map Display
Budget Allocation Formula:
pythonDaily Budget = Total Budget ÷ Number of Days

Accommodation = Total Budget × 0.40 (40%)
Food = Total Budget × 0.30 (30%)
Activities = Total Budget × 0.20 (20%)
Transport = Total Budget × 0.10 (10%)
```

---

## 📁 Project Structure
```
ai-travel-planner/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file (optional)

🎯 Problem Statement
Planning trips is time-consuming and expensive for students with limited budgets. Current travel apps provide generic suggestions without considering:

Student-specific budget constraints
Personalized preferences
Efficient time management
Cost optimization

This application solves these challenges through AI-powered automation.

✨ Future Enhancements

 Real-time flight and hotel price integration via APIs
 Weather forecast integration
 Student discount database
 Group travel planning with cost splitting
 Chatbot interface for conversational planning
 Multi-language support
 Mobile app (Android & iOS)
 User authentication and saved itineraries
 Social sharing features
 Carbon footprint calculator


🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
ANKIT KUMAR

GitHub: https://github.com/AnkitKumar-222
LinkedIn: https://www.linkedin.com/in/ankit-kumar-355147244/
Email: ankit.kumar.official115@email.com


 Acknowledgments

Edunet Foundation - For providing the learning platform and project opportunity
AICTE - For the AI internship program
IBM SkillsBuild - For AI learning resources
Streamlit - For the amazing web framework
Folium - For map visualization capabilities


📞 Support
If you have any questions or issues, please:

Open an issue on GitHub
Contact: your ankit.kumar.official115@email.com


⭐ Show Your Support
Give a ⭐️ if this project helped you!

Made with ❤️ by [ ANKIT KUMAR]
Project Year: 2026
Course: AICTE AI Internship Batch 7

