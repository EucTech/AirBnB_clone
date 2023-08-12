Welcome to the Airbnb project. In thiss first stage, we write a command interpreter to manage your AirBnB objects. This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help us to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine


What’s a command interpreter?
A command line interpreter is any program that allows the entering of commands and then executes those commands to the operating system. It's literally an interpreter of commands.
It’s exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

How to start a command line interpreter
On Mac OS or Linux, enter python in the command line to run the interactive Python interpreter. On Windows, open Command Prompt and enter py. 

How to Use a command interpreter
You can access the command prompt in Windows OS using the program directory or using shortcut keys. Using the program directory, go to your search bar (next to the Windows icon) and type cmd. This will pop up a list of all the command prompts available on your machine, including the default windows cmd.

Examples of a command line interpreter
 DEC's DIGITAL Command Language (DCL) in OpenVMS and RSX-11, the various Unix shells (sh, ksh, csh, tcsh, zsh, Bash, etc.), CP/M's CCP, DOS' COMMAND.COM, as well as the OS/2 and the Windows CMD.
