## Please read this README.

### To Run This Code:
- This code uses only Python builtins. So you don't need a dependency manager like pip, and you don't need to pull down any libraries. If your machine has Python 3.+, you should be good to go.
- Run this code from the command line by navigating to this directory and using the command `$ python command_line_find_apex.py FILENAME`. Optionally, you can set the working data limit: `$ python command_line_find_apex.py FILENAME --working_data_limit=WORKING_DATA_LIMIT`.
- Run any test by navigating to the `find_apex_solution` directory and running the command `python test_file_name.py`. There is a test file for the `find_apex` functions, a test file for the `process_file` function, a test file for benchmarking speed, and a test file for benchmarking resource use.

### How this Code Works:
- The function `process_file` in `process_file.py` accepts a required filename parameter and an optional `working_data_limit` parameter. Comments in the code itself explain `working_data_limit`. 
- `process_file` has, as a dependency, a function called `find_apex_iterative` which is in the file `find_apex.py` (the `ApexNotFoundException` is also in there for now).

### What you will learn about me from this code:
- How I navigate the tradeoff between speed and resource use
- How I make decisions about naming
- How I make decisions to simplify and streamline my code

### What you will NOT learn about me from this code:
- How I architect large applications or complex solutions
- How I handle automated testing, containerization, or deployment on a production app
- How I organize files (they're all in one directory for now because this is not a prod solution and path management in Python creates enough overhead that it didn't make sense for a one hour challenge)
- How I choose libraries (I don't have not-invented-here syndrome, I promise. For an actual app where it makes sense to use a library, I use one).
- How I solve a problem I have, say, a day on, rather than an hour :)

### Decisions that affected resource usage and latency characteristics:
- For files that exceed a predetermined resource limit, `process_file` processes the file in batches to avoid going over the resource limit.
- `find_apex` uses a binary search strategy whose number of steps increase with the log of the number of lines in the file. Python has a builtin `bisect` for binary search, but it is really designed for use on insertion, not search, and specifically for searching for a given integer in an already-sorted list. We're instead searching for an apex, so binary search here is implemented from scratch.
-  The `find_apex_iterative` code uses an iterative approach to binary search rather than a recursive implementation because Python does not have tail call optimization, and the iterative approach prevents the situation of pushing a new Frame onto the stack for every additional call to a recursive function.
- Batches are processed from the beginning of the file to the end, rather than with a binary search strategy. This was originally for client-side simplicity, but it turns out that TRYING to identify the batch containing the apex with binary search puts the hurt on iops (file I/O is heavily optimized for streaming through the file).
- File I/O reads the lines in as strings and converting strings to numbers is computationally expensive enough that we ONLY convert the lines that we need (the last two each batch, and then the lines we need to compare to check for the presence of an apex). **A note:** for VERY VERY small batch sizes, this is actually gonna be more expensive than just converting everything. But for a case of a reasonably large batch size, it saves on resources.
