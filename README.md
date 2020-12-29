# generals-wiki
The various scripts I write to make constructing my generals-notes-wiki easier


These scripts will likely all be python tools meant to automate things I find annoying or repetitive in my work.
For example, I like python to automatically format my initialized wikipedia pages before I use the content.

We'll see what else crops up here, but for now this is strictly formatting games for use with dokuwiki

TODO: 
- Write a script for generating **themes** pages
- Fix books generator so it can handle middle names/initials
- Fix it so that it can handle articles


catch me on twitter @elenatryan



HOW I SET THIS UP --
Using MacOS Catalina


NB: Much of this needs to be done in terminal on the command line

1. edit apache configuration as root

`sudo pico /etc/apache2/httpd.conf`
(it's actually not essential to use pico or whatever. Use a text editor you're comfortable with)

Edit the file in the following ways:

Enable PHP by uncommenting line 186, changing:

`#LoadModule php7_module libexec/apache2/libphp7.so`

to

`LoadModule php7_module libexec/apache2/libphp7.so`
(delete the #)


Enable Perl by uncommenting line 187, changing:

`#LoadModule perl_module libexec/apache2/mod_perl.so`

to

`LoadModule perl_module libexec/apache2/mod_perl.so`



Enable personal websites by uncommenting the following at line 183:

`#LoadModule userdir_module libexec/apache2/mod_userdir.so`

to

`LoadModule userdir_module libexec/apache2/mod_userdir.so`



and do the same at line 520:

`#Include /private/etc/apache2/extra/httpd-userdir.conf`

to

`Include /private/etc/apache2/extra/httpd-userdir.conf`

Save and quit.

Open the file you just enabled above with:

`sudo pico /etc/apache2/extra/httpd-userdir.conf`

and uncomment the following at line 16:

`#Include /private/etc/apache2/users/*.conf`

to

`Include /private/etc/apache2/users/*.conf`

Save and exit.

Create a quick test site by doing the following:
`mkdir ~/Sites`

`echo "<html><body><h1>My site works</h1></body></html>" > ~/Sites/index.html.en`

While you are in /etc/apache2, double-check to make sure you have a user config file. It should exist at the path: /etc/apache2/users/<your short user name>.conf. 



That file may not exist and if you upgrade from an older version, you may still not have it. It does appear to be created when you create a new user. If that file doesn't exist, you will need to create it with:

`sudo pico /etc/apache2/users/<your short user name>.conf`


you want it to look something like this:

`<Directory "/Users/kevin/Sites/">`
  `Options Indexes MultiViews`
  `AllowOverride None`
  `Require all granted`
`</Directory>`

There is a chance you'll still be blocked and, if that's the case, you'll have to sort it out through the ol' Apache config file as I did. Here are some resources from which I figured out this problem:
[apple site](https://discussions.apple.com/docs/DOC-250001766)
[stack overflow](https://stackoverflow.com/questions/24583859/apache-localhost-username-not-working)

helpful apache commands for restarting the server/starting it after editing:
`sudo systemctl apache2 enable`
I think you have to do this one first? Maybe the configtest? It'll probably be pretty clear if things don't work. As ever, pay attention to error messages.
`sudo apachectl configtest`
`sudo apachectl start`
`sudo apachectl restart`


OKAY SO TO SET UP DOKUWIKI -- download source stuff into the ol' newly created Sites folder and try to navigate to the appropriate URL which for me was: 
[http://localhost/~elenaryan/dokuwiki/index.php](http://localhost/~elenaryan/dokuwiki/index.php)
