# maaun-24-dts-001-mini-cbt-project

# What the app does
This is a Mini Computer-Based Test (CBT) web application built with Python and Flask. It displays a series of questions to the user one by one, tracks their score in the background, and generates a timestamped results page when the test is finished.

# Technologies Used
* **Backend:** Python, Flask
* **Frontend:** HTML/CSS
* **Data Structure:** Queue (First-In-First-Out) used to manage the progression of test questions.
* **OOP:** Custom `Question` class used to encapsulate question data and answer validation logic.

## Features
* **Dynamic Question Rendering:** Questions are served sequentially to the user interface.
* **FIFO Queue Management:** Utilizes a custom Queue data structure to handle the flow of the exam.
* **Instant Validation:** Object-Oriented methods instantly validate user input against the correct answers.
* **Timestamped Results:** Generates a precise completion time using Python's native `datetime` API.
