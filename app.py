from flask import Flask, render_template, request, jsonify, send_file
#import pandas as pd
import datetime

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')  # Ensure 'index.html' is in the 'templates' folder

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    data = request.get_json()
    
    start_time = data['startTime']
    end_time = data['endTime']
    interview_duration = data['interviewDuration']
    break_duration = data['breakDuration']
    candidates_per_day = data['candidatesPerDay']
    start_day = data['startDay']
    weeks = data['weeks']
    candidates = data['candidates']
    
    

    schedule = []
    current_day = datetime.datetime.strptime(start_day, '%A')
    current_time = datetime.datetime.strptime(start_time, '%H:%M')
    end_time_dt = datetime.datetime.strptime(end_time, '%H:%M')

    candidate_index = 0
    for week in range(weeks):
        for day in range(5):  # Monday to Friday
            interviews_today = 0
            while current_time < end_time_dt and candidate_index < len(candidates) and interviews_today < candidates_per_day:
                schedule.append({
                    'Day': current_day.strftime('%A'),
                    'Interview start at': current_time.strftime('%H:%M %p'),
                    'Duration of the interview in mins': interview_duration,
                    'Candidate': candidates[candidate_index]['name'],
                    'Phone': candidates[candidate_index]['phone']
                })
                current_time += datetime.timedelta(minutes=interview_duration)
                candidate_index += 1
                interviews_today += 1

                #if interviews_today % 3 == 0 and break_duration > 0:
                #This line to put breaks between each Candidate
                current_time += datetime.timedelta(minutes=break_duration)

            current_day += datetime.timedelta(days=1)
            current_time = datetime.datetime.strptime(start_time, '%H:%M')
        


    return jsonify({'schedule': schedule})

if __name__ == '__main__':
    app.run(debug=True)
