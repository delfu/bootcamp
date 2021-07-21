# Week 0: The Setup

## Story

Welcome, intern, to ZaftCorp, the leading company in all things technology! You have joined the Software department working on our latest product, codenamed Project DoubleZero.

Since this is your first week, we are only trying to get you up to speed and get your computer setup. You should have already received your work laptop with the Operating System of your choice. And if your choice was Windows, we are seriously reconsidering our decision to hire you. Just kidding...

## Terminologies

- `Git`: a source version control system (SVC). It's a software that lets you take snapshot of your code/files and share it with others. It's what we'll use for most of our lessons, workshop, assignment submissions, ...

- `Github`: a cloud service/website on top of Git. Once your files are saved through Git, you can send a copy to Github to be stored on the cloud so you can access your files on any computer or share your code with others

- `IDE`: integrated development environment. A text editor that provides different tools to make coding easier. We will be using VS Code but once you're more used to it, you can opt to use any IDE you wish

- `Command Line`: a way to interact with a computer through command written using only text and special keywords. This is in contrast with `GUI`. The advantage of using `CLI` (command line interface) is the ability to script interactions so you can automate them (eg: every hour, download the top image from /r/images and set it as the background). This will also be referred to as CLI, terminal, commandline throughout this bootcamp. They all mean the exact same thing.

- `GUI`: graphical user interface. Most programs out there (web browsers, video games, mobile apps, ...) provide a GUI

- `StackOverflow`: a forum/Q&A style website where users can post a question which will likely be answered by other users.

## Setup Instructions:

1. (Windows only, not strictly required but recommended) [Enable Windows subsystems for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10): developing on Windows is not the easiest thing since it's usually missing tons of free tools/resources that available on linux/mac. But it's possible to install a lightweight Linux virtual machine to fill in the gap. There's other alternatives like [Cygwin](http://cygwin.com/) or [MingW](http://mingw-w64.org/doku.php)

2. Install Python 3.X: Python is the easiest language to get started. In this bootcamp we'll be using Python and Javascript as our main coding languages

3. Install NodeJs: Javascript is a programming language that's widely used across the internet to build the internet. Almost every single website out there uses Javascript. NodeJs is a way to use Javascript outside of the web environment and without using a browser.

4. Install Visual Studio Code. It is a free IDE to make your coding experience much easier/more pleasant. It has many extensions, add-ons, customizable settings, ... to suit any developer. There are many other IDEs out there, feel free to explore and try them out but in this bootcamp, VSCode will be the defacto setup

5. Open a command line (`cmd` on windows or `Terminal` on Mac). As explained in the Terminologies section, CLI is the way for programmers to quickly run computer commands and therefore will be the main way we will be interacting with our code for the first few weeks.

6. Verify `python` and `node` commands work in the command line. They should start up without complaint or error messages. To exit, you can use `cmd+c` hotkey to close any program opened in command line

7. Install Git. If you're on Mac/Linux, this might already be installed for you. To verify, run the `git` command in CLI.

8. At this point you're all set up! If it takes you a while to get setup or get used to all these new tools, no worries. In a professional environment, it usually takes many days/weeks for developers to get used to a setup.

## CLI tutorial:

This is a bonus section that you can skip if you're a bit more familiar with CLI but for others, read it and practice this on your own. This will be very useful for the rest of this bootcamp

1. In a `CLI`, you can still access all your files, and pretty much do anything you usually do using other programs. There's even a text based reddit browser!

2. First, try the `ls` command. It will _list_ all the files and folders present in your current folder. On Windows, it's likely inside `My Documents` and on Mac, it defaults to a folder called `Home` (we'll cover that later)

3. Next, try to the `cd` command. It allows you to _change directory_. Imagine it like double clicking on a folder. So try it with a folder you see from using the `ls` command (eg: `cd Desktop`) and try using `ls` after to see that you're indeed in a different folder with different content. Using `cd ..` will allow you to go back up one level

4. Now that you know how to move around the filesystem using only your keyboard, there's a few more commands that are commonly used. You can play with these on your own. READ everything before running the commands though

**THERE ARE NO CONFIRMATION OR UNDO. Make sure your parameters are correct. Triple check before running them.**

_note_ if you see `<something in braces>` as a command, don't write the braces. It's just a way for me to indicate that it's a parameter and you need to change it to something else. For example, if a command has `<your name>`, I will be typing `delong` not `<delong>`

- `mv` is for moving files around. This is similar to dragging a file from one folder into another. Use it by providing two additional parameters `mv <filename> <new filename>`. Combine file name with other folder names for moving across many folders. For example `mv Desktop/fileA.txt Documents/fileA.txt` will move fileA.txt out of the Desktop folder into Documents folder.

