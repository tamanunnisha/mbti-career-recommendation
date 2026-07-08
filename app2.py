from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
mbti_data = {

"INTJ": {
    "name": "Introverted Intuitive Thinking Judging",
    "keywords": "Strategic, Analytical, Independent",
    "jobs": {
        "AI Engineer": {
            "skills": "Python, Machine Learning, Deep Learning",
            "link": "https://www.coursera.org/search?query=artificial%20intelligence"
        },
        "Data Scientist": {
            "skills": "Python, SQL, Data Analysis",
            "link": "https://www.coursera.org/search?query=data%20science"
        },
        "Software Architect": {
            "skills": "System Design, Java, Cloud Computing",
            "link": "https://www.coursera.org/search?query=software%20architecture"
        }
    }
},

"INTP": {
    "name": "Introverted Intuitive Thinking Perceiving",
    "keywords": "Logical, Curious, Innovative",
    "jobs": {
        "Software Developer": {
            "skills": "Python, Algorithms, Problem Solving",
            "link": "https://www.coursera.org/search?query=programming"
        },
        "ML Engineer": {
            "skills": "Python, Machine Learning, Statistics",
            "link": "https://www.coursera.org/search?query=machine%20learning"
        },
        "Blockchain Developer": {
            "skills": "Solidity, Cryptography, Smart Contracts",
            "link": "https://www.coursera.org/search?query=blockchain"
        }
    }
},

"ENTJ": {
    "name": "Extroverted Intuitive Thinking Judging",
    "keywords": "Leader, Strategic, Confident",
    "jobs": {
        "Product Manager": {
            "skills": "Leadership, Communication, Agile",
            "link": "https://www.coursera.org/search?query=product%20management"
        },
        "Tech Lead": {
            "skills": "System Design, Java, Team Management",
            "link": "https://www.coursera.org/search?query=software%20engineering"
        },
        "Startup Founder": {
            "skills": "Entrepreneurship, Strategy, Innovation",
            "link": "https://www.coursera.org/search?query=entrepreneurship"
        }
    }
},

"ENTP": {
    "name": "Extroverted Intuitive Thinking Perceiving",
    "keywords": "Innovative, Curious, Energetic",
    "jobs": {
        "Startup Founder": {
            "skills": "Creativity, Business Strategy, Leadership",
            "link": "https://www.coursera.org/search?query=startup"
        },
        "Innovation Manager": {
            "skills": "Problem Solving, Strategy, Design Thinking",
            "link": "https://www.coursera.org/search?query=innovation"
        },
        "Software Engineer": {
            "skills": "Programming, Data Structures, Debugging",
            "link": "https://www.coursera.org/search?query=software%20engineering"
        }
    }
},

"INFJ": {
    "name": "Introverted Intuitive Feeling Judging",
    "keywords": "Insightful, Visionary, Empathetic",
    "jobs": {
        "UX Designer": {
            "skills": "User Research, Wireframing, Design Tools",
            "link": "https://www.coursera.org/search?query=ux%20design"
        },
        "Data Analyst": {
            "skills": "Excel, SQL, Data Visualization",
            "link": "https://www.coursera.org/search?query=data%20analytics"
        },
        "AI Ethics Researcher": {
            "skills": "Ethics, AI Concepts, Research",
            "link": "https://www.coursera.org/search?query=ai%20ethics"
        }
    }
},

"INFP": {
    "name": "Introverted Intuitive Feeling Perceiving",
    "keywords": "Creative, Idealistic, Curious",
    "jobs": {
        "UI/UX Designer": {
            "skills": "Creativity, Figma, User Research",
            "link": "https://www.coursera.org/search?query=ui%20ux"
        },
        "Content Developer": {
            "skills": "Writing, Creativity, SEO",
            "link": "https://www.coursera.org/search?query=content%20writing"
        },
        "Game Designer": {
            "skills": "Game Design, Creativity, Storytelling",
            "link": "https://www.coursera.org/search?query=game%20design"
        }
    }
},

"ENFJ": {
    "name": "Extroverted Intuitive Feeling Judging",
    "keywords": "Inspiring, Leader, Supportive",
    "jobs": {
        "Product Manager": {
            "skills": "Leadership, Communication, Planning",
            "link": "https://www.coursera.org/search?query=product%20management"
        },
        "HR Tech Specialist": {
            "skills": "HR Analytics, Communication, Tools",
            "link": "https://www.coursera.org/search?query=hr%20analytics"
        },
        "Coach/Mentor": {
            "skills": "Guidance, Communication, Empathy",
            "link": "https://www.coursera.org/search?query=coaching"
        }
    }
},

"ENFP": {
    "name": "Extroverted Intuitive Feeling Perceiving",
    "keywords": "Energetic, Creative, Social",
    "jobs": {
        "Digital Marketer": {
            "skills": "SEO, Social Media, Analytics",
            "link": "https://www.coursera.org/search?query=digital%20marketing"
        },
        "Content Creator": {
            "skills": "Creativity, Video Editing, Storytelling",
            "link": "https://www.coursera.org/search?query=content%20creation"
        },
        "UX Researcher": {
            "skills": "Research, Analysis, Communication",
            "link": "https://www.coursera.org/search?query=ux%20research"
        }
    }
},

"ISTJ": {
    "name": "Introverted Sensing Thinking Judging",
    "keywords": "Organized, Responsible, Practical",
    "jobs": {
        "System Administrator": {
            "skills": "Linux, Networking, Security",
            "link": "https://www.coursera.org/search?query=system%20administration"
        },
        "Database Administrator": {
            "skills": "SQL, Database Design, Backup",
            "link": "https://www.coursera.org/search?query=sql"
        },
        "Cybersecurity Analyst": {
            "skills": "Security, Networking, Risk Analysis",
            "link": "https://www.coursera.org/search?query=cybersecurity"
        }
    }
},

"ISFJ": {
    "name": "Introverted Sensing Feeling Judging",
    "keywords": "Supportive, Loyal, Detail-oriented",
    "jobs": {
        "QA Tester": {
            "skills": "Testing, Bug Tracking, Automation",
            "link": "https://www.coursera.org/search?query=software%20testing"
        },
        "Technical Support": {
            "skills": "Troubleshooting, Communication, Systems",
            "link": "https://www.coursera.org/search?query=it%20support"
        },
        "HR Tech Specialist": {
            "skills": "HR Tools, Data, Communication",
            "link": "https://www.coursera.org/search?query=hr%20analytics"
        }
    }
},

"ESTJ": {
    "name": "Extroverted Sensing Thinking Judging",
    "keywords": "Efficient, Organized, Leader",
    "jobs": {
        "Project Manager": {
            "skills": "Planning, Leadership, Scheduling",
            "link": "https://www.coursera.org/search?query=project%20management"
        },
        "IT Manager": {
            "skills": "Management, Networking, Systems",
            "link": "https://www.coursera.org/search?query=it%20management"
        },
        "Operations Manager": {
            "skills": "Operations, Strategy, Leadership",
            "link": "https://www.coursera.org/search?query=operations"
        }
    }
},

"ESFJ": {
    "name": "Extroverted Sensing Feeling Judging",
    "keywords": "Friendly, Organized, Supportive",
    "jobs": {
        "HR Manager": {
            "skills": "Recruitment, Communication, Management",
            "link": "https://www.coursera.org/search?query=human%20resources"
        },
        "Customer Success Manager": {
            "skills": "Communication, CRM, Problem Solving",
            "link": "https://www.coursera.org/search?query=customer%20success"
        },
        "Event Coordinator": {
            "skills": "Planning, Communication, Organization",
            "link": "https://www.coursera.org/search?query=event%20management"
        }
    }
},

"ISTP": {
    "name": "Introverted Sensing Thinking Perceiving",
    "keywords": "Practical, Independent, Problem-solver",
    "jobs": {
        "DevOps Engineer": {
            "skills": "Docker, CI/CD, Linux",
            "link": "https://www.coursera.org/search?query=devops"
        },
        "Hardware Engineer": {
            "skills": "Electronics, Embedded Systems, Debugging",
            "link": "https://www.coursera.org/search?query=hardware"
        },
        "Cybersecurity Specialist": {
            "skills": "Security, Networking, Ethical Hacking",
            "link": "https://www.coursera.org/search?query=cybersecurity"
        }
    }
},

"ISFP": {
    "name": "Introverted Sensing Feeling Perceiving",
    "keywords": "Artistic, Sensitive, Flexible",
    "jobs": {
        "UI Designer": {
            "skills": "Design, Figma, Creativity",
            "link": "https://www.coursera.org/search?query=ui%20design"
        },
        "Graphic Designer": {
            "skills": "Photoshop, Creativity, Branding",
            "link": "https://www.coursera.org/search?query=graphic%20design"
        },
        "Animator": {
            "skills": "Animation, Creativity, Tools",
            "link": "https://www.coursera.org/search?query=animation"
        }
    }
},

"ESTP": {
    "name": "Extroverted Sensing Thinking Perceiving",
    "keywords": "Energetic, Practical, Bold",
    "jobs": {
        "Network Engineer": {
            "skills": "Networking, Routing, Troubleshooting",
            "link": "https://www.coursera.org/search?query=networking"
        },
        "Sales Engineer": {
            "skills": "Sales, Technical Knowledge, Communication",
            "link": "https://www.coursera.org/search?query=sales"
        },
        "Technical Consultant": {
            "skills": "Consulting, Problem Solving, Communication",
            "link": "https://www.coursera.org/search?query=consulting"
        }
    }
},

"ESFP": {
    "name": "Extroverted Sensing Feeling Perceiving",
    "keywords": "Fun-loving, Energetic, Social",
    "jobs": {
        "Social Media Manager": {
            "skills": "Social Media, Content, Analytics",
            "link": "https://www.coursera.org/search?query=social%20media"
        },
        "Brand Manager": {
            "skills": "Branding, Marketing, Strategy",
            "link": "https://www.coursera.org/search?query=branding"
        },
        "Content Creator": {
            "skills": "Video Editing, Creativity, Storytelling",
            "link": "https://www.coursera.org/search?query=video%20editing"
        }
    }
}

}

