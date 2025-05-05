# RandomAlarm Backend

Backend API for the iOS app **Random Alarm**, where random alarms are 
generated in a user-defined time period. User have to solve math problems 
to stop the alarms.

## Features

- Generates random alarm times within a specified daily time range
- Math challenges required to dismiss the alarm
- FastAPI-powered REST API
- Data validation using Pydantic
- Unit tested with Pytest
- Swift-compatible (CORS configured)

## 🧪 Local Development

```bash
# Clone & install dependencies
git clone https://github.com/tobiaserdweg/randomalarm.git
cd randomalarm/backend
poetry install

# Run the server locally
poetry run uvicorn main:app --reload