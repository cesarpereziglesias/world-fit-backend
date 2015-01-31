#!/bin/bash
curl -H "Content-Type: application/json" -d '[{"value": 100, "date": "2015/01/01"}, {"value": 151, "date": "2015/01/02"}]' http://localhost:6543/users/$1/activities/steps
