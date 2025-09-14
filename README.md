# פרויקט הסתברות ותורת המידע
## Probability & Information Theory Project

פרויקט מקיף להדגמת מושגים בהסתברות ותורת המידע באמצעות Python וויזואליזציות אינטראקטיביות.

**מבוסס על:** Jon Krohn's Machine Learning Foundations series  
**Based on:** Jon Krohn's Machine Learning Foundations series  
This is the companion code to lectures and videos from Jon Krohn's Machine Learning Foundations series

**מרצה:** דר. יורם סגל  
**Lecturer:** Dr. Yoram Segal

### 📋 תוכן עניינים

- [תיאור הפרויקט](#תיאור-הפרויקט)
- [מבנה הפרויקט](#מבנה-הפרויקט)
- [התקנה](#התקנה)
- [שימוש](#שימוש)
- [השקפים](#השקפים)
- [טסטים](#טסטים)
- [תרומה לפרויקט](#תרומה-לפרויקט)

### 🎯 תיאור הפרויקט

פרויקט זה מכיל 10 שקפים אינטראקטיביים המדגימים מושגים מרכזיים בהסתברות ותורת המידע:

- **התפלגויות הסתברות**: אחידה, נורמלית, בינומית, פואסון
- **מדדים סטטיסטיים**: נטייה מרכזית, פיזור, מתאם
- **תורת המידע**: אנטרופיה של שאנון, דיברגנס KL

כל שקף כולל:
- ✅ הסבר תיאורטי מפורט
- ✅ קוד Python מתועד
- ✅ ויזואליזציות אינטראקטיביות
- ✅ דוגמאות מהעולם האמיתי
- ✅ טסטים יחידה

### 📁 מבנה הפרויקט

```
probability_project/
├── main.py                    # נקודת כניסה ראשית
├── requirements.txt           # חבילות Python נדרושות
├── README.md                 # תיעוד הפרויקט
├── slide01/                  # שקף 1: מבוא להסתברות
│   ├── slide01_main.py
│   ├── __init__.py
│   └── slide01.html
├── slide02/                  # שקף 2: התפלגות אחידה
│   ├── slide02_main.py
│   ├── __init__.py
│   └── slide02.html
├── ...                       # שקפים 3-10
├── tests/                    # טסטים יחידה
│   ├── __init__.py
│   ├── test_slide01.py
│   ├── test_slide02.py
│   └── ...
└── presentation/            # קבצי המצגת HTML
    ├── slide1.html
    ├── slide2.html
    └── ...
```

### 🚀 התקנה

1. **שכפול הפרויקט**:
```bash
git clone <repository-url>
cd probability_project
```

2. **יצירת סביבה וירטואלית** (מומלץ):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# או
venv\Scripts\activate     # Windows
```

3. **התקנת חבילות**:
```bash
pip install -r requirements.txt
```

### 💻 שימוש

#### הרצת שקף יחיד
```bash
python main.py --slide 3
```

#### הרצת כל השקפים
```bash
python main.py --all
```

#### הצגת רשימת השקפים
```bash
python main.py --list
```

#### הרצת טסטים
```bash
python main.py --test
```

### 📊 השקפים

| מספר | נושא | תיאור | טכנולוגיות |
|------|------|--------|-------------|
| 01 | מבוא להסתברות | מושגי יסוד, זריקת קובייה | Chart.js |
| 02 | התפלגות אחידה | מאפיינים וויזואליזציה | Chart.js |
| 03 | התפלגות נורמלית | עקומת הפעמון, חוק 68-95-99.7 | D3.js |
| 04 | התפלגות בינומית | ניסויים בינאריים | Chart.js |
| 05 | התפלגות פואסון | אירועים נדירים | Chart.js |
| 06 | מדדי נטייה מרכזית | ממוצע, חציון, שכיח | Chart.js |
| 07 | מדדי פיזור | שונות, סטיית תקן | Chart.js |
| 08 | מתאם וקורלציה | מטריצת מתאם אינטראקטיבית | D3.js |
| 09 | אנטרופיה של שאנון | מדידת אי-ודאות | Chart.js |
| 10 | דיברגנס KL | מרחק בין התפלגויות | Chart.js |

### 🧪 טסטים

הפרויקט כולל טסטים מקיפים לכל שקף:

```bash
# הרצת כל הטסטים
pytest tests/ -v

# הרצת טסט ספציפי
pytest tests/test_slide01.py -v

# הרצה עם כיסוי קוד
pytest tests/ --cov=. --cov-report=html
```

#### סוגי טסטים:
- ✅ **טסטי יחידה**: בדיקת פונקציות בודדות
- ✅ **טסטי אינטגרציה**: בדיקת זרימת עבודה שלמה
- ✅ **טסטי נתונים**: וולידציה של תוצאות חישוביות
- ✅ **טסטי ויזואליזציה**: בדיקת יצירת גרפים

### 📈 דוגמאות קוד

#### שימוש בשקף התפלגות נורמלית:
```python
from slide03.slide03_main import generate_normal_data, create_interactive_normal_plot

# יצירת נתונים
data = generate_normal_data(mu=0, sigma=1, n_samples=1000)

# יצירת ויזואליזציה
fig = create_interactive_normal_plot()
```

#### חישוב אנטרופיה:
```python
from slide09.slide09_main import shannon_entropy

# חישוב אנטרופיה של התפלגות
probabilities = [0.25, 0.25, 0.25, 0.25]  # התפלגות אחידה
entropy = shannon_entropy(probabilities)
print(f"אנטרופיה: {entropy:.3f} ביטים")
```

### 🔧 פיתוח

#### הוספת שקף חדש:
1. צור תיקייה חדשה: `slideXX/`
2. הוסף קבצים: `slideXX_main.py`, `__init__.py`
3. צור טסט: `tests/test_slideXX.py`
4. עדכן את `main.py`

#### סטנדרטים:
- **קוד**: PEP 8, type hints
- **תיעוד**: docstrings בעברית ואנגלית
- **טסטים**: כיסוי מינימלי 80%

### 🤝 תרומה לפרויקט

1. Fork הפרויקט
2. צור branch חדש: `git checkout -b feature/amazing-feature`
3. Commit השינויים: `git commit -m 'Add amazing feature'`
4. Push ל-branch: `git push origin feature/amazing-feature`
5. פתח Pull Request

### 📝 רישיון וזכויות יוצרים

**© כל הזכויות שמורות לדר. יורם סגל**

פרויקט זה מבוסס על Jon Krohn's Machine Learning Foundations series ומהווה קוד נלווה להרצאות ולסרטונים מהסדרה.

**This is the companion code to lectures and videos from Jon Krohn's Machine Learning Foundations series**

השימוש בפרויקט זה מותר למטרות חינוכיות ומחקריות בלבד, בכפוף לאישור מראש מדר. יורם סגל.

### 👥 מחברים

- **דר. יורם סגל** - מרצה ובעל הזכויות
- **Jon Krohn** - Machine Learning Foundations series (מקור החומר)
- **Manus AI System** - פיתוח ראשוני

### 🙏 תודות

- **NumPy & SciPy** - חישובים מדעיים
- **Matplotlib & Seaborn** - ויזואליזציות
- **Chart.js & D3.js** - גרפים אינטראקטיביים
- **pytest** - מסגרת טסטים

### 📞 יצירת קשר

לשאלות, הצעות או דיווח על באגים, אנא פתח issue בפרויקט.

---

**הערה חשובה**: 
- פרויקט זה נוצר למטרות חינוכיות ומחקריות
- כל הזכויות שמורות לדר. יורם סגל
- מבוסס על Jon Krohn's Machine Learning Foundations series
- השימוש מותר בכפוף לאישור מראש

