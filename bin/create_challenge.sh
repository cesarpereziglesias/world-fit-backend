#!/bin/bash
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge", "owner": "", "challenge_type": "steps", "init": "2015/01/01", "end": "2015/02/28"}' http://localhost:6543/challenges
