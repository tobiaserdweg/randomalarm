# RandomAlarm Backend

Python backend for the iOS app **Random alarm**.

The backend is in charge of

- generating a sequence of random times given the user defined parametrization
  (start and end time, number of alarms, minimum time distance between alarms),
- generating math problems of user defined difficulty.

The backend is implemented as an API using the Python library fastapi. The API
is deployed on **render.com**.

# Local development set up

First, clone the code. To do this, open the git cmd, cd to the local directory 
in which you want to run the application and execute

```
git clone "https://github.com/tobiaserdweg/randomalarm"
```

Ensure that poetry is installed in your global Python environment. Open the 
Windows powershell and create a virtual environment by executing

```
poetry install
```

In order to run application, cd to the folder *backend* and execute the 
following command

```
poetry run uvicorn app.main:app --reload
```

Open *http://127.0.0.1:8000/docs* in your browser and test the API.