- `cp` is for copying files. Use it by providing two additional parameters `cp <filename> <new filename>`. For example `cp Desktop/fileA.txt Documents/fileA.txt` will copy fileA.txt in Desktop folder and replicate it in the Documents folder.

- `rm` is for deleting and removing files. **BE CAREFUL** . use it with a single parameter `rm <filename>` For example `rm Documents/fileA.txt` will delete that copy you made of fileA.txt file that you put into Documents

There are wayyy more commands but these should suffice for your every day needs and allows you to do most things you would with files. Once you get used to it, CLI will be many times faster than using a mouse and GUI

## Git tutorial

This section is for those who have never used Git before. It will take a long time to understand all the intricacies but this should suffice for everything you need for this bootcamp.

Git is a CLI tool that allows you to create snapshots of a folder so can you revisit previous iterations or send your changes to another programmer. It is the most popular source version control tool at the moment but there are many other tools for the same purpose. We use Git because of its popularity and it's the easiest to use.

1. Let's `clone` this repo. Repo, or Repository just means a centralized location on the internet where this folder, containing all our bootcamp code/text is stored. In this case our repo lives on Github at the [url](https://github.com/delfu/bootcamp). To clone run `git clone https://github.com/delfu/bootcamp.git` in CLI in any folder where you want the project to live in.

2. Congrats, you now have the exact same repo on your computer! You can even access these workshops without internet access. These README documents are written in a "language" called Markdown. If you prefer to read a better formatted version, you can get a VS Code extension for Markdown preview. Or you can just keep reading them on Github.

3. A git repo is nothing different from a regular folder with files/folders inside. Only difference is there's a `.git` folder inside each folder in the repo. Make sure not to delete or move that folder.

Let's make a new _branch_ this will be how we'll submit assignments. In general, this is how developer share their code to other developers who are also working on the same repo without accidentally erasing other people's work.

4. `git checkout -b <your name>-week0` this will create a new branch prefixed with your name. We'll use this convention as your assignment submission.

5. If you now type `git status` it should tell you you are on your branch now. Now everything you do will be stored in this branch and will not affect other people.

The master branch is the default branch. Usually that's the one shared with everyone and is the source of truth for a project. Writing stuff to the master branch usually involve some process (review, discussions, testing, ...)

Let's make some changes

6. Create a new file (we have not covered how to do that in CLI, so just use the regular GUI) in the week 0 folder and call it what ever you want. It can be a file with any extension you want

7. If you do `git status` again you will see git knows about the file but says it's untracked, meaning changes to it will not be saved to your branch. `git add <filename>` will add that file to the list of files that's tracked.

8. Make some content changes to that file and save. `git status` will tell you that file has some changes. `git add <filename>` again will add those new changes to your change list.

9. Now we need to do a snapshot. While all your changes have been saved to disk and git knows about them, we get to manually control when git snapshots them and save them in git permanently. This is very helpful. Say you are writing a Word document and save and closed the file. Later, you realized want to undo you changes, so you open your Word file again but you can't undo anymore :( With git, since snapshoting is a manual process you can always go back to a previous snapshot. In video game parlance, file save is like QuickSave (you only get one slot) and git snapshot is a manual save into a save slot. Git snapshot is more commonly called git commit

10. So let's do an actual git commit. `git commit -m "<some description text>"` will commit your changes into your branch, along with some description message explaining what has changed since last commit. The `"` are important.

11. Now, `git log` will show you the history of your commits along with their messages. (you might need to press `q` to escape)

12. Repeat 6 - 11 as many times as it takes for you to get comfortable with these commands. These are the 4 git commands that you'll be using 99% of the time and is how you'll save your work and submit for assignment grading.

13. Now that you have committed changes to your branch, you need to send your branch to github so the instructor can see it. `git push` will _push_ your branch to the cloud (github) and you'll be able to see it [here](https://github.com/delfu/bootcamp/branches)

Ok, you might ask, "why are we doing all this? why can't we just use Dropbox or Google Drive to share these files?" The reason is git will allow users (students and instructor) to see how a branch is different from another branch, which file got changed, which file got deleted, ... Each commit can also hold changes from many different files. If we were using Google Drive you'd need to zip the entire week 0 folder and send it and the instructor will need to unzip, look at each file to see what's changed. It's much better this way.

14. To switch between branches (eg: you want to see another student's work, or you have multiple branches, you want to see your work from a previous week, you want to get back to master, ...) `git checkout <branch name>`

This pretty much concludes Week 0 !!!! There will be other Git commands in the future, we'll cover them as we go.
