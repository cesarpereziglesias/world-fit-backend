#!/bin/bash
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge 1", "owner": "", "challenge_type": "steps", "init": "2015/01/01", "end": "2015/02/28"}' http://ccbsoftware.com:6543/challenges
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge 2", "owner": "", "challenge_type": "steps", "init": "2015/02/01", "end": "2015/03/28"}' http://ccbsoftware.com:6543/challenges
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge 3", "owner": "", "challenge_type": "steps", "init": "2015/03/01", "end": "2015/04/28"}' http://ccbsoftware.com:6543/challenges
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge 4", "owner": "", "challenge_type": "steps", "init": "2015/04/01", "end": "2015/05/28"}' http://ccbsoftware.com:6543/challenges
curl -H "Content-Type: application/json" -d '{"name": "The Super Challenge 5", "owner": "", "challenge_type": "steps", "init": "2015/05/01", "end": "2015/06/28"}' http://ccbsoftware.com:6543/challenges
