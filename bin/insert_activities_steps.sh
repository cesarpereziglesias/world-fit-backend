#!/bin/bash
curl -H "Content-Type: application/json" -d '[{"value": 100, "date": "2015/01/01", "activity_type": "steps"}, {"value": 151, "date": "2015/01/02", "activity_type": "steps"}]' http://localhost:6543/users/$1/activities
