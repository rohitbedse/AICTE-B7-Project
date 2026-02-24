# 🧠 Job Application Intelligence System

> **AICTE Internship Project** | EduNet Foundation & IBM SkillsBuild  
> A smart resume analyzer powered by Google's Gemini AI and LangChain

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

The **Job Application Intelligence System** is an AI-powered tool that helps job seekers optimize their resumes for specific job descriptions. Using parallel processing with LangChain and Google's Gemini AI, it provides instant feedback on resume-job alignment, missing skills, improvement suggestions, and generates custom cover notes.

**Internship Context:** This project was developed as part of the AICTE internship program in collaboration with EduSkills Foundation and IBM SkillsBuild.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **📊 Match Analysis** | Calculates skill match percentage (0-100%) between resume and job description |
| **❌ Missing Skills Detection** | Identifies key skills absent from your resume |
| **✍️ Smart Suggestions** | Provides actionable improvements tailored to the job |
| **📨 Cover Note Generator** | Creates professional 3-line cover notes instantly |
| **⚡ Parallel Processing** | Uses LangChain's RunnableParallel for simultaneous AI calls |
| **🔒 Secure API Handling** | Environment variable protection for API keys |

---

## 🛠️ Tech Stack

**Core Technologies:**
- **Python 3.8+**
- **Streamlit** - Interactive web interface
- **LangChain** - LLM orchestration and chaining
- **Google Generative AI (Gemini 2.5 Flash)** - Large Language Model
- **python-dotenv** - Environment variable management

**Key Libraries:**
```
streamlit
langchain
langchain-google-genai
python-dotenv
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/job-application-intelligence.git
cd job-application-intelligence
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ **Security Note:** Never commit your `.env` file to version control. It's already added to `.gitignore`.

---

## 🎮 Usage

### Run the Application
```bash
streamlit run app.py
```

### How to Use
1. **Paste your Resume** in the first text area
2. **Paste the Job Description** in the second text area
3. Click **"Analyze Resume vs JD 🚀"**
4. Review the four-panel analysis:
   - Match Percentage
   - Missing Skills
   - Improvement Suggestions
   - Custom Cover Note

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Streamlit UI  │
│  (User Inputs)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│     RunnableParallel        │
│  (LangChain Parallel Chain) │
└────────┬────────────────────┘
         │
    ┌────┴────┬────────┬────────┐
    ▼         ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│ Match │ │Missing│ │Improve│ │ Cover │
│  %    │ │Skills │ │Suggestions│ │ Note  │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │         │         │
    └────┬────┴─────────┴─────────┘
         │
         ▼
┌─────────────────────────┐
│ Google Gemini 2.5 Flash │
│    (LLM Processing)     │
└─────────────────────────┘
```

**Parallel Processing Benefits:**
- 4x faster than sequential processing
- Independent AI calls for each analysis type
- Efficient resource utilization
  
---

## 🔮 Future Enhancements

- [ ] PDF/Word resume upload support
- [ ] ATS score visualization with charts
- [ ] Resume template recommendations
- [ ] Multi-language support
- [ ] Interview question generator
- [ ] Skill gap learning path suggestions

---

## 📁 Project Structure

```
job-application-intelligence/
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (not in git)
├── .env.example           # Example environment file
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── screenshots/          # UI screenshots
```

---

## 🙏 Acknowledgments

This project was developed as part of the **AICTE Internship Program** sponsored by:

- **EduSkills Foundation** - For providing the learning platform and internship opportunity
- **IBM SkillsBuild** - For technical resources and cloud credits
- **All India Council for Technical Education (AICTE)** - For facilitating industry-academia collaboration

**Special Thanks:**
- Google AI for Gemini API access
- LangChain community for excellent documentation
- Streamlit team for the amazing web framework

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Rohit Bedse 
AICTE Intern | EduNet Foundation & IBM SkillsBuild  
[LinkedIn](#) | [GitHub](#) | [Email](#)

---

