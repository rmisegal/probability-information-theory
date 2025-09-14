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

### 🔄 עדכון פרויקט קיים

אם כבר הורדת את הפרויקט בעבר וברצונך לעדכן לגרסה החדשה:

```bash
# נווט לתיקיית הפרויקט
cd C:\Projects\probability-information-theory

# ודא שהסביבה הוירטואלית פעילה
venv\Scripts\activate

# משוך את העדכונים האחרונים מ-GitHub
git pull origin main

# עדכן את החבילות (במקרה שהוספתי חבילות חדשות)
pip install -r requirements.txt

# בדוק שהכל עובד
python main.py --list
```

### 🚀 התקנה

#### **📋 דרישות מוקדמות:**
- **Python 3.8+** - הורד מ: https://www.python.org/downloads/
- **Git** - הורד מ: https://git-scm.com/download/win
- **Command Prompt או PowerShell** (Windows 11)

#### **📥 שלב 1: הורדת הפרויקט מ-GitHub**

פתח **Command Prompt** או **PowerShell** והרץ:

```bash
# יצירת תיקייה לפרויקט
mkdir C:\Projects
cd C:\Projects

# שכפול הרפוזיטורי
git clone https://github.com/rmisegal/probability-information-theory.git

# מעבר לתיקיית הפרויקט
cd probability-information-theory
```

#### **🐍 שלב 2: יצירת סביבה וירטואלית**

```bash
# יצירת סביבה וירטואלית
python -m venv venv

# הפעלת הסביבה הוירטואלית
venv\Scripts\activate

# וידוא שהסביבה פעילה (אמור להופיע (venv) בתחילת השורה)
```

#### **📦 שלב 3: התקנת חבילות**

```bash
# עדכון pip לגרסה האחרונה
python -m pip install --upgrade pip

# התקנת כל החבילות הנדרושות
pip install -r requirements.txt

# וידוא התקנה תקינה
pip list
```

### 💻 שימוש

#### **🧪 שלב 4: הרצת בדיקות**

```bash
# הרצת כל הטסטים
python main.py --test

# או באמצעות pytest ישירות
python -m pytest tests/ -v

# הרצת טסט ספציפי
python -m pytest tests/test_slide01.py -v
```

##### **🎯 מה לצפות לראות בבדיקות:**

**תוצאה מוצלחת תיראה כך:**
```
============================= test session starts ==============================
platform win32 -- Python 3.11.0, pytest-8.4.2, pluggy-1.6.0 -- python.exe
cachedir: .pytest_cache
rootdir: C:\Projects\probability-information-theory
collected 8 items

tests/test_slide01.py::TestSlide01::test_calculate_dice_probabilities PASSED [ 12%]
tests/test_slide01.py::TestSlide01::test_conditional_probability PASSED  [ 25%]
tests/test_slide01.py::TestSlide01::test_probability_rules PASSED        [ 37%]
tests/test_slide01.py::TestSlide01::test_simulate_dice_rolls PASSED      [ 50%]
tests/test_slide01.py::TestDataValidation::test_numpy_random_seed PASSED [ 62%]
tests/test_slide01.py::TestDataValidation::test_probability_bounds PASSED [ 75%]
tests/test_slide02.py::TestSlide02::test_generate_uniform_data PASSED    [ 87%]
tests/test_slide02.py::TestSlide02::test_uniform_properties PASSED       [100%]

============================== 8 passed in 2.11s ===============================
```

**משמעות התוצאות:**
- ✅ **PASSED** - הטסט עבר בהצלחה
- ❌ **FAILED** - הטסט נכשל (יוצג פירוט השגיאה)
- ⚠️ **SKIPPED** - הטסט דולג (בדרך כלל בגלל תלות חסרה)

**אם יש כשלים, תראה משהו כמו:**
```
FAILED tests/test_slide01.py::TestSlide01::test_calculate_dice_probabilities
AssertionError: Lists differ: [0.167, 0.167, 0.167, 0.167, 0.167, 0.167] != [0.166, 0.167, 0.167, 0.167, 0.167, 0.167]
```

**בדיקות ספציפיות שמתבצעות:**
1. **חישוב הסתברויות קובייה** - וידוא שכל פאה מקבלת הסתברות 1/6
2. **סימולציית זריקות** - בדיקה שהתוצאות קרובות לתיאוריה
3. **חוקי הסתברות** - וידוא שחוקים בסיסיים מתקיימים
4. **התפלגות אחידה** - בדיקת ממוצע ושונות תיאורטיים
5. **גבולות הסתברות** - וידוא שכל הסתברות בין 0 ל-1

#### **▶️ שלב 5: הרצת הפרויקט**

##### **הצגת אפשרויות:**
```bash
python main.py --list
```

**תוצאה צפויה:**
```
שקפים זמינים:
----------------------------------------
 1. מבוא להסתברות
 2. התפלגות אחידה
 3. התפלגות נורמלית
 4. התפלגות בינומית
 5. התפלגות פואסון
 6. מדדי נטייה מרכזית
 7. מדדי פיזור
 8. מתאם וקורלציה
 9. אנטרופיה של שאנון
10. דיברגנס KL ואנטרופיה צולבת
```

##### **הרצת שקף יחיד:**
```bash
# הרצת שקף 1
python main.py --slide 1
```

**מה יקרה:**
1. **פלט טקסט** - הסברים ותוצאות חישובים:
```
שקף 1: מבוא להסתברות
מרצה: דר. יורם סגל
============================================================
=== חישוב הסתברויות זריקת קובייה ===
הסתברות לכל תוצאה: 0.167
הסתברות למספר זוגי: 0.500
הסתברות למספר אי-זוגי: 0.500
הסתברות למספר גדול מ-4: 0.333
```

