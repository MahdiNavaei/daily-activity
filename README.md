# Daily Engineering Activity Tracker

یک سیستم خودکار برای ثبت فعالیت‌های روزانه مهندسی AI/ML که به صورت طبیعی و حرفه‌ای commit های منظم در GitHub ایجاد می‌کند.

## ✨ ویژگی‌ها

- ✅ ثبت خودکار فعالیت‌های واقعی AI/ML Engineering
- ✅ Commit message های متنوع و طبیعی
- ✅ محتوای حرفه‌ای بر اساس تخصص‌های Senior AI/ML Engineer
- ✅ استفاده از GitHub Actions برای خودکارسازی کامل
- ✅ فعالیت‌های متنوع: ML Development, Data Engineering, Research, Infrastructure
- ✅ گاهی اوقات به‌روزرسانی فایل‌های دیگر برای طبیعی‌تر شدن

## 🚀 نحوه استفاده

### روش 1: GitHub Actions (پیشنهادی - بدون نیاز به کامپیوتر روشن)

1. این repository را در GitHub خود push کنید
2. فایل `.github/workflows/daily-commit.yml` به صورت خودکار هر روز ساعت 9 صبح UTC (12:30 ظهر به وقت ایران) اجرا می‌شود
3. نیازی به تنظیمات اضافی نیست!

**نکته:** برای اینکه commit ها با نام شما نمایش داده شوند، در workflow فایل email و name شما تنظیم شده است.

### روش 2: اجرای محلی

#### Windows (Task Scheduler):

1. فایل `run_daily.bat` را ویرایش کنید و مسیر پروژه را تنظیم کنید
2. Task Scheduler را باز کنید و یک task جدید ایجاد کنید:
   - **Trigger:** Daily (هر روز)
   - **Action:** Start a program
   - **Program:** مسیر فایل `run_daily.bat`
   - **Time:** هر ساعت که می‌خواهید (مثلاً 9 صبح)

#### Linux/Mac (Cron):

```bash
# اضافه کردن به crontab
crontab -e

# اضافه کردن این خط (هر روز ساعت 9 صبح)
0 9 * * * cd /path/to/project && python3 update_daily.py && git add -A && git commit -m "📝 Daily engineering log update" && git push
```

## 📁 ساختار پروژه

```
.
├── daily-notes.md              # فایل یادداشت‌های روزانه
├── update_daily.py             # اسکریپت اصلی برای به‌روزرسانی
├── utils.py                    # توابع کمکی
├── config.json                 # تنظیمات پروژه
├── run_daily.bat              # اسکریپت batch برای Windows
├── .github/
│   └── workflows/
│       └── daily-commit.yml   # GitHub Actions workflow
└── README.md
```

## 🎯 فعالیت‌های پشتیبانی شده

اسکریپت فعالیت‌های زیر را به صورت تصادفی و طبیعی تولید می‌کند:

### ML/AI Development
- Fine-tuning LLM models
- RAG architecture implementation
- Semantic search pipelines
- Recommendation systems
- Model optimization
- و بیشتر...

### Data Engineering
- ETL pipelines
- Feature engineering
- Data quality checks
- SQL optimization
- و بیشتر...

### Research & Experimentation
- Model benchmarking
- Hyperparameter tuning
- Performance evaluation
- و بیشتر...

### Infrastructure
- Code refactoring
- Testing and CI/CD
- Documentation
- Monitoring setup
- و بیشتر...

## 🔧 شخصی‌سازی

می‌توانید فعالیت‌ها را در فایل `update_daily.py` شخصی‌سازی کنید:

- `ML_DEVELOPMENT`: فعالیت‌های توسعه ML/AI
- `DATA_ENGINEERING`: فعالیت‌های مهندسی داده
- `RESEARCH`: فعالیت‌های تحقیقاتی
- `INFRASTRUCTURE`: فعالیت‌های زیرساختی
- `PROJECT_SPECIFIC`: فعالیت‌های مرتبط با پروژه‌های خاص
- `COLLABORATION`: فعالیت‌های همکاری

## 📊 نمونه خروجی

هر روز یک entry جدید با این فرمت اضافه می‌شود:

```markdown
## 2025/01/15 (دی) - سه‌شنبه (Wednesday)

**Time:** 14:30

**Activities:**

1. Fine-tuning LLaMA model for domain-specific tasks
2. Optimizing transformer inference pipeline for lower latency
3. Building semantic search pipeline using sentence transformers

**Results:** achieved 2.3% improvement in model accuracy

**Tech:** Python (PyTorch, TensorFlow)

**Notes:** Good progress on the optimization task.

---
```

## ⚙️ تنظیمات پیشرفته

### تغییر زمان اجرا

در فایل `.github/workflows/daily-commit.yml` می‌توانید زمان cron را تغییر دهید:

```yaml
schedule:
  - cron: '0 9 * * *'  # ساعت 9 صبح UTC
```

### تغییر توزیع فعالیت‌ها

در `update_daily.py` می‌توانید weights را در تابع `select_activity_category()` تغییر دهید.

## 📝 نکات مهم

- ✅ Commit ها به صورت طبیعی و با محتوای واقعی ایجاد می‌شوند
- ✅ هر روز 1-4 فعالیت تصادفی اضافه می‌شود
- ✅ گاهی اوقات metrics و technical details اضافه می‌شوند
- ✅ Commit message ها متنوع هستند
- ✅ گاهی اوقات فایل‌های دیگر (config, utils) هم به‌روزرسانی می‌شوند

## 🔒 حریم خصوصی

- Email و نام شما در workflow تنظیم شده است
- می‌توانید در `.github/workflows/daily-commit.yml` تغییر دهید

## 📄 مجوز

این پروژه برای استفاده شخصی است.

---

**ساخته شده برای:** Mahdi Navaei - Senior AI/ML Engineer
