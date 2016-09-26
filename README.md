Scriptipy
=========

After installing a UNIX based distribution, one often needs to install some packages and tweak some configurations to make it really functional.

This process, done manually, can be a little cumbersome. Thus, after a while, scripting the post-installation treatment is an excellent solution.

However, without any knowledge of shell command lines, this process can get pretty tricky. This is where Scriptipy gets involved. It is a post-installation script (in Python) aiming to simplify this process. It proposes following features :

* Executing a raw command
* Appending a line to a file
* Replacing a line into a file
* Package specific actions
* Repository specific actions

It works like a DBMS, but for shell, in Python.


## Class diagrams
-----------------
[Commands](https://www.lucidchart.com/invitations/accept/0864b763-d6b5-4b8f-837d-3d79d1bb6b46)

## ToDo
-------
* _Implement file serialization (XML, JSON, DB)_
* _Implement UI_