2. **גרפים אינטראקטיביים** - יפתחו חלונות matplotlib עם:
   - גרף עמודות של הסתברויות קובייה
   - היסטוגרמה של סימולציה
   - השוואה בין תיאורטי לאמפירי

3. **קבצי תמונות** - יישמרו בתיקיית השקף:
   - `dice_probability_chart.png`
   - `dice_simulation.png`

4. **שקף HTML** - יפתח בדפדפן אוטומטית

##### **הרצת כל השקפים:**
```bash
python main.py --all
```

**מה יקרה:**
- הרצה רצופה של כל 10 השקפים
- כל שקף יציג את התוכן שלו
- יווצרו עשרות גרפים וקבצי תמונות
- זמן ריצה: כ-2-3 דקות

**כותרת התוכנית תציג:**
```
======================================================================
Probability & Information Theory Project
Version: 1.0.0
Build Date: 2025-09-14
Current Time (Jerusalem): 2025-09-14 15:30:45 IST
Based on: Jon Krohn's Machine Learning Foundations series
Lecturer: Dr. Yoram Segal
======================================================================
```

##### **הרצת שקף ספציפי עם תפריט אינטראקטיבי:**
```bash
# מעבר לתיקיית שקף
cd slide01

# הרצה אינטראקטיבית
python slide01_main.py --interactive
```

**תפריט אינטראקטיבי:**
```
==================================================
שקף 1: מבוא להסתברות
==================================================
1. הצג שקף HTML
2. חשב הסתברויות בסיסיות
3. צור ויזואליזציה
4. הרץ סימולציה
5. דוגמאות לחוקי הסתברות
6. הרץ הכל
0. יציאה

בחר אפשרות (0-6):
```

#### **🌐 שלב 6: צפייה בשקפים**

השקפים יפתחו אוטומטית בדפדפן, או ניתן לפתוח ידנית:

```bash
# פתיחת שקף 1
start slide01\slide1.html

# פתיחת שקף 2
start slide02\slide2.html
```

### **📊 חשוב: עבודה עם חלונות גרפים**

#### **מה קורה כשמריצים את הקוד:**
- **חלונות matplotlib יפתחו אוטומטית** - אלו חלונות נפרדים עם הגרפים
- **התוכנית תחכה** עד שתסגרו את החלון לפני שתמשיך
- **לא ניתן להמשיך** עד שכל החלונות נסגרים

#### **איך לסגור חלונות גרפים:**
1. **לחיצה על X** - בפינה הימנית העליונה של החלון
2. **מקש ESC** - בעת מיקוד על החלון
3. **Alt+F4** - סגירה מהירה (Windows)
4. **סגירת כל החלונות** - Ctrl+Alt+T ואז סגירת terminal

#### **טיפים לעבודה עם גרפים:**
- **שמירת גרפים** - הגרפים נשמרים אוטומטית כקבצי PNG
- **צפייה מחדש** - ניתן לפתוח את קבצי ה-PNG שנשמרו
- **הרצה ללא גרפים** - השתמש בפרמטר `--no-display` (אם זמין)

#### **אם התוכנית "תקועה":**
```bash
# אם התוכנית לא מגיבה:
Ctrl+C          # עצירת התוכנית
Ctrl+Z          # השהיית התוכנית
kill -9 <PID>   # עצירה כפויה (Linux/Mac)
```

#### **הרצת טסטים - מה לצפות:**
- **חלונות יפתחו ויסגרו מהר** - זה נורמלי
- **אם חלון נשאר פתוח** - סגרו אותו ידנית
- **הטסטים ימשיכו אוטומטית** - לאחר סגירת החלונות

### 🔧 פתרון בעיות נפוצות

#### **בעיה: "Font family 'Arial Unicode MS' not found"**
**✅ תוקן בגרסה 1.0.0!**

הבעיה נפתרה אוטומטית - הקוד עודכן להשתמש בפונטים זמינים בלבד.

אם עדיין רואה אזהרות פונט:
```bash
# ודא שיש לך את הגרסה החדשה:
git pull origin main
pip install -r requirements.txt

# הרץ שוב - אמור לעבוד ללא אזהרות
python main.py --test
```

#### **בעיה: שקף HTML לא נפתח**
```bash
# ודא שקובץ ה-HTML קיים בתיקיית השקף
dir slide01\slide1.html

# פתח ידנית:
start slide01\slide1.html

# או בדפדפן:
# פתח File -> Open -> נווט לתיקיית הפרויקט -> slide01 -> slide1.html
```

#### **בעיה: Python לא מזוהה**
```bash
# הוסף Python ל-PATH או השתמש בנתיב מלא
C:\Users\[USERNAME]\AppData\Local\Programs\Python\Python311\python.exe main.py --list
```

#### **בעיה: חבילות לא מותקנות**
```bash
# וודא שהסביבה הוירטואלית פעילה
venv\Scripts\activate

# התקן חבילות בודדות
pip install numpy matplotlib seaborn scipy pandas pytest
```

#### **בעיה: שגיאות בטסטים**
```bash
# הרץ טסט בודד לאבחון
python -m pytest tests/test_slide01.py::TestSlide01::test_calculate_dice_probabilities -v
```

### 💡 טיפים שימושיים

1. **שמירת הסביבה:** תמיד הפעל `venv\Scripts\activate` לפני עבודה
2. **יציאה מהסביבה:** `deactivate`
3. **עדכון הפרויקט:** `git pull origin main`
4. **צפייה בלוגים:** הוסף `--verbose` לפקודות
5. **שמירת תוצאות:** הגרפים נשמרים אוטומטית בתיקיות השקפים

### 🎯 דוגמה מלאה להרצה
```bash
cd C:\Projects\probability-information-theory
venv\Scripts\activate
python main.py --slide 1
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

