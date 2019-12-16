# 2019fa-final-project-wjleddy

## Overview
This project uses Django to create a web application that will, for any given input Twitter handle, generate active or suspended handles that are within an edit distance of one (one deletion, one insertion, one transposition or one replacement).
It has the capability to find handles within an edit distance of two, but this leads to very long run time (and rate-limiting from the Twitter API), so I've stuck with an edit distance of one. The project was built locally with a Postgresql backend,
And is deployed here for real use. 

## Planned Next Steps
- Pretty up the interface, adding filtering and sorting to tables.
- Currently the app will only allow a base handle's similar handles to be found once a day. This is the desired behavior, but when a base handle that already exists for a given day is requested, I would like the returned result to be the page of similar handles, not a message saying that handle's already been searched.
- Clarify that users can get newer results for handles that are already in the database.