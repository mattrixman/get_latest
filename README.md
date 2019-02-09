# Super Awesome Nightly Test Runs 

## Scenario

You have already written a super awesome test suite for a component that Clover needs to be reliable: *web-react*.  You also have a script that runs your tests and reports their results.  Your script is called `super_awesome_tests.sh`
Right now, when you run the script it will say something like:

    [<timestamp>] Super Awesome Tests not run.  Software not installed.

But if web-react is installed it will say something like:

    [<timestamp>] Super Awesome Tests run against version: <version>

Your co-worker Eric has provided a script that installs web-react. He says:

> I put the script in /usr/local/bin.  If you call it each night with the version you want, install_web-react should handle all of the set-up so that all you need to do then is run your tests.

## Goal

Configure your machine so that the super awesome tests run against the *latest version* of web-react every night at midnight.  After a week, the output of `./view_nightly_test_runs.sh` should resemble this:

    [2018-02-17] Super Awesome Tests run against version: facd0bc
    [2018-02-18] Super Awesome Tests run against version: f3668b9
    [2018-02-19] Super Awesome Tests run against version: e8d1a8e
    [2018-02-20] Super Awesome Tests run against version: e8d1a8e
    [2018-02-21] Super Awesome Tests run against version: d122764
    [2018-02-22] Super Awesome Tests run against version: d122764
    [2018-02-23] Super Awesome Tests run against version: d122764

## Setup

To set up the challenge, do this:

    sudo ./challenge_setup.sh

This will create `/opt/clover` and set up its contents for the challenge.  It will also place the `install_web-react` script in `/usr/local/bin/`.

Then, in a separate shell, start the web server that `install_web-react` grabs artifacts from:

    cd super_awesome/site
    python -m SimpleHTTPServer 8080

## Guidelines

 - Feel free to use a browser to search for help--this is not a test of what you can remember, it is a test of what you can do

 - Feel free to use whatever technologies you are comfortable with

 - If you feel like you are stuck, it is OK to ask questions

 - *web-react* was chosen only because it is small and therefore quick to download, the actual contents of the package are not relevant to this excercie.

 - No clues, and no curve-balls were placed on your filesystem outside of this repo (except by `challenge_setup.sh` which has nothing to hide).

 - `super_awesome_tests.sh` was only provided to give you a way to "run your tests".  It should not be necessary to modify it.

 - `view_nightly_test_runs.sh` was only provided to to give you an idea of how your solution will be evaluated for correctness.  It should not be necessary to modify it.

