#     Python Style Guide

Simplified version for beginner programmers by John Magee based on
[http://www.python.org/dev/peps/pep-0008](Style Guide for Python Code).

##  Introduction

This simplified style guide is intended to help beginner Python progammers adhere to basic coding conventions. Properly styled computer code is more easily read and understood by humans. You may revisit code you write later, or you may work on code with other people in the future. It's important that your code is easily understood by yourself and others.

This guide is a simplified version of *Style Guide for Python Code* by Guido van Rossum and Barry Warsaw. The original document has been placed in the public domain by the authors and is available here:
[http://www.python.org/dev/peps/pep-0008]().


## Consistency

Code is read much more often than it is written. The guidelines provided here are intended to improve the
readability of code and make it consistent across the wide spectrum of Python code.  So readability counts.

A style guide is about consistency.  Consistency with this style guide is important.  Consistency within a project is more important. Consistency within one module or function is most important.

But most importantly: know when to be inconsistent -- sometimes the style guide just doesn't apply.  When in doubt, use your best judgment.  Look at other examples and decide what looks best.  And don't hesitate to ask!

Two good reasons to break a particular rule:
*  When applying the rule would make the code less readable, even for someone who is used to reading code that follows the rules.

* To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this may also be an opportunity to clean up someone else's mess.

##    Code lay-out
### Indentation

Use 4 spaces per indentation level.

For really old code that you don't want to mess up, you can continue to use 8-space tabs.

### Tabs or Spaces?

Never mix tabs and spaces.

The most popular way of indenting Python is with spaces only.

### Maximum Line Length

Limit all lines to a maximum of 79 characters.

There are still many devices around that are limited to 80 character lines; plus, limiting windows to 80 characters makes it possible to have several windows side-by-side. The default wrapping on such devices disrupts the visual structure of the code, making it more difficult to understand.  Therefore, please limit all lines to a maximum of 79 characters.

The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces.  If necessary, you can add an extra pair of parentheses around an expression, but sometimes using a backslash looks better.

### Blank Lines

Separate top-level function and class definitions with two blank lines. Method definitions inside a class are separated by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions.  Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

## Imports
### Placement    

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

**Note:** Our text violates this. Please adhere to the convention in your own code.

### Formatting

Imports should usually be on separate lines, e.g.:

Yes:

	import os
	import sys

No:  

	import sys, os

It's okay to write this though:

	from subprocess import Popen, PIPE
##   Whitespace in Expressions and Statements

### Avoid extraneous whitespace in the following situations:

Immediately inside parentheses, brackets or braces.

Yes:

	spam(ham[1], {eggs: 2})

No:  

	spam( ham[ 1 ], { eggs: 2 } )

Immediately before a comma, semicolon, or colon:

Yes:

	if x == 4: print x, y; x, y = y, x

No:

	if x == 4 : print x , y ; x , y = y , x

Immediately before the open parenthesis that starts the argument list of a function call:

Yes:

	spam(1)

No:

	spam (1)

Immediately before the open parenthesis that starts an indexing or slicing:

Yes:

	dict['key'] = list[index]

No:

	dict ['key'] = list [index]

More than one space around an assignment or other operator to align it with another.

Yes:

	x = 1
	y = 2
	long_variable = 3

No:

	x             = 1
	y             = 2
	long_variable = 3


### Places to use spaces:

Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, &lt;, &gt;, !=, &lt;&gt;, &lt;=, &gt;=, **in**, **not in**, **is**, **is not**), Booleans (**and**, **or**, **not**).

Use spaces around arithmetic operators:

Yes:

	i = i + 1
	submitted += 1
	x = x * 2 - 1
	hypot2 = x * x + y * y
	c = (a + b) * (a - b)

No:

	i=i+1
	submitted +=1
	x = x*2 - 1
	hypot2 = x*x + y*y
	c = (a+b) * (a-b)

Compound statements (multiple statements on the same line) are generally discouraged.

Yes:

	if foo == 'blah':
		do_blah_thing()
	do_one()
	do_two()
	do_three()

Rather not:

	if foo == 'blah': do_blah_thing()
	do_one(); do_two(); do_three()

## Comments

Comments that contradict the code are worse than no comments.  Always make a priority of keeping the comments up-to-date when the code changes.

Comments should be complete sentences.  If a comment is a phrase or sentence, its first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers).

If a comment is short, the period at the end can be omitted.  Block comments generally consist of one or more paragraphs built out of complete sentences, and each sentence should end in a period.

You should use two spaces after a sentence-ending period.

### Header Comments
Header comments appear at the top of a file. These lines typically include the filename, author, date, version number, and a description of what the file is for and what it contains. For class assignments, headers should also course name, number, section, instructor, and assignment
number.

The detailed file documentation is best placed in a python *docstring*
at the top of the file, rather than in ad hoc comment strings. Properly
using docstrings helps integrate your code into the python help system.

Example:

    """
    File: <filename>  
    Copyright (c) 2016 <your name>
    License: MIT

    Course: PHYS227
    Assignment: 1.1
    Date: Feb 7, 2016
    Email: somebody@mail.chapman.edu
    Name: Som Ebody
    Description: a basic start-up program.
    """

### Function Comments  

Function comments are like the description part of a header comment, but contain
information specific to what a function does. These comments should also include
a description of the purpose and expected input arguments, the expected output
values, and how error conditions are handled.

The detailed documentation of functions is best placed in a python *docstring*
after the function definition, rather than in ad hoc comment strings. Properly
using docstrings helps integrate your code into the python help system.

Example:

	def calcHypotenuse(a, b):
      """Solve the Pythagorean theorem a^2 + b^2 = c^2 for the value of c.

      Inputs: a and b are the lengths of sides of a right triangle.
      Output: c is the length of the hypotenuse.
      """
      return math.sqrt(a**2 + b**2)

Ideally your code should be self-documenting and Pythonic, so docstrings should
be used liberally. Other common conventions like littering your code with
irrelevant comment strings ##### are discouraged in favor of code clarity.

### Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code.  Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single #.

### Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement.  Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they statethe obvious.  Don't do this:

	x = x + 1       # Increment x

But sometimes, something like this  is useful:

	x = x + 1          # Compensate for border

##  Naming Conventions

There are various naming conventions used in Python and other programming languages. The two common ones we will see are lowercase_with_underscore and mixedCase (aka lowerCamelCase).

For consistency, we should stick to the mixedCase convention. Multi-word names should start with a lowercase letter, and each new word should start with a capital letter. You can never have a space within a name. For example,

	sumOfSquares
	printHappyBirthday
	totalApples

### Names to Avoid

Never use the characters `l` (lowercase letter el), `O` (uppercase letter oh), or `I` (uppercase letter eye) as single character variable names.

In some typefaces, these characters are indistinguishable from the numerals one and zero.

In general, try to avoid using single character names. There are some times when using `x`, `y`, `z` for axis names, or `a`, `b`, `c` for the sides of a triangle, or `i`, `j`, `k` for indices will make sense,  For most other cases, create names that have meaning for their function.
