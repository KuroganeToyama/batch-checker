# Batch Mode Check
Once again, a story during my tenure as an Instructional Support Assistant. 
<br><br>
For quite a while, whenever we run batch mode to automark student submissions, the Linux machine would just decide to 
skip random students.
<br><br>
Back then, we didn't really know what was going on, so until we got it resolved (which we eventually did), we had to 
somehow find a way to assess how much the batch run got screwed up, i.e. how many students got skipped and who they were, so that 
we could manually handle them.
<br><br>
So this script was developed by me to handle that (it became useless when we fixed the issue with the machine but is nonetheless still a good sanity checker).

# Usage
`python check_skipped.py <assn> <type> [-verbose/-v] [start_time] [end_time]`
<br><br>
`assn` is the assignment number, `type` is the type of test.
<br><br>
You also have the option to make the script verbose and tell you all the stats.
<br><br>
When both `start_time` and `end_time` are not specified, the script checks for skipped students after the very first batch run.
<br><br>
When both are specified, the script checks for skipped students for subsequent batch runs, identified via the specified time period (as marksheets are already generated after the first run).

# Note
I am aware that my script doesn't follow very good coding principle, but as a good rule of thumb, you gotta make it do the job before you start caring about other stuff.
<br><br>
The script you'll see is more of a template, because I'm not gonna give away confidential info here.