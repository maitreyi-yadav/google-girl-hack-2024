# HealthNex- Disease prediction software, with Doctor suggestions

## How to run-

### 1. Frontend

FRONTEND- run python server as mentioned below, and open frontend.html file

### 2. REST API

API- Send POST Request to this endpoint
`   http://0.0.0.0:8000/api/recommend-doc
  `

- Sample Input
  ```
  {
      "symptoms" : "leg pain with difficulty to walk"
  }
  ```
- Sample Output

  ````{
  "data": [
      {
          "Osteoarthristis": "Rheumatologist"
      },
      {
          "Cervical spondylosis": "Neurologist"
      }
  ],
  "doctors": [
      [
          {
              "name": "Dr. Satvinder Kapoor",
              "experience": "30+ Years",
              "days_available": "Friday",
              "time_available": "5:00 PM to 7:00 PM",
              "specialty_name": "Rheumatologist",
              "hospital_name": "Max Hospital"
          },
          {
              "name": "Dr. Sanjay Dhall",
              "experience": "36+ Years",
              "days_available": "Wednesday",
              "time_available": "5:00 PM to 7:00 PM",
              "specialty_name": "Rheumatologist",
              "hospital_name": "Max Hospital"
          }
      ],
      [
          {
              "name": "Dr. Amit Gupta",
              "experience": "18+ Years",
              "days_available": "Monday, Wednesday, Friday",
              "time_available": "3:00 PM to 5:00 PM",
              "specialty_name": "Neurologist",
              "hospital_name": "Max Hospital"
          },
          {
              "name": "Dr. K K Jindal",
              "experience": "No Experience Mentioned",
              "days_available": "Wednesday",
              "time_available": "11:00 AM to 1:00 PM",
              "specialty_name": "Neurologist",
              "hospital_name": "Max Hospital"
          },
      ]
  ]
  }
  ````

## To run this on local machine
Ensure that python is installed on your machine.

Clone the repository and open terminal in the root directory of repository.

1. python -m venv venv
2. Activate your virtual environment(windows- ./venv/scripts/activate)
3. pip install -r requirements.txt
4. python -m pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_md-0.5.1.tar.gz
5. cd DiseasePredictor
6. python manage.py runserver 8000

Now either use POSTMAN to test the Rest API, or open frontend.html, or open localhost:8000/


