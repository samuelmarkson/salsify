# Salsify Coding Project

## Setup
* Make sure python is installed
* (Optional) Set up a python virtual environment: https://virtualenv.pypa.io/en/latest/ to keep this orject versions separate from your own development
* Run the `build.sh` script to install all dependecies and create the database
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
* Gunicorn - I used this lightweight server at my old job, and I knew that it was fairly easy to set up.

#### How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
* I worked on this for a total of about 4 1/2 - 5 1/2 hours.
  * 30 minutes conceptualizing how I wanted the line searching algorithm to work
  * 30 minutes setting up the Flask server, database, getting all of libraries downloaded
  * 2 1/2 hours of iterative design on my algorithm idea
  * 30 minutes of testing different edge cases
  * 1 hour of setting up gunicorn, writing the shell scripts
  * 30 minutes of cleaning up the code, removing logging statements
* Plus it took me another 1 1/2 hours to complete this questionaire.
* The biggest hurdle I had was since I was mostly using a Windows machine for devlopment, the newlines also had carriage returns. So my byte numbers kept being off, and this took me a while to track down the source of the issue. Once I figured it out, I just made sure to read the file in byte mode, which doesn't care about the type line endings at all.
* If I had unlimted time to spend on this, I would work on these things, in order
  1. Do a lot of speed tests with different chunk sizes to determine the optimal size for reading efficiency
  2. Try and think of a better way to store the data to cut down on the amount of scrolling line-by-line that has to be done. The database table solution is using a b-tree though, and then we are switching to a linear search when the it becomes easy. I guess we could store every line and its byte offset in the database, but that feels very close to just copying all of the data, which I was asked not to do.
  3. A lot of the choices I made were for the constraints of the project, but I would love to be able to use a real database
  4. The feature request for this was pretty small, but there could be some definite added features: changes to file, not reprocessing the file every time the server starts, adding more command line argument options.

#### If you were to critique your code, what would you have to say about it?
* As mentioned above, I don't like that I am using an in-memory database, and that bugs me, but I was just worried about the constraints of this exercise so I went with minimal configuration
* The code directly solves the problem as it was given to me, but if the requirements were to change, I would have to add some additional features to make it more adaptable.


