# HumDataCarp

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/elliewix/humdatacarp)

## What is this?

This repository hosts lesson materials for a variety of modules that can be used for short form workshops for digitial humanities and Python.  These each presume that participants have zero programming exposure or knowledge before the workshop.

These materials aren't meant to be the only instruction in Python, but comprise a starting point for someone curious about how it looks and what they might do with it.

## What lessons are there?

### Spring 2017 Humanities Data Programming workshop

This should run as a one day intensive overview of Python for pure beginners.

#### Morning session:  [Programming-Concepts.ipynb](Programming-Concepts.ipynb)
  * This session covers some of the essential data types and Python syntax.  Again, aiming at exposure and demonstration rather than instruction in theory.

#### Afternoon session: [Programming for Humanities Data.ipynb](Programming for Humanities Data.ipynb)
  * This session walks students through a single, but complex task. The idea is to create a bag of words from within The Raven. Students are walked through the steps of lowercasing the text, removing punctionation, splitting words, and removing stop words.  Ending with an easy method of counting and exploring the words and writing out the data file with the CSV.
  * This session could stand alone from the morning session if the students were previously exposed to core programming concepts or perhaps already versed in R.  This aims at walking students through the iterative development process of trying to solve a complex text processing problem.  It also provides foundational patterns for reading in data, manipulating text, and writing out data.

### DHOxSS17 Python workshop: [Two-Hour-Beginner-Tour.ipynb](Two-Hour-Beginner-Tour.ipynb)

This is a 2 hour form hands on workshop presented as part of the "Humanities Data: A Hands on Approach to Curation" strand of the 2017 Digital Humanities at Oxford Summer School.  [http://www.dhoxss.net/](http://www.dhoxss.net/)

This lessons takes students through reading in a text file in a variety of ways to collect and analyse some information on them.  It has links to some repl.it links so that this can be run entirely online without having to install things.  However, it is designed to be platform neutral.  It would work well for any other IDE, including Jupyter Notebooks.  It would not work well, but would be possible, to use this with the interpreter.