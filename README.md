# Basic Testing Template

Just a basic way to run your tests in python

## Why?

Test runners usually feature multiple useless dependencies or are uncomfortable to use or have bad documentation.
Instead of investing time and my brain in a testing suite, I use a simple system of assertions coupled with functional or unit tests.

In the end all that matters is that none of the assertions fail.

## When to not use this

When you have a big project with lots of tests, chances are you will require good debugging information, go for existing test suites
or build your own (pytest is probably the best though)