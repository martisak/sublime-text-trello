# Sublime Trello

This is a package for [Sublime Text 3](http://www.sublimetext.com/3) that provides a number of useful commands for interacting with Trello (using the [Trello API](https://trello.com/docs/index.html)).

## Usage

This package allows you to navigate the data Trello provides using the Trello API. It's heavily inspired in the [File Navigator](https://github.com/Chris---/SublimeText-File-Navigator) package.

For more info on how to customize the plugin check the [settings][4].


### Navigate

If you [run][1] the `Trello: Navigate` command, you'll see your boards, and from there you can go into the Trello element structure `(Board -> List -> Card -> Actions)`.

In the [default settings][4] you can find `{ "keep_navigate_open_after_action": true }`
If you want you can set it to false on your [user settings][3] so the panel will close after each action.

### Card creation

#### 'Quick create card' and 'Create card with description'

It tries to create a Card on the last **active** List. The **active** List refers to the last List viewed using the `Trello: Navigate` command.

If you didn't use `Navigate` yet the package will display a panel explaining the situation.

### Notifications

Running `Trello: Notifications` you'll get two options, `Unread` and `Read all`.

#### Unread notifications

When you [run][1] `Trello: Unread Notifications`, you'll see the amount of unread notifications the current user has, and a *little* description of what happened, for example:

````
Total unread: 1

1) Nofitication type: commentCard
Card: Some Card
Board: Some Board
````

This could be improved a lot, but I think it's understandable (with a little bit of brain parsing) and I prefer adding some other stuff before making it prettier (pull requests are welcome!).

#### Read all notifications

This command will attempt to read all your current unread notifications. This may result in an error because more privileges are needed. The package will explain how to fix this (if you so desire) in a panel.


### Cache

By default most requests will be cached, to improve performance. When you do an action that requires the element to be realoaded, for example creating a new card in a list, the package will try to delete only that cache, maintaining the rest.

But if you make changes in the web version or by some chance elements remain cached, changes will not be reflected.

To avoid this you have two options, [run][1] the `Trello: Delete cache` command, which will clean the cache and will request everything again *or* you can switch the `use_cache` (which is true by default) option to `false` on your [user settings][3], like this:

````json
{ "use_cache": false }
````

which is not really recommended because the package will request everything on *every* request, but it's an option just in case.

## Generating Your Keys
By default the package uses a Trello app generated only to be used here. If the `token` isn't present the package will pop up a message telling you how to get it.

Basically because of the way Trello authentication works, you'll need to copy a url in your browser and pase the result in the `token` property of the [user settings][3], for example:

Url:

````
https://trello.com/1/connect?key={KEY}&name=sublime_app&response_type=token&scope=read,write
````

Options:

````json
{
    "key"   : "",
    "secret": "",
    "token" : "{token_goes_here}"
}
````

If you don't want to use the default app, you can change it by adding your own key and secret to the [user settings][3] (check the [default settings][4] to see how). You can get them from [here](https://trello.com/1/appKey/generate).

Also, if you want to enable only some access to your account, you can modify the scope of the url before pasting it in the browser, for example from `&scope=read,write` to `&scope=read` 

## All settings

````javascript
{
    // Key and secret to identify the app. If not present the default is used
    "key"   : "",
    "secret": "",

    // Access token to interact with the API (required)
    "token" : "",

    // Cache unchanged responses for better performance
    "use_cache": true,

    // After creating elements or performing an action on them the panel reopens (until exit is selected)
    "keep_navigate_open_after_action": true,

    // Use a new tab when showing the results. If it's false it'll use a panel (like the ST console)
    "results_in_new_tab": true,

    // Syntax to use when showing the text from a trello element
    "syntax_file": "Packages/Markdown/Markdown.tmLanguage",

    // Set the delemiter used to create more than one card at once in 'Create card with description'.
    // By default, if you place "<end>" after the card description placeholder you can create another card (as many as you want)
    "card_delimiter": "<end>"
}
````

## Shortcut Keys

**Windows and Linux:**

 * Navigate: `ctrl+alt+t`
 * Unread notifications: `ctrl+alt+n`

**OSX**

 * Navigate: `super+alt+t`
 * Unread notifications: `super+alt+n`


`Delete cache` and `Notifications` don't have a shortcut, but you can set it in `Preferences -> Key Bindings - User` by adding:

````json
{
    "keys": ["alt+d"], "command": "trello_delete_cache", 
    "keys": ["alt+n"], "command": "trello_notifications"
}
````

## Settings location
Preferences -> Package Settings -> Trello -> Settings - User

## Installation

### PackageControl
If you have [PackageControl](http://wbond.net/sublime_packages/package_control) installed, you can use that to install the package.

Just type `cmd-shift-p`/`ctrl-shift-p` to bring up the command pallate and pick `Package Control: Install Package` from the dropdown.

Then type `Trello` and choose this package from the dropdown. That's it!

### Manual

You can clone the repo in your `/Packages` (*Preferences -> Browse Packages...*) folder and start using/hacking it.
    
    cd ~/path/to/Packages
    git clone git://github.com/NicoSantangelo/sublime-text-trello.git Trello

## Known issues

[Curl](http://curl.haxx.se/) is required for Linux users (it should be on:
`/usr/local/sbin`, `/sbin`,  `/usr/sbin`, `/usr/local/bin`, `/usr/bin`, or `/bin`).


## Roadmap

* Checklists
* Port to ST2?
* The rest of the [Trello API](https://trello.com/docs/index.html)?
* ~~Labels~~
* ~~Don't cache requests~~
* ~~Go back option~~
* ~~Card description~~
* ~~Create Card from List~~
* ~~Create List from Board~~
* ~~Create Board~~
* ~~Print the comment somewhere when it's selected from the list of Card comments~~ (ouput panel)

## Any idea?

* Pull requests are more than welcome, you can run the tests using the [AAAPT Package](https://github.com/guillermooo/AAAPT) or in the terminal (for example: `cd path/to/Trello && python3 -m tests.test_output`).

* Another way would be adding an [issue](https://github.com/NicoSantangelo/sublime-text-trello/issues) with your feature request.

## Thanks to
* The [Trollop](https://bitbucket.org/btubbs/trollop) Python Library
* The [Sublime Github](https://github.com/bgreenlee/sublime-github) package for the awesome workaround for httplib

## Copyright

Copyright &copy; 2013+ Nicolás Santángelo. 

See LICENSE for details.

  [1]: https://github.com/NicoSantangelo/sublime-text-trello#shortcut-keys
  [2]: https://github.com/NicoSantangelo/sublime-text-trello#roadmap
  [3]: https://github.com/NicoSantangelo/sublime-text-trello#settings-location
  [4]: https://github.com/NicoSantangelo/sublime-text-trello#all-settings
