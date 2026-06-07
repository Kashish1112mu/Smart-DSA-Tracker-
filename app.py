from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from database import get_connection
from ai_engine import get_ai_suggestions, next_best_problem
app = Flask(__name__)
load_dotenv()


# Home page
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM problems ORDER BY id DESC")
    problems = cursor.fetchall()

    conn.close()

    weak_topics = set()
    recommendations = []
    
    # SAFE LOOP
    for problem in problems:
        attempts = problem.get('attempts', 0) or 0
        status = problem.get('status', '')
        topic = problem.get('topic', '')

        if attempts > 2 or status == "Not Solved":
            weak_topics.add(topic)

    # recommendations
    recommendations = [f"Practice more {t} problems" for t in weak_topics]

    solved = sum(1 for p in problems if p.get('status') == "Solved")
    total = len(problems)

    readiness = int((solved / total) * 100) if total > 0 else 0
    daily_target = 3

    remaining_percentage = max(0, 90 - readiness)

    estimated_remaining_problems = int(
    (remaining_percentage / 100) * total
    )

    days_to_target = (
        estimated_remaining_problems + daily_target - 1
    ) 

    if readiness >= 90:
        prediction = (
        "🎉 Excellent consistency detected. "
        "You are already above the 90% interview readiness mark."
    )

    elif len(weak_topics) == 0:
        prediction = (
        f"Your solving pattern looks balanced. "
        f"At your current pace of {daily_target} problems/day, "
        f"you could reach 90% readiness in approximately "
        f"{days_to_target} days."
    )

    else:
        prediction = (
        f"AI analysis indicates that your primary focus should be "
        f"{', '.join(weak_topics)}. "
        f"If you maintain a pace of "
        f"{daily_target} problems/day, you are approximately "
        f"{days_to_target} days away from achieving "
        f"90% interview readiness."
    )

    return render_template(
    'index.html',
    problems=problems,
    weak_topics=weak_topics,
    recommendations=recommendations,
    readiness=readiness,
    next_best="Keep focusing on weak topics",
    prediction=prediction
    )
# Add problem
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        name = request.form['name']
        difficulty = request.form['difficulty']
        status = request.form['status']

        topic = request.form['topic']
        platform = request.form['platform']
        attempts = int(request.form['attempts']) 
        revision_needed = 1 if 'revision_needed' in request.form else 0

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO problems
            (name, topic, difficulty, status, platform, attempts, revision_needed)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (name, topic, difficulty, status, platform, attempts, revision_needed)
        )
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add.html')


# Delete problem
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM problems WHERE id = %s", (id,))
    
    conn.commit()
    conn.close()
    
    return redirect('/')


@app.route('/ai', methods=['GET', 'POST'])
def ai():
    response = ""

    query = ""

    if request.method == 'POST':
        query = request.form.get('query', '').lower()

        if "dp" in query:
            response = "DP Roadmap: Start with Fibonacci → Knapsack → LIS → LCS → Partition DP"

        elif "graph" in query:
            response = "Graph Roadmap: BFS → DFS → Topo Sort → Dijkstra → MST (Prim/Kruskal)"

        elif "array" in query:
            response = "Array Patterns: Two pointers → Sliding window → Prefix sum → Binary search"

        elif "weak" in query:
            response = "Check dashboard for weak topics and high attempts problems"

        else:
            response = "Practice daily 2-3 problems. Focus on patterns not questions."

    return render_template("ai.html", response=response)
# Run app
if __name__ == '__main__':
    app.run(debug=True)