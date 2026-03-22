from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ==========================================
# REQUIREMENT: OBJECT-ORIENTED PROGRAMMING 
# ==========================================
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    # Custom behavior method
    def check_answer(self, user_answer):
        return self.correct_option == user_answer

# ==========================================
# REQUIREMENT: DATA STRUCTURES (QUEUE - FIFO) 
# ==========================================
class CBTQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) # FIFO: Removes and returns the first item
        return None

    def is_empty(self):
        return len(self.items) == 0

# Global variables to manage test state
test_queue = CBTQueue()
current_question = None
score = 0
total_questions = 0

def load_questions():
    """Helper function to populate the queue with questions."""
    global total_questions
    test_queue.items = [] # Reset queue
    
    # Create instances of our Question class
    q1 = Question("What does OOP stand for?", 
                  ["Object-Oriented Programming", "Only Open Programs", "Out Of Print"], 
                  "Object-Oriented Programming")
    q2 = Question("Which Python framework are we using for this web app?", 
                  ["Django", "Flask", "FastAPI"], 
                  "Flask")
    q3 = Question("Which data structure uses First-In-First-Out (FIFO)?", 
                  ["Stack", "Queue", "Array"], 
                  "Queue")
    
    # Add questions to the queue
    test_queue.enqueue(q1)
    test_queue.enqueue(q2)
    test_queue.enqueue(q3)
    total_questions = 3

# ==========================================
# REQUIREMENT: THE WEB UI (FLASK ROUTES) 
# ==========================================

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/start')
def start_test():
    """Initializes the test and redirects to the first question."""
    global score, current_question
    score = 0
    load_questions()
    current_question = test_queue.dequeue()
    return redirect(url_for('test'))

@app.route('/test', methods=['GET', 'POST'])
def test():
    """Displays questions and handles answer submissions."""
    global score, current_question

    if request.method == 'POST':
        user_answer = request.form.get('option')
        
        # Check answer using the OOP method
        if current_question and current_question.check_answer(user_answer):
            score += 1

        # Load next question from the Queue
        if not test_queue.is_empty():
            current_question = test_queue.dequeue()
        else:
            current_question = None
            return redirect(url_for('result'))

    # If someone tries to access /test without starting, redirect to home
    if current_question is None:
        return redirect(url_for('home'))

    return render_template('test.html', question=current_question)

@app.route('/result')
def result():
    """Displays the final score and a timestamp."""
    # REQUIREMENT: STANDARD API (DATETIME) 
    submit_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    return render_template('result.html', score=score, total=total_questions, time=submit_time)

if __name__ == '__main__':
    app.run(debug=True)
