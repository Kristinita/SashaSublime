[![Bitcoin Donate Button](http://Kristinita.ru/Donate-files/Bitcoin-Donate-button.png)](http://Kristinita.ru/Donate-files/Bitcoin-Redirect)
[![Litecoin Donate Button](http://Kristinita.ru/Donate-files/Litecoin-Donate-button.png)](http://Kristinita.ru/Donate-files/Litecoin-Redirect)
[![PayPal Dollar button](http://Kristinita.ru/Donate-files/PayPal-Donate-Button-Dollar.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=W6MP468ZZV66Q)
[![PayPal Euro button](http://Kristinita.ru/Donate-files/PayPal-Donate-Button-Euro.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=DGT7K29LDD2HQ)  
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Release](https://img.shields.io/badge/Release-1.1.0-orange.svg)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/SashaS.svg?style=flat-square)](https://packagecontrol.io/packages/SashaS)
[![GitHub issues](https://img.shields.io/github/issues/Kristinita/SashaSublime.svg)](https://github.com/Kristinita/SashaSublime/issues)

<!-- MarkdownTOC -->

1. [Description](#description)
1. [Support](#support)
	1. [Platforms](#platforms)
	1. [Sublime Text](#sublime-text)
	1. [Syntaxes](#syntaxes)
1. [Screenshots](#screenshots)
	1. [General](#general)
		1. [Overall plan](#overall-plan)
		1. [Details](#details)
		1. [Gutter](#gutter)
		1. [Autocomplete](#autocomplete)
		1. [Tabs](#tabs)
		1. [Sidebar](#sidebar)
		1. [Indexing status](#indexing-status)
		1. [Phantom](#phantom)
	1. [Plugins](#plugins)
		1. [Sublimerge 3 + GitGutter](#sublimerge-3--gitgutter)
		1. [HexViewer](#hexviewer)
		1. [GitGutter + SublimeLinter](#gitgutter--sublimelinter)
		1. [BracketHighlighter](#brackethighlighter)
		1. [Emmet](#emmet)
		1. [Color Helper](#color-helper)
		1. [dr_months_calendar](#drmonthscalendar)
		1. [Suricate](#suricate)
	1. [Selected text Sasha](#selected-text-sasha)
		1. [Selected text](#selected-text)
		1. [Selected text when the carriage is not on text field](#selected-text-when-the-carriage-is-not-on-text-field)
		1. [Find \(Ctrl+F\) text](#find-ctrlf-text)
		1. [Find text when the carriage is out of the found text.](#find-text-when-the-carriage-is-out-of-the-found-text)
	1. [Panels and consoles](#panels-and-consoles)
		1. [GotoAnything panel](#gotoanything-panel)
		1. [Switch Project panel](#switch-project-panel)
		1. [Find and Replace panel](#find-and-replace-panel)
		1. [Console](#console)
		1. [Build System output console](#build-system-output-console)
		1. [ScopeHunter output console](#scopehunter-output-console)
	1. [Syntaxes](#syntaxes-1)
		1. [JSON](#json)
		1. [XML](#xml)
		1. [HTML](#html)
		1. [CSS](#css)
		1. [JavaScript](#javascript)
		1. [Diff](#diff)
		1. [Regular Expression](#regular-expression)
		1. [Mediawiki NG](#mediawiki-ng)
1. [Comparison of Monokai \(default color scheme\) and SashaSublime](#comparison-of-monokai-default-color-scheme-and-sashasublime)
	1. [Monokai scopes](#monokai-scopes)
	1. [SashaSublime scopes](#sashasublime-scopes)
1. [Downloading and installation](#downloading-and-installation)
	1. [Package Control](#package-control)
	1. [Git](#git)
	1. [Hub](#hub)
	1. [Manually](#manually)
1. [Activation](#activation)
	1. [Themr and Schemr](#themr-and-schemr)
	1. [Manually](#manually-1)
1. [Preferences](#preferences)
1. [Setting SashaSublime for some plugins](#setting-sashasublime-for-some-plugins)
	1. [BracketHighlighter](#brackethighlighter-1)
	1. [GitGutter](#gitgutter)
1. [Customization non-Sublime Text settings for Windows](#customization-non-sublime-text-settings-for-windows)
		1. [Active window](#active-window)
		1. [Inactive window](#inactive-window)
	1. [Changing favicon in Sublime Text 3](#changing-favicon-in-sublime-text-3)
	1. [Title Bar and window border color](#title-bar-and-window-border-color)
	1. [Winaero Tweaker](#winaero-tweaker)
		1. [Inactive Title Bar color](#inactive-title-bar-color)
		1. [Menu Bar settings](#menu-bar-settings)
		1. [Title Bar settings](#title-bar-settings)
1. [Editing SashaSublime settings](#editing-sashasublime-settings)
	1. [Editing default files](#editing-default-files)
		1. [Steps](#steps)
		1. [Problem](#problem)
	1. [Editing user files](#editing-user-files)
		1. [Steps](#steps-1)
		1. [Problem](#problem-1)
1. [Known defects](#known-defects)
	1. [SublimeLinter wrote own color scheme file in preferences](#sublimelinter-wrote-own-color-scheme-file-in-preferences)
1. [See also](#see-also)
1. [Thanks](#thanks)
1. [Contacts](#contacts)
1. [Donate](#donate)
	1. [Bitcoin](#bitcoin)
	1. [Litecoin](#litecoin)
	1. [Paypal $](#paypal-)
	1. [Paypal €](#paypal-€)
1. [License](#license)

<!-- /MarkdownTOC -->

---

---

<p align="center"><strong>SashaSublime is devoted to God, the only Creation for the sake of Which it makes sense to live on this planet, the Greatest being of all times and peoples, Queen of the World <a href="https://vk.com/hair_in_the_wind">Sasha Chernykh</a> (Kira Kenyukhova)</strong>.</p>

<p align="center"><img src="http://i.imgur.com/OJSBK4V.jpg" alt="Queen of the World Sasha Chernykh"></p>

## Description
i faced a problem that in already available themes and color schemes many elements of syntaxes have badly distinguishable an eye of color. i tried to use many themes and schemes, but the result in one of them didn't satisfy me. Therefore, i decided to write own theme/scheme; its concept:

1. **all colors of all elements are well visible**,
2. change colors made not for beauty, and for better visibility,
3. different colors for each syntax,
4. each element of syntax has to have color.

## Support

### Platforms

Windows, macOS, Linux.

### Sublime Text

Only Build 3114 and higher. Older versions of Sublime Text are not supported. Please take the automatic upgrade Sublime Text, if you wanted use SashaSublime.

Cause — [serious updating](https://forum.sublimetext.com/t/changing-scopes-in-build-3114/20088) [scopes](http://ru.stackoverflow.com/a/516668/199934) for syntaxes in new builds. After each new update Sublime Text, color schemes developers [needs to many changes](https://toster.ru/q/321006#answer_852035) color scheme files.

Example, how to view JavaScript code:

**Build 3114:**
![Build 3114](http://i.imgur.com/fTv7zgG.png)

**Build 3103:**
![Build 3103](http://i.imgur.com/9vnVBy4.png)

In Build 3103 many syntax elements are not own colors.

### Syntaxes

Supported syntaxes: JSON, XML, HTML, CSS, JavaScript, Diff, Regular Expression, Mediawiki NG, dr_months_calendar. The color scheme is incompatible with syntaxes of [CSS3](https://packagecontrol.io/packages/CSS3_Syntax) and [JavaScriptNext - ES6](https://packagecontrol.io/packages/JavaScriptNext%20-%20ES6%20Syntax). Please, use default syntax for JavaScript and CSS for compatibility with SashaSublime. If you want use SashaSublime, but in some syntaxes you want use another color scheme, please, read page 73 in «[Sublime Text Power User](http://nbviewer.jupyter.org/github/Kristinita/SashaBooks/blob/master/IT/Sublime%20Text/Sublime%20Text%20Power%20User.pdf#page=73)» book. If you want other color scheme for [Distraction Free Mode](https://www.sublimetext.com/docs/2/distraction_free.html), please, see [this answer](http://stackoverflow.com/a/15908023/5951529).

## Screenshots

Screenshots are made in the Windows 10 operating system, Sublime Text 3, Build 3114. If i make changes to my color theme and color scheme, i try not to forget to take screenshots of the changes. But Sublime Text and plugins updated, and look at my screenshots may differ from appearance to reality. If you see a discrepancy, please let me know.

### General

#### Overall plan
![SashaSublime](http://i.imgur.com/ljT5eJp.png)

#### Details
In a theme/scheme the smallest details are well visible.
![Overall plan details](http://i.imgur.com/DlrJCes.png)

#### Gutter
![Gutter](http://i.imgur.com/VqeuQtH.png)

#### Autocomplete
![Autocomplete](http://i.imgur.com/3RPAwA7.png)

#### Tabs
![Tabs](http://i.imgur.com/CTOQ9WG.png)

#### Sidebar
![Side bar](http://i.imgur.com/N8UWi1Q.png)

#### Indexing status

![Indexing status](http://i.imgur.com/FMo5NLK.png)

#### Phantom

![Phantom](http://i.imgur.com/C2aZ7oy.png)

### Plugins

####  [Sublimerge 3](http://www.sublimerge.com/sm3/) + [GitGutter](https://packagecontrol.io/packages/GitGutter)
![Sublimerge](http://i.imgur.com/YnfYXWD.png)

####  [HexViewer](https://github.com/facelessuser/HexViewer)
![Hex Viewer](http://i.imgur.com/c0t0Iqy.png)

####  [GitGutter](https://packagecontrol.io/packages/GitGutter) + [SublimeLinter](http://www.sublimelinter.com/en/latest/)
![GitGutter and SublimeLinter](http://i.imgur.com/24kzw67.png)

####  [BracketHighlighter](https://facelessuser.github.io/BracketHighlighter/)
![BracketHighlighter](http://i.imgur.com/S8SE9nh.png)

#### [Emmet](http://emmet.io/)
![Emmet](http://i.imgur.com/Arhzbgl.png)

#### [Color Helper](https://github.com/facelessuser/ColorHelper)
![Color Helper](http://i.imgur.com/ZcmyymH.png)

#### [dr_months_calendar](https://github.com/dragon/dr_months_calendar)
![dr_months_calendar](http://i.imgur.com/Pq1HXC7.png)

#### [Suricate](https://github.com/nsubiron/SublimeSuricate)

![Suricate](http://i.imgur.com/ivsdfXM.png)

If `"popup_style_file": "Packages/Suricate/css/dark.css",` in Suricate settings.

### Selected text Sasha
Results with the established [WordHighlight](https://github.com/SublimeText/WordHighlight) plugin.

#### Selected text
![Accentuation](http://i.imgur.com/yJ2EdbD.png)

#### Selected text when the carriage is not on text field
![Accentuation2](http://i.imgur.com/y715wdq.png)

#### Find (<kbd>Ctrl+F</kbd>) text
![Find result](http://i.imgur.com/Z3lGryq.png)

#### Find text when the carriage is out of the found text.
![Find result2](http://i.imgur.com/Tyqv7to.png)
Сarriage color and this border color set to the same parameter.

### Panels and consoles

#### GotoAnything panel
![GotoAnything panel](http://i.imgur.com/2hRinyv.png)

#### Switch Project panel
![Switch Project panel](http://i.imgur.com/YVcfF0k.png)

#### Find and Replace panel
![Find and Replace panel](http://i.imgur.com/H6tolbC.png)

#### Console
![Console](http://i.imgur.com/JwQyqyU.png)

#### Build System output console

For get a black and white colors, Install [SublimeANSI](https://github.com/aziz/SublimeANSI) plugin and [add](https://github.com/aziz/SublimeANSI#using-this-plugin-as-a-dependency-for-your-pluginbuild-output-panel) in your `.sublime-build` file these lines:

```json
"target": "ansi_color_build",
"syntax": "Packages/ANSIescape/ANSI.tmLanguage"
```

![Build console](http://i.imgur.com/4s81HhM.png)

#### ScopeHunter output console
![ScopeHunter console](http://i.imgur.com/CsxZ8XW.png)

### Syntaxes

#### JSON
![JSON1](http://i.imgur.com/N2LvbNZ.png)
![JSON2](http://i.imgur.com/epuwjOb.png)

With [LanguageTool](https://packagecontrol.io/packages/LanguageTool) plugin:

![JSON3](http://i.imgur.com/6kWo4aW.png)

#### XML
![XML](http://i.imgur.com/0s4EFYN.png)

#### HTML
![HTML1](http://i.imgur.com/POTMTWq.png)
![HTML2](http://i.imgur.com/LFKMdDX.png)
![HTML3](http://i.imgur.com/AbGgQa9.png)

#### CSS
![CSS](http://i.imgur.com/Rr9AmIZ.png)

#### JavaScript
It turned out to work not so carefully as i wanted.

![JS1](http://i.imgur.com/dedldIL.png)
![JS2](http://i.imgur.com/2e34vGr.png)

#### Diff
![Diff](http://i.imgur.com/AF7BgIU.png)

#### Regular Expression
![Regex1](http://i.imgur.com/kzwyA4E.png)
![Regex2](http://i.imgur.com/Fu2Slm6.png)
![Regex3](http://i.imgur.com/1kvOeeK.png)

#### Mediawiki NG
![Mediawiki1](http://i.imgur.com/Y2FYuFI.png)
![Mediawiki2](http://i.imgur.com/sSzqfsm.png)

## Comparison of Monokai (default color scheme) and SashaSublime
SashaSublime has several times more than parameters, than a default theme Monokai. See mouse cursor on the thumb of vertical scroll bar SashaSublime color scheme. Testing was carried out on [TmTheme Editor](https://tmtheme-editor.herokuapp.com). 

### Monokai scopes
![Monokai scopes](http://i.imgur.com/YITyD6A.png)

### SashaSublime scopes
![SashaSublime scopes](http://i.imgur.com/JzT6vnk.png)

## Downloading and installation

After installation, you need to activate SashaSublime, see [Activation](#Activation) section. Sublime Text no needs to be restarted after installation SashaSublime.

### Package Control

[Package Control](https://packagecontrol.io/) — package manager for Sublime Text, via Package Control you may install thousands of plugins. If you never used Package Control, make steps.

Open your Sublime Text. After Build 3124 install Package Control may quick, use `Tools` menu item: `Tools` → `Install Package Control...`.

![Install Package Control](http://i.imgur.com/JSw5Rbw.png)

<kbd>Ctrl+Shift+P</kbd> → `Package Control: Install Package`

![Install Package](http://i.imgur.com/qxOBpFq.png)

Print `SashaS`. Name package in Package Control is different right name package, because [not recommended use «Sublime» word](https://packagecontrol.io/docs/submitting_a_package#Step_2) in names of Package Control packages. 

![SashaS](http://i.imgur.com/KgvXigD.png)

### Git

`Preferences` → `Browse Packages...` → in this folder open terminal, preferable to you, and run command:

    git clone https://github.com/Kristinita/SashaSublime.git

### Hub

I recommend use [Hub](https://hub.github.com/) — a command-line wrapper for git that makes you better at GitHub.

If you use Hub, `Preferences` → `Browse Packages...` → in this folder open terminal, preferable to you, and run command:

    hub clone Kristinita/SashaSublime

### Manually

Open the page <https://github.com/Kristinita/SashaSublime> in browser. In right bottom angle select <kbd>Clone or download</kbd> and then <kbd>Download ZIP</kbd>:

![Download ZIP](http://i.imgur.com/fzvUXYo.png)

Download zip-archive and unpack it to <kbd>Alt+N</kbd> → `Browse Packages...` folder. Rename `SashaSublime-master` to `SashaSublime`.

----

As a result, your folder with SashaSublime has to settle down on the path `Preferences` → `Browse Packages...` → `SashaSublime`. For example, absolute path for me is `E:\Sublime Text 3\Data\Packages`.

## Activation

### Themr and Schemr

Install [Themr](https://github.com/benweier/Themr) plugin. <kbd>Ctrl+Shift+P</kbd> → `Themr: List themes` → `SashaSublime` → <kbd>Enter</kbd>.

![Theme SashaSublime](http://i.imgur.com/dgIVs3Y.png)

Then install [Schemr](https://github.com/benweier/Schemr) plugin. <kbd>Ctrl+Shift+P</kbd> → `Schemr: List all scheme`s → `SashaSublime  [Dark]` → <kbd>Enter</kbd>.

![Scheme SashaSublime](http://i.imgur.com/UYOiBB9.png)

### Manually

<kbd>Alt+N</kbd> → `Settings - User` → add in open file 2 lines:

```json
"color_scheme": "Packages/SashaSublime/SashaSublime.tmTheme",
"theme": "SashaSublime.sublime-theme",
```

Be attentive, [correctly place](http://ru.stackoverflow.com/a/238934/199934) commas, quotes, brackets and colons.

## Preferences

Also, you can make that all your settings were as at me. Copy into your file`Preferences` → `Settings - User` these lines from my file `Preferences` → `Preferences.sublime-settings`:

```json
"always_show_minimap_viewport": true,
"auto_find_in_selection": false,
"bold_folder_labels": true,
"caret_style": "wide",
"detect indentation": false,
"draw_indent_guides": false,
"draw_minimap_border": true,
"fade_fold_buttons": false,
"font_face": "Consolas",
"font_options":
[
    "subpixel_antialias",
    "directwrite"
],
"highlight_line": true,
"highlight_modified_tabs": true,
"line_padding_bottom": 1,
"line_padding_top": 1,
"match_brackets": false,
"match_brackets_angle": false,
"match_brackets_braces": false,
"match_brackets_content": false,
"match_brackets_square": false,
"match_tags": false,
"menu_visible": true,
"show_encoding": true,
```

Before copying save in a safe place file *Preferences.sublime-settings* from the `User` folder or, what better, use [Local History](https://github.com/vishr/local-history) plugin. If you don't like my preferences, you will be able to return to your preferable settings.


## Setting SashaSublime for some plugins

### BracketHighlighter

To paint in different colors of a bracket of a plugin of BracketHighlighter, execute the following actions:

+ Install plugin BracketHighlighter via Package Control,
+ `Preferences` → `Package Settings` → `BracketHighlighter` → `Bracket Settings - User` → add in open file this code and save file:

```json
{
    "bracket_styles": {
        "unmatched": {
            "icon": "question",
            "color": "brackethighlighter.unmatched",
            "style": "highlight"
        },
        "curly": {
            "icon": "curly_bracket",
            "color": "brackethighlighter.curly",
            "style": "highlight"
        },
        "round": {
            "icon": "round_bracket",
            "color": "brackethighlighter.round",
            "style": "outline"
        },
        "square": {
            "icon": "square_bracket",
            "color": "brackethighlighter.square",
            "style": "outline"
        },
        "angle": {
            "icon": "angle_bracket",
            "color": "brackethighlighter.angle",
            "style": "outline"
        },
        "tag": {
            "icon": "tag",
            "color": "brackethighlighter.tag",
            "style": "outline"
        },
        "single_quote": {
            "icon": "single_quote",
            "color": "brackethighlighter.quote",
            "style": "outline"
        },
        "double_quote": {
            "icon": "double_quote",
            "color": "brackethighlighter.quote",
            "style": "outline"
        },
        "regex": {
            "icon": "regex",
            "color": "brackethighlighter.quote",
            "style": "outline"
        }
    }
}
```

### GitGutter

Probably you are faced with the [same](https://github.com/jisaacks/GitGutter/issues/199#issuecomment-227016698) problem of small icons in GitGutter. To solve this problem, at first install [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin. <kbd>Ctrl+Shift+P</kbd> → `PackageResourceViewer: Extract Package` → `GitGutter`. Then `Preferences` → `Browse Packages...` → `icons` → change the already available icons to icons in folder `icons` → `GitGutter` of SashaSublime repository. Your icons for GitGutter have to replace on icons of the bigger size.

## Customization non-Sublime Text settings for Windows

Some settings not customizable via Sublime Text, to change them, you need to use other programs.

All settings in sections **Title Bar** color and **Winaero Tweaker** will affect **all** programs that do not have their own settings for these options, not only for Sublime Text. You will see the changes made, and when you open other programs.

All manuals in this section for Windows 10 users, use default theme. Users of others operating systems, please, see instructions for your OS in other sources.

If you follow all the steps in this section, you will get the result:

#### Active window
![Active window](http://i.imgur.com/AUdJEug.png)

#### Inactive window
![Inactive window](http://i.imgur.com/3E1qY10.png)

### Changing favicon in Sublime Text 3

Unfortunately, after Sublime Text updates, you will have to make this steps again.

Mac users possible help [this](http://apple.stackexchange.com/questions/153176/changing-sublime-text-3-icon-in-dock-on-yosemite) answer.

For Windows users: download and open [Resource Hacker](http://rsload.net/soft/editor/9133-resource-hacker.html) or [alternate](http://alternativeto.net/software/resource-hacker/) programs for edit *.exe* files. For example, in Resource Hacker: `File` → `Open` → *sublime_text.exe* → `Icon Group` → right mouse button on *103:3081* → `Replace Icon ...`

![Resource Hacker](http://i.imgur.com/XcLuNqS.png)

→ select *SashaSublime.ico* in `icons` → `favicon` folder of this repository → `Replace` → `File` → `Save As` → `Yes` → `Save` → restart Windows.

In Sublime Text folder *sublime_text_original.exe* file is created. If you don't like my icons, you can replace *sublime_text_original.exe* → *sublime_text.exe*. Besides, you can always replace your *sublime_text.exe* file on [original version](https://www.sublimetext.com/3) this file.

Examples, when use colors of «S» letter my favicon:

![SashaSublime.ico](http://i.imgur.com/b2DxblV.png)

+ yellow — for smallest favicons, because is good visible; use in top left angle Sublime Text 3 and in Windows Explorer,
+ blue — icons in taskbar,
+ violet — icons on desktop,
+ orange — in [Rocket Dock](http://portableapps.com/node/25965) panel and at drag and drop file with icon Sublime Text.

### Title Bar and window border color

<kbd>Win+R</kbd> → insert in input area this text

    rundll32.exe shell32.dll,Control_RunDLL desk.cpl,Advanced,@Advanced

→ <kbd>OK</kbd> → move thumbs. You can preview changes in title bar your window. I select orange color:

![Orange Title bar](http://i.imgur.com/iZDK322.png)

`Save changes`. Window border will have exactly the same color as title bar.

![Orange windows border](http://i.imgur.com/jdWUb5m.png)

### Winaero Tweaker

Install program [Winaero Tweaker](http://rsload.net/soft/optimization/19590-winaero-tweaker.html) — GUI for customization Windows 10 settings — and run it.

#### Inactive Title Bar color

`Appearance` → `Inactive Title Bars Color` → click on the square near *Current color (Click to change)* to select the color. I select pink color:

![Pink inactive Title Bar](http://i.imgur.com/ZdcNwMQ.png)

#### Menu Bar settings

`Advanced Appearance Settings` → `Menus` → change values of parameters. I select `Adjust menu height` → *27*, `font` — *Segoe UI*, `font size` — *10*.

![Menu Bar](http://i.imgur.com/TxDmEIg.png)

`Apply changes` → `Sign out now` → settings are viewed in new Windows session.

#### Title Bar settings

`Advanced Appearance Settings` → `Window Title Bars` → change values of parameters. I select `Window Title bar height` → *30*, `font` — *Segoe UI*, `font size` — *11*.

![Title bar settings](http://i.imgur.com/mFnVWxi.png)

`Apply changes` → `Sign out now` → settings are viewed in new Windows session.

## Editing SashaSublime settings

Parameters in the file of SashaSublime package are comments in Russian. You can see which color corresponds to which element. Exception — `Preferences.sublime-settings`. Comments in this file automatically [removed](https://forum.sublimetext.com/t/bug-comments-deleted-in-preferences-user/7064/6?u=sasha_chernykh). About all parameters containing in `Preferences.sublime-settings` file it is [possible to read](http://www.sublimetext.ru/documentation/preferences/list) on the Russian site Sublime Text 3.

If you don't like some colors in SashaSublime, you can change them yourself, see [detailed instructions in Russian](http://ru.stackoverflow.com/a/516668/199934). You can also find a set of other solutions on themes and schemes in other my answers on [Stack Overflow in Russian](http://ru.stackoverflow.com/search?q=user:199934%20[sublime-text]%20is:answer) and [Toster](https://toster.ru/user/Kristinita/answers).

But there're problems. You have 2 options, how to customize SashaSublime.

### Editing default files

#### Steps

Install [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin: <kbd>Ctrl+Shift+P</kbd> → `PackageResourseViewer:Open Resourse` → `SashaSublime` → edit SashaSublime files.

#### Problem

After updates, SashaSublime your changes will be lost. You will need to copy the modified file in a separate place, and after the upgrade SashaSublime, you will need to merge you changes from your file into the file of SashaSublime, for example, via [Sublimerge 3](http://www.sublimerge.com/sm3/).

### Editing user files

#### Steps

1. **Theme file**  
`Preferences` → `Browse Packages...` → `User` → create file `Example.sublime-theme`, if you want to make a changes in theme. Instead of `Example` you can name your file by any other name. Copy the contents of the file `SashaSublime.sublime-theme` into `Example.sublime-theme` make a changes and save `Example.sublime-theme` file. Via [Themr](#themr-and-schemr) select Example theme.

2. **Scheme file**  
`Preferences` → `Browse Packages...` → `User` → create file `Example.tmTheme`. Instead of `Example` you can name your file by any other name. Copy the contents of the file `SashaSublime.tmTheme` into `Example.tmTheme` make a changes and save `Example.tmTheme` file. Via [Schemr](#themr-and-schemr) select Example scheme.

#### Problem

Will be updated `SashaSublime.sublime-theme` and `SashaSublime.tmTheme` files, no `Example.sublime-theme` and `Example.tmTheme` files. You will not see updates, if you not select SashaSublime theme and scheme files. You will need to merge you changes from SashaSublime into your file, for example, via [Sublimerge 3](http://www.sublimerge.com/sm3/).

## Known defects

If you know how to solve these problems, please, [tell me](https://github.com/Kristinita/SashaSublime/issues).

+ [not change color text «Open files and folders» in placeholder](https://forum.sublimetext.com/t/how-to-style-placeholders-text-like-open-files-and-folders-in-the-find-in-files-dialog/21650),
+ [lower half of font is cut off when increasing tab_label font.size](https://github.com/SublimeTextIssues/Core/issues/694),
+ [reset Custom Settings icon after updating GitGutter](https://github.com/jisaacks/GitGutter/issues/307),
+ [Color Highlighter are generated new schemes](https://forum.sublimetext.com/t/how-to-disable-new-color-scheme-generating-color-highlighter/22949),
+ [double schemes in Schemr list if you use Color Highlighter](https://github.com/benweier/Schemr/issues/34),
+ [no syntax highlighting in *Replace With:* field](https://forum.sublimetext.com/t/where-i-can-to-make-regex-syntax-highlight-for-replace-with/22961),
+ [not working `body#inline-error` CSS selector in phantomCss](https://forum.sublimetext.com/t/how-to-change-border-color-and-square-in-error-color-for-phantomcss/23265/3?u=sasha_chernykh),
+ [font-family property not worked for «Show Definition» popups](https://github.com/SublimeTextIssues/Core/issues/1415),
+ [not change Menu Bar color in default Windows 10 theme](http://winreview.ru/forum/viewtopic.php?f=6&t=294),
+ [not change window border thickness in default Windows 10 theme](http://winreview.ru/forum/viewtopic.php?f=6&t=295),

### SublimeLinter wrote own color scheme file in preferences

If you use [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3), you may not like that Sublime Linter additional sets the color scheme in your user settings. To deactivate the color scheme SublimeLinter, follow these steps:

Install [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin → <kbd>Ctrl+Shift+P</kbd> → PackageResourceViewer: `Open Resource` → `SublimeLinter` → `lint` → `util.py` → in open file to comment out or remove line 215:

```python
sublime.set_timeout_async(generate_color_scheme_async, 0)
```

Restart Sublime Text → SublimeLinter should not prescribe in your preferences own color scheme file. Thanks [@r-stein](https://github.com/r-stein) at [solution](https://forum.sublimetext.com/t/sublimelinter-write-own-color-scheme-path-in-the-configuration-file/21842/2?u=sasha_chernykh).

## See also

+ [Kristinita's Search](http://kristinita.ru) — search engine, searching only authoritative sources, materials are written by experts on the subject.
+ [Sasha Black](http://kristinita.ru/Sasha-Black) — mini-service checks the reputation of your site and the availability of the site in the blacklists.

## Thanks

Many thanks to those who answered my questions on themes and color schemes on [Stack Overflow](http://stackoverflow.com/), [English](https://forum.sublimetext.com/) and [Russian](http://forum.sublimetext.ru) Sublime Text forums: [@Keith Hall](https://github.com/keith-hall), [@MattDMo](https://github.com/MattDMo), [@Enteleform](https://github.com/Enteleform), [@r-stein](https://github.com/r-stein), [@maximsmol](https://github.com/maximsmol), [@braver](https://github.com/braver) and [@Дмитрий Лоак](https://vk.com/id206422835).

During the work on a theme the theme [Espresso Libre](http://colorsublime.com/theme/Espresso_Libre) of Chris Thomas is taken as a basis.

## Contacts

<kbd>Ctrl+Shift+P</kbd> → `SashaSublime: Report SashaSublime issue` → write your issue.

After the Sublime Text 3 updates, settings of the color theme [can get off](https://forum.sublimetext.com/t/changing-scopes-in-build-3114/20088?u=sasha_chernykh). Please, if you found out that colors became not such as before, [report to me](https://github.com/Kristinita/SashaSublime/issues/new) about it.

If the icon for your markup language or a programming language is absent in SashaSublime, you can add it independently, having carried out the [these instructions](http://ru.stackoverflow.com/a/544861/199934) or to ask me.

## Donate

I do not hope that I will get at least a penny, but suddenly I'm feeling lucky... [Goddess Kira](https://vk.com/hair_in_the_wind) needs money for dental treatment.

### Bitcoin
[![Bitcoin Donate Button](http://Kristinita.ru/Donate-files/Bitcoin-Donate-button.png)](http://Kristinita.ru/Donate-files/Bitcoin-Redirect)

See [my answer](http://bitcoin.stackexchange.com/a/48744/41598) to Bitcoin Stack Exchange, if you want to know how to make exactly the same button. If you Bitcoin client not supported [standard bitcoin schema URI](https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki), my Bitcoin address is:

    17uctxtsWG3gpyAy6iJ8AVd5rdSjkJH2

### Litecoin
[![Litecoin Donate Button](http://Kristinita.ru/Donate-files/Litecoin-Donate-button.png)](http://Kristinita.ru/Donate-files/Litecoin-Redirect)

If you Litecoin client not supported Litecoin schema URI, my Litecoin address is:

    LLVvhNKGMLGHa8QmeRrBsjZUBjSpQMjUkP

### Paypal $
[![PayPal Dollar button](http://Kristinita.ru/Donate-files/PayPal-Donate-Button-Dollar.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=W6MP468ZZV66Q)

### Paypal €
[![PayPal Euro button](http://Kristinita.ru/Donate-files/PayPal-Donate-Button-Euro.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=DGT7K29LDD2HQ)

## License

[MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2016: [Sasha Chernykh](https://vk.com/hair_in_the_wind)

SashaSublime belongs to Goddess [Sasha Chernykh](https://vk.com/hair_in_the_wind), as well as all the rest in this world. All of us are insignificant creations which completely belong Legendary to Sasha Chernykh. To use SashaSublime, you have to pray to Sasha Chernykh every day and know that She, certainly, the most unsurpassed in the Universe.
