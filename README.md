Stimulation
===
The main goal of Stimulation is to provide an adult friendly approach to popular brain-training games, that is free for public use.

Motivation
---
Stimulation was created to be a way for adults to enjoy the same sort of brain training games that children do, without feeling like they are playing childish games. Currently, existing softwares seem to target children, creating simple games that children can easily relate to. With Stimulation, adults are the target audience, so the games were created with the experiences of adults in mind, such as memorizing a blind date's number, tracking children around the house, and picking out paint colors for the walls. 

Description
---
Stimulation consists of (currently) 9 brain training games. These are based off popular memory, focus, and problem solving games. This application is meant to be an easily accessible, adult-focused way to keep the brain stimulated and an enjoyable reprise.

Brain training games have been proven to improve brain function in regards to memory recall, focus, and problem solving. Stimulation currently contain the following games:

1. Blind Date
    - Blind Date relates going on a date with number memorization. A number will be displayed in a box for 5 seconds before disappearing, and the user must commit the number to memory and input it when the text entry box appears. Game automatically ends after 10 correct answers.
2. Bookworm
    - Bookworm is a game in which the user unscrambles words. Letter boxes appear and the user must input the correct word. Game automatically ends after 10 correct answers. 
3. Editor
    - Editor relates to editing a book. Two sentences appear, and the user must identify the mistake and input the correctly spelled sentence. Game automatically ends after 10 correct answers.
4. Find the Kiddo - currently under development
    - Find the Kiddo is similar to Simon Says. A floorplan is displayed, and an image of a child will appear within the rooms, one at a time. The user must then click on the corresponding rooms, after prompted, following the pattern of the child. Game automatically ends after 5 correctly replicated patterns.
5. Maze Runner
    - Maze Runner is a maze game. The user will pick the size of the maze, then find the way "out" of the maze to the green square. Game automatically ends upon arrival at maze exit. 
6. Paint Picker
    - Paint Picker is similar to the optical illusion. A colored box will appear with a contradicting word name (text is also a different color) for 5 seconds before disappearing. User must focus on the color of the background and commit it to memory, and input the color of the background when prompted. Game automatically ends after 10 correct answers.
7. Quick Change
    - Quick Change is a subtraction problem solving game. An amount appears with a total, and another amount with amount given. User must then use the buttons to create the difference. 
8. Space Oddity - currently under development
    - Space Oddity is a find the difference game. An odd number of aliens will appear, multiple pairs(identical) and one odd alien out that has no pair. The user must click on the odd alien out. Game automatically ends after 5 correct inputs. 
9. Type Racer
    - Type Racer is similar to the online type racer game. A sentence appears, and the user must input the same sentence. Accuracy and words per minute are displayed based off user input.

*A more detailed description of how to play each game and known bugs are included in segments below.*

To code Stimulation, a relatively new framework was used, Pygame Gui (referred to as PyGui in this README). PyGui uses Pygame and Python code chunks to create a developer friendly user interface. PyGui was chosen as it simplified creating windows, displays, buttons, sliders, and other interactable elements within Python.

Some challenges within this application include lack of documentation. As PyGui is relatively new, there are not many tutorials or 3rd party documentation on how to use the classes. Most of the coding effort was done through studying the API reference and extensive testing. Also, PyGui advertised as simple to use with Pygame, and there were some implementation issues when trying to execute pygame files within Stimulation.

Future development plans:
  - elevating the current design of the application and games to make them more engaging. 
  - implementing levels of difficulty
  - implementing a national leaderboard
  - implementing profiles for users to track personal progress
  - implementing more games to include a larger variety

How to Install and Run Stimulation
---
User must have the following installed: Python

Use pip to install the following libraries:

-pip install pygame, pygame_gui, requests

Ensure folder labeled "images", with 4 images within, is in the same execution folder as the python codes.
Ensure all 3 json files are in the same execution folder as the python codes. 

Execute the application from the Stimulation.py file through either an IDE or from the terminal. 


How to Use Stimulation
---

Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Known Bugs
---
Bookworm
- generated letters contain an apostrophe
  - user is unable to enter apostrophes, and causes an infinite loop of "Incorrect" responses
- letter buttons currently not in use
  - clicking buttons do not apply text to text entry

Type Racer
- generated window takes over display
  - after exiting game user can still see Type Racer display behind the current window

Maze Runner
- generated window appears in top right corner

Credits
---
Christiana Taylor (main contributor) - [https://github.com/catwoman2209]

Tanner Kellogg - [https://github.com/perennat]

Sean Criswell - [https://github.com/SeanCris]

Abigayle McVaney - [https://github.com/amcvaney]

License
---
GNU LESSER GENERAL PUBLIC LICENSE

Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

* Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

* Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
