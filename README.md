# AI-Powered Student Attendance Predictor

## Project Overview
This is my project.  
The goal is to build a simple system that can predict whether a student is at risk of falling below the 75% attendance required to sit for the exam.

## Problem I'm Trying to Solve
In our college, many students get barred from exams because of low attendance and most of the time teachers find out only in the last week. I wanted to make something that can warn us earlier (maybe 3-4 weeks before) so counselors or class teachers can talk to the student.

## How It Works (very basic right now)
- I collected dummy attendance data of 100 students for the first 8 weeks (CSV file in data/ folder)
- Added some extra columns I thought matter: CGPA of previous sem, distance from home to college, number of backlogs, etc.
- Used a Random Forest model (I followed scikit-learn examples + some YouTube tutorials)
- The model tries to predict the final attendance percentage
- If predicted < 75%, it flags the student as "at risk"

## Files
- `attendance_data.csv` → dummy dataset I created
- `train_model.py` → code to train and save the model
- `predict.py` → load model and predict for new students
- `notebook.ipynb` → where I did all the experimentation

## What I Learned
- How to handle categorical variables (OneHotEncoder)
- Feature importance (found that previous semester attendance is the strongest predictor)
- Random Forest works better than simple linear regression for this

## Limitations (I know it's not perfect)
- Data is completely made up right now
- Very small dataset
- Not yet connected to real college database

## Next Steps (if I get time)
- Add real data (with permission)
- Make a simple web page where teacher can upload CSV and get list of at-risk students
- Send email alerts automatically

I wrote all the code myself (only used ChatGPT to fix some small errors and understand concepts).
