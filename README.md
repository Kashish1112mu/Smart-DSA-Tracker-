# Smart DSA Tracker

Smart DSA Tracker is a full-stack web application designed to help students systematically track their Data Structures and Algorithms preparation. The platform records problem-solving activity, identifies weak areas, monitors interview readiness, and generates personalized recommendations based on user performance.

## Overview

The application provides a centralized dashboard for managing DSA practice. By analyzing problem status, topic distribution, and attempt history, it assists users in prioritizing topics that require additional focus.

## Features

### Problem Management

* Add DSA problems with metadata
* Store topic, difficulty, platform, attempts, and revision status
* Delete existing entries
* Persistent storage using MySQL

### Performance Analytics

* Total problems tracked
* Solved and unsolved problem statistics
* Interview readiness score
* Topic-wise performance analysis

### Recommendation Engine

* Detects weak topics based on:

  * Multiple failed attempts
  * Unsolved problems
  * Revision requirements
* Generates personalized practice recommendations

### Progress Prediction

* Estimates time required to reach a target interview readiness score
* Uses current solving pace and performance metrics
* Provides actionable preparation insights

### DSA Coach

* Provides topic-specific learning roadmaps
* Supports common interview topics such as:

  * Arrays
  * Graphs
  * Dynamic Programming
  * Binary Search

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Jinja2 Templates

### Backend

* Python
* Flask

### Database

* MySQL

### Libraries

* mysql-connector-python

## System Architecture

```text
Client (Browser)
       |
       v
Flask Application
       |
       +---- Recommendation Engine
       |
       +---- DSA Coach Module
       |
       v
MySQL Database
```

## Project Structure

```text
Smart-DSA-Tracker/
│
├── app.py
├── database.py
├── ai_engine.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── Templates/
│   ├── index.html
│   ├── add.html
│   └── ai.html
│
└── static/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/smart-dsa-tracker.git
cd smart-dsa-tracker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a MySQL database:

```sql
CREATE DATABASE dsa_tracker;
```

Update database credentials in `database.py`.

### Run Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```




