#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily activity log helper for tracking engineering work
"""

import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Engineering activities
ML_DEVELOPMENT = [
    "Fine-tuning LLaMA model for domain-specific tasks",
    "Optimizing transformer inference pipeline for lower latency",
    "Implementing RAG architecture with hybrid retrieval (vector + BM25)",
    "Building semantic search pipeline using sentence transformers",
    "Training collaborative filtering model for recommendation system",
    "Developing real-time feature engineering pipeline",
    "Implementing model explainability using SHAP values",
    "Optimizing GPU inference with TensorRT",
    "Building end-to-end MLOps pipeline with monitoring",
    "Implementing A/B testing framework for model evaluation",
    "Developing time-series forecasting model using LSTM",
    "Creating prompt engineering templates for LLM applications",
    "Implementing vector database indexing for semantic search",
    "Building FastAPI microservice for model serving",
    "Optimizing batch inference for production workloads",
    "Implementing model versioning and experiment tracking",
    "Developing automated retraining pipeline",
    "Building real-time recommendation API with caching",
    "Implementing model monitoring and drift detection",
    "Creating data validation pipeline for ML features"
]

# Data engineering
DATA_ENGINEERING = [
    "Optimizing SQL queries for large-scale data processing",
    "Building ETL pipeline for feature store",
    "Implementing data quality checks and validation",
    "Creating data pipeline for real-time streaming",
    "Optimizing MongoDB aggregation queries",
    "Building data preprocessing pipeline with Pandas",
    "Implementing incremental data loading strategy",
    "Creating data schema migration scripts",
    "Building data lake architecture for ML workflows",
    "Implementing data versioning with DVC"
]

# Research
RESEARCH = [
    "Experimenting with new transformer architectures",
    "Benchmarking different embedding models for semantic search",
    "Testing various hyperparameter configurations",
    "Evaluating model performance on new datasets",
    "Researching latest papers on LLM fine-tuning techniques",
    "Comparing different RAG retrieval strategies",
    "Analyzing model performance metrics and identifying bottlenecks",
    "Testing new prompt engineering techniques",
    "Experimenting with few-shot learning approaches",
    "Researching causal inference methods for recommendation systems"
]

# Infrastructure
INFRASTRUCTURE = [
    "Refactoring code for better modularity and maintainability",
    "Adding comprehensive unit tests for ML models",
    "Improving error handling and logging in production services",
    "Optimizing Docker container images for faster deployment",
    "Setting up CI/CD pipeline for automated testing",
    "Documenting API endpoints and model architectures",
    "Reviewing and optimizing database query performance",
    "Implementing caching strategy for API responses",
    "Setting up monitoring dashboards for model metrics",
    "Improving code documentation and type hints"
]

# Project activities
PROJECT_SPECIFIC = [
    "Working on DriveShield ADAS collision prediction improvements",
    "Enhancing hybrid recommender system with new features",
    "Optimizing NL-to-SQL agent query accuracy",
    "Improving RAG knowledge engine retrieval quality",
    "Fine-tuning agentic AI workflows for better root-cause analysis",
    "Benchmarking model performance on production data",
    "Implementing new evaluation metrics for recommendation system",
    "Optimizing real-time inference latency",
    "Adding new features to recommendation API",
    "Improving model monitoring and alerting system"
]

# Collaboration
COLLABORATION = [
    "Code review for ML model implementations",
    "Mentoring junior data scientists on best practices",
    "Collaborating with product team on feature requirements",
    "Reviewing pull requests and providing feedback",
    "Participating in technical architecture discussions",
    "Sharing knowledge in team tech talks",
    "Documenting ML system design decisions",
    "Coordinating with DevOps on deployment strategies"
]

# Technical details

TECHNICAL_DETAILS = [
    "achieved 2.3% improvement in model accuracy",
    "reduced inference latency by 15ms",
    "improved precision@10 by 0.08",
    "optimized memory usage by 12%",
    "increased throughput by 25%",
    "reduced false positive rate by 3%",
    "improved recall@20 by 0.12",
    "optimized query response time by 40%",
    "reduced model size by 18%",
    "improved AUC-ROC by 0.02"
]

TECH_STACK = [
    "Python (PyTorch, TensorFlow)",
    "FastAPI",
    "PostgreSQL",
    "MongoDB",
    "Redis",
    "Docker",
    "Vector DB (Pinecone/Weaviate)",
    "MLflow",
    "Kubernetes",
    "GitHub Actions"
]

# Helper functions

def get_persian_date():
    """Convert date to Persian format"""
    now = datetime.now()
    persian_months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]
    month_name = persian_months[now.month - 1]
    return f"{now.year}/{now.month:02d}/{now.day:02d} ({month_name})"

def get_weekday_persian():
    """Get Persian weekday name"""
    weekdays = {
        'Monday': 'دوشنبه',
        'Tuesday': 'سه‌شنبه',
        'Wednesday': 'چهارشنبه',
        'Thursday': 'پنج‌شنبه',
        'Friday': 'جمعه',
        'Saturday': 'شنبه',
        'Sunday': 'یکشنبه'
    }
    return weekdays[datetime.now().strftime('%A')]

def generate_realistic_time():
    """Generate realistic work hours"""
    # Most work happens between 9 AM and 6 PM
    hour = random.randint(9, 18)
    minute = random.choice([0, 15, 30, 45])
    return f"{hour:02d}:{minute:02d}"

def select_activity_category():
    """Select activity category based on realistic distribution"""
    weights = [0.35, 0.20, 0.15, 0.15, 0.10, 0.05]  # ML dev is most common
    categories = [
        ML_DEVELOPMENT,
        DATA_ENGINEERING,
        RESEARCH,
        INFRASTRUCTURE,
        PROJECT_SPECIFIC,
        COLLABORATION
    ]
    return random.choices(categories, weights=weights)[0]

def generate_daily_entry():
    """Generate a realistic daily entry for AI/ML engineer"""
    today = datetime.now()
    date_str = get_persian_date()
    weekday_persian = get_weekday_persian()
    weekday_english = today.strftime("%A")
    time_str = generate_realistic_time()
    
    # Select 1-4 activities (realistic for a day)
    num_activities = random.choices([1, 2, 3, 4], weights=[0.15, 0.35, 0.35, 0.15])[0]
    
    activities = []
    for _ in range(num_activities):
        category = select_activity_category()
        activity = random.choice(category)
        activities.append(activity)
    
    # Build entry
    entry = f"\n## {date_str} - {weekday_persian} ({weekday_english})\n\n"
    entry += f"**Time:** {time_str}\n\n"
    entry += "**Activities:**\n\n"
    
    for i, activity in enumerate(activities, 1):
        entry += f"{i}. {activity}\n"
    
    # Add technical details (40% chance)
    if random.random() < 0.4:
        detail = random.choice(TECHNICAL_DETAILS)
        entry += f"\n**Results:** {detail}\n"
    
    # Add tech stack mention (30% chance)
    if random.random() < 0.3:
        tech = random.choice(TECH_STACK)
        entry += f"\n**Tech:** {tech}\n"
    
    # Add notes (25% chance)
    if random.random() < 0.25:
        notes = [
            "Good progress on the optimization task.",
            "Need to investigate performance bottleneck further.",
            "Ready for code review and testing.",
            "Planning next iteration improvements.",
            "Model performance looks promising.",
            "Will continue with deployment preparation tomorrow.",
            "Identified some areas for further optimization.",
            "Collaborated with team on architecture decisions."
        ]
        entry += f"\n**Notes:** {random.choice(notes)}\n"
    
    entry += "\n---\n"
    return entry

def update_daily_notes():
    """Update daily-notes.md file"""
    file_path = "daily-notes.md"
    today_str = datetime.now().strftime("%Y/%m/%d")
    
    # Check if entry already exists for today
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if today_str in content:
                print(f"✓ Entry for today ({today_str}) already exists.")
                return False
    
    # Generate and add new entry
    entry = generate_daily_entry()
    
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(entry)
    else:
        # Create file with header
        header = """# Daily Engineering Log

This file contains daily engineering activities and progress notes for AI/ML projects.

---
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(header + entry)
    
    print(f"✓ New entry added for {datetime.now().strftime('%Y-%m-%d')}")
    return True

def maybe_update_other_files():
    """Sometimes update other files to make commits more realistic"""
    # 20% chance to update a config or utils file
    if random.random() < 0.2:
        files_to_update = [
            "config.json",
            "requirements.txt",
            "utils.py",
            "README.md"
        ]
        
        for file_name in files_to_update:
            if os.path.exists(file_name):
                # Just touch the file or add a small comment
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add a timestamp comment if it's a code file
                if file_name.endswith('.py'):
                    if '# Last updated:' not in content[-200:]:  # Check last 200 chars
                        with open(file_name, 'a', encoding='utf-8') as f:
                            f.write(f"\n# Last updated: {datetime.now().strftime('%Y-%m-%d')}\n")
                        return file_name
    return None

if __name__ == "__main__":
    updated = update_daily_notes()
    other_file = maybe_update_other_files()
    
    if updated:
        print("✓ Daily notes updated successfully")
    if other_file:
        print(f"✓ Also updated: {other_file}")