# -------- LOAD DATA & TRAIN MODELS --------
df = pd.read_csv("dataset_1000_fixed.csv")

X = df[[f"Q{i}" for i in range(1, 21)]]

y_EI = df['EI']
y_SN = df['SN']
y_TF = df['TF']
y_JP = df['JP']

model_EI = RandomForestClassifier()
model_SN = RandomForestClassifier()
model_TF = RandomForestClassifier()
model_JP = RandomForestClassifier()

model_EI.fit(X, y_EI)
model_SN.fit(X, y_SN)
model_TF.fit(X, y_TF)
model_JP.fit(X, y_JP)

# -------- ROUTES --------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get 20 answers
    answers = [int(request.form[f"Q{i}"]) for i in range(1, 21)]

    # Convert to DataFrame (important fix)
    input_df = pd.DataFrame([answers], columns=[f"Q{i}" for i in range(1, 21)])

    # Predict
    ei = model_EI.predict(input_df)[0]
    sn = model_SN.predict(input_df)[0]
    tf = model_TF.predict(input_df)[0]
    jp = model_JP.predict(input_df)[0]

    mbti = ei + sn + tf + jp

    data = mbti_data.get(mbti)

    return render_template(
    "result.html",
    result=mbti,
    full_form=data["name"],
    keywords=data["keywords"],
    jobs=data["jobs"]
)


if __name__ == '__main__':
    app.run(debug=True)