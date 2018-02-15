# Nightly Runs Coding Challenge

Imagine that you have already written a super awesome test suite for Clover's next amazing product: *web-react.  Then you wrote a script that runs your tests and reports their results.  Your script is called `super_awesome_tests.sh`
Right now, when you run the script it will say something like:

    [<timestamp>] Super Awesome Tests not run.  Software not installed.

But if web-react is installed and running it will say something like:

    [<timestamp>] Super Awesome Tests run against version: <version> .

Your goal is to make sure your tests run against the *latest version* every night at midnight.  Your co-worker Eric has provided a script that installs web-react. He says: 

 > I put the script in /usr/local/bin, it is called install_web-react.  If you call it each night with the version you want to install, it should handle everything so that all you need to do then is run your tests.


