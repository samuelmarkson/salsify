# Salsify Coding Project

## Setup
* Make sure python is installed
* (Optional) Set up a python virtual environment: https://virtualenv.pypa.io/en/latest/ to keep this orject versions separate from your own development
* Run the `build.sh` script to install all dependecies and create the databse
* Run the `run.sh` script with a single argument on the file name that you want to read from. This will also start the server once the file has finished processing
  * `run.sh lorem.txt`

## Questions
#### How does your system work? (if not addressed in comments in source)
* During build, the system creates a table with two columns (line number and the byte to seek to for the start of the line).
* When the server starts, the system reads through the file once, keeping track of the total size of the already read portion. When it reaches the end of a chunk of lines (by default 5000), it records that line number and the number of bytes so far.
* When a request is made to return a certain line number, the system calculates the 'floor' of that number to the nearest chunk starting point.
* The system then retrieves that byte number from the database, it seeks to that line in the file, then reads through the file line by line until it finds the correct line.
* This line is returned.

#### How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
* Obviously, the larger the file, the longer the preprocessing will take and it will grow linearly.
* On the line lookup, since there is an index created on the `line_num` column in the database table, the lookup time should remain pretty fast. I am using SQLite for this project, and it uses a btree to store the index which I believe will keep the lookup time to growing O(logN).
- Scanning through 5000 lines of a file is trivial and can be done easily and quickly.

#### How will your system perform with 100 users? 10000 users? 1000000 users?
* The system is using Gunicorn to serve, which is very capable of handling a large number of requests. Since the lookup can be done quickly, the workers will be free ot handle other requests.

#### What documentation, websites, papers, etc did you consult in doing this assignment?
* I used the documentation pages of Flask, Gunicorn, Python, SQLite
  * http://flask.pocoo.org/docs/1.0/
  * http://docs.gunicorn.org/en/stable/index.html
  * https://docs.python.org/3/
  * https://www.sqlite.org/docs.html
* I also used a lot of Stack Overflow, but who doesn't? 
#### What third-party libraries or other tools does the system use? How did you choose each library or framework you used?
* Python - This is the language I have worked in the most and am the most comfortable in. I had also used Flask before, so I wanted to use Python for that.
* Flask - As mentioned above, I used Flask to set up small webservices before, and it can be done with very little overhead. Also, it doesn't need any kind of database backing, which was good because I did not want to have to worry about setting up a database through a build script.
* SQLite - Similarly, using an in-memory database is obviously not ideal for production, but this means that I did not have to worry about setting up anything more complicated using a build script.
#### How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
* I worked on this for a total of about 5 hours. Plus it took me another 1 1/2 hours to complete this questionaire. The biggest hurdle I had was since I was mostly using a Windows machine for devlopment, the newlines also had carriage returns. So my byte numbers kept being off, and this took me a while to track down the source of the issue. Once I figured it out, I just made sure to read the file in byte mode, which doesn't care about the line endings at all.
#### If you were to critique your code, what would you have to say about it?
* 


