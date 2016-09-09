![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

# SashaSublime

<p align="center">It is devoted to God, the only Creation for the sake of Which it makes sense to live on this planet, the Greatest being of all times and peoples, Queen of the World <a href="https://vk.com/hair_in_the_wind">Sasha Chernykh</a> (Kira Kenyukhova).</p>

<p align="center"><img src="http://i.imgur.com/0TF54SX.jpg" alt=""></p>

##Description
i faced a problem that in already available themes and color schemes many elements of syntaxes have dim, badly distinguishable an eye of color. i tried to use many themes and schemes, but the result in one of them didn't satisfy me. Therefore, i decided to write own theme; its concept: 

1. **all colors of all elements are well visible**,
2. change colors made not for beauty, and for better visibility,
3. proper execution for each syntax,
4. each element of syntax has to have color.

Supported syntaxes: JSON, XML, HTML, CSS, JavaScript, Diff, Regular Expression and Mediawiki NG. The color scheme is incompatible with syntaxes of [CSS3](https://packagecontrol.io/packages/CSS3_Syntax) and [JavaScriptNext - ES6](https://packagecontrol.io/packages/JavaScriptNext%20-%20ES6%20Syntax). Please, use default syntax for JavaScript and CSS for compatibility with SashaSublime. If you want use SashaSublime, but in some syntaxes you want use another color scheme, please, read page 73 «[Sublime Text Power User](https://docs.zoho.com/file/nqgo4e3473558e032489e9dc3bceb3db16723)» book.

## Screenshots

Screenshots are made in the Windows 10 operating system, Sublime Text 3, Build 3114. If i make changes to my color theme and color scheme, i try not to forget to take screenshots of the changes. But Sublime Text and plugins updated, and look at my screenshots may differ from appearance to reality. If you see a discrepancy, please let me know.

### General
![SashaSublime](http://i.imgur.com/ljT5eJp.png)
In a theme/scheme the smallest details are well visible.
![Overall plan details](http://i.imgur.com/DlrJCes.png) 
![Gutter](http://i.imgur.com/VqeuQtH.png) 
![Autocomplete](http://i.imgur.com/3RPAwA7.png) 
![Tabs](http://i.imgur.com/CTOQ9WG.png)
![Side bar](http://i.imgur.com/N8UWi1Q.png) 

### Plugins

[Sublimerge 3](http://www.sublimerge.com/sm3/) + [GitGutter](https://packagecontrol.io/packages/GitGutter)
![Sublimerge](http://i.imgur.com/YnfYXWD.png)  
[HexViewer](https://github.com/facelessuser/HexViewer)  
![Hex Viewer](http://i.imgur.com/c0t0Iqy.png)  
[GitGutter](https://packagecontrol.io/packages/GitGutter) + [SublimeLinter](http://www.sublimelinter.com/en/latest/)   
![GitGutter and SublimeLinter](http://i.imgur.com/24kzw67.png)  
[BracketHighlighter](https://facelessuser.github.io/BracketHighlighter/)     
![BracketHighlighter](http://i.imgur.com/S8SE9nh.png)     
[Emmet](http://emmet.io/)    
![Emmet](http://i.imgur.com/Arhzbgl.png)    


### Selected text
Results with the established [WordHighlight](https://github.com/SublimeText/WordHighlight) plugin.  
![Accentuation](http://i.imgur.com/yJ2EdbD.png) 
_Selected text_
![Accentuation2](http://i.imgur.com/y715wdq.png)
_Selected text when the carriage is not on text field_  
![Find result](http://i.imgur.com/Z3lGryq.png)
_Find (<kbd>Ctrl+F</kbd>) text_
![Find result2](http://i.imgur.com/Tyqv7to.png)
_Find text when the carriage is out of the found text. Сarriage color and this border color set to the same parameter._

### Panels and consoles
![Ctrl+P panel](http://i.imgur.com/2hRinyv.png)
![Find and Replace panel](http://i.imgur.com/VRbjlZz.png)
![Console](http://i.imgur.com/vYkR1MV.png)
![Git output console](http://i.imgur.com/Ifw1A6s.png)
![Build console](http://i.imgur.com/DpltLqa.png)
![ScopeHunter console](http://i.imgur.com/BToxW54.png)

### Comparison of Monokai (default theme) and SashaSublime
SashaSublime has several times more than parameters, than a default theme Monokai.
![Monokai scopes](http://i.imgur.com/YITyD6A.png)
![SashaSublime scopes](http://i.imgur.com/5KE0MKI.png)

### JSON
![JSON1](http://i.imgur.com/N2LvbNZ.png)
![JSON2](http://i.imgur.com/epuwjOb.png)
![JSON3](http://i.imgur.com/6kWo4aW.png)

### XML
![XML](http://i.imgur.com/0s4EFYN.png)

### HTML
![HTML1](http://i.imgur.com/POTMTWq.png)
![HTML2](http://i.imgur.com/LFKMdDX.png)
![HTML3](http://i.imgur.com/AbGgQa9.png)

### CSS
![CSS](http://i.imgur.com/Rr9AmIZ.png)

### JavaScript
It turned out to work not so carefully as i wanted.
![JS1](http://i.imgur.com/dedldIL.png)
![JS2](http://i.imgur.com/2e34vGr.png)

### Diff
![Diff](http://i.imgur.com/AF7BgIU.png)

### Regular Expression
![Regex1](http://i.imgur.com/kzwyA4E.png)
![Regex2](http://i.imgur.com/Fu2Slm6.png)

### Mediawiki NG
![Mediawiki1](http://i.imgur.com/Y2FYuFI.png)
![Mediawiki2](http://i.imgur.com/sSzqfsm.png)

## Installation

### Package Control

i'm wait, when accepting [my request](https://github.com/wbond/package_control_channel/pull/5723)...

### Git




### Manually

Copy files from a repository to the folder `User`: *Preferences* → *Browse Packages* → `User`. 

*Preferences* → *Settings - User* → add in opened file these lines:

	"color_scheme": "Packages/User/SashaSublime.tmTheme",
	"theme": "SashaSublime.sublime-theme",


## Preferences

Also you can make that all your settings were as at me. Copy into your file *Preferences* → *Settings - User* these lines from my file *Preferences* → *Preferences.sublime-settings*:

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
	"show_full_path": true,

Before copying save in a safe place file *Preferences.sublime-settings* from the `User` folder or, what better, use [Local History](https://github.com/vishr/local-history) plugin. If you don't like my preferences, you will be able to return to your preferable settings.


## Setting SashaSublime for some plugins

### BracketHighlighter 

To paint in different colors of a bracket of a plugin of BracketHighlighter, execute the following actions:

+ Install plugin BracketHighlighter via Package Control,
+ `Preferences` → `Package Settings` → `BracketHighlighter` → `Bracket Settings - User` → add in open file tis code and save file:

```
{
	"bracket_styles": {
		// This particular style is used to highlight
		// unmatched bracket pairs. It is a special
		// style.
		"unmatched": {
			"icon": "question",
			"color": "brackethighlighter.unmatched",
			"style": "highlight"
		},
		// User defined region styles
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

*Bonus*: , add in the `Packages` → `GitGutter` `icons` folder from the title page of my repository.

### GitGutter

Probably you are faced with the [same](https://github.com/jisaacks/GitGutter/issues/199#issuecomment-227016698) problem of small icons in GitGutter. In this case in folder, when Sublime Text installed, → `Data` → `Installed Packages` → unpack `GitGutter.sublime-package` any zip archiver (i reccomend [Hao Zip](http://forum.ru-board.com/topic.cgi?forum=5&topic=35814&start=0)) to Data → Packages folder. For example, for me file GitGutter.sublime-package is situated for me in `E:\Sublime Text 3\Data\Installed Packages` path, and I unpacked `.zip` to `E:\Sublime Text 3\Data\Packages` path. 

Now in my `Packages` folder is situated folder `GitGutter`. Delete `GitGutter.sublime-package` file → `GitGutter` → `icons` → replace icons in GitGutter folder to icons on `icons` → `GitGutter` of my repository.

## How to change favicon in Sublime Text 3?

This guide for Windows users, Mac users possible help [this](http://apple.stackexchange.com/questions/153176/changing-sublime-text-3-icon-in-dock-on-yosemite) answer.

Download and open [Resource Hacker](http://rsload.net/soft/editor/9133-resource-hacker.html) or [alternate](http://alternativeto.net/software/resource-hacker/) programs for edit *.exe* files. For example, in Resource Hacker: `File` → `Open` → *sublime_text.exe* → `Icon Group` → right mouse button on *103:3081* → `Replace Icon ...` 

![Resource Hacker](http://i.imgur.com/XcLuNqS.png)

→ select *SashaSublime.ico* in `icons` → `favicon` folder of this repository → `Replace` → `File` → `Save As` → `Yes` → `Save` → restart Windows.

In Sublime Text folder *sublime_text_original.exe* file is created. If you don't like my icons, you can replace *sublime_text_original.exe* → *sublime_text.exe*. Besides, you can always replace your *sublime_text.exe* file on [original version](https://www.sublimetext.com/3) this file.

Examples, when use colors of «S» letter my favicon: 

![SashaSublime.ico](http://i.imgur.com/b2DxblV.png)

+ yellow — for smallest favicons, because is good visible; use in top left angle Sublime Text 3 and in Windows Explorer, 
+ blue — icons in taskbar,
+ violet — icons on desktop,
+ orange — in [Rocket Dock](http://portableapps.com/node/25965) panel and at drag and drop file with icon Sublime Text.

## Notes

The subject is created for personal use if it isn't pleasant to you, simply don't use it. If you don't like any separate colors in my subject, you can change them yourself, see [detailed instructions in Russian](http://ru.stackoverflow.com/a/516668/199934). You can also find a set of other solutions on themes in other my answers on [Stack Overflow in Russian](http://ru.stackoverflow.com/search?q=user:199934%20[sublime-text]%20is:answer) and [Toster](https://toster.ru/user/Kristinita/answers).

To all parameters in the `Default.sublime-theme` file and almost to all parameters in the `Sasha.tmTheme` file comments in Russian are left. You can quickly see which color corresponds to which element. Comments in the `Preferences.sublime-settings` file aren't present because they are [removed](https://forum.sublimetext.com/t/bug-comments-deleted-in-preferences-user/7064/6?u=sasha_chernykh) at change of settings. About all parameters containing in this file it is [possible to read](http://www.sublimetext.ru/documentation/preferences/list) on the Russian site Sublime Text 3.

After the Sublime Text 3 updatings settings of the color theme can get off. Please, if you found out that colors became not such as before, [report to me](https://github.com/Kristinita/SashaSublime/issues/new) about it. Unfortunately, i always used only Windows, and i can't check operability of a subject on other operating systems.

During the work on a theme the theme [Espresso Libre](http://colorsublime.com/theme/Espresso_Libre) of Chris Thomas is taken as a basis.

## Known defects

If you know how to solve these problems, please, [tell me](https://github.com/Kristinita/SashaSublime/issues).

+ [changing color text «Open files and folders» in placeholder](https://forum.sublimetext.com/t/how-to-style-placeholders-text-like-open-files-and-folders-in-the-find-in-files-dialog/21650),
+ [reset Custom Settings icon after updating GitGutter](https://github.com/jisaacks/GitGutter/issues/307).

### SublimeLinter wrote own color scheme file in preferences

If you use [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3), you may not like that Sublime Linter additional sets the color scheme in your user settings. To deactivate the color scheme SublimeLinter, follow these steps:

Install [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) plugin → <kbd>Ctrl+Shift+P</kbd> → PackageResourceViewer: `Open Resource` → `SublimeLinter` → `lint` → `util.py` → in open file to comment out or remove line 215: :crossed_flags:  

	sublime.set_timeout_async(generate_color_scheme_async, 0)

Restart Sublime Text → SublimeLinter should not prescribe in your preferences own color scheme file. Thanks [@r-stein](https://github.com/r-stein) at [solution](https://forum.sublimetext.com/t/sublimelinter-write-own-color-scheme-path-in-the-configuration-file/21842/2?u=sasha_chernykh).

## See also

+ [Kristinita's Search](http://kristinita.ru) — search engine, searching only authoritative sources, materials are written by experts on the subject.
+ [Sasha Black](http://kristinita.ru/Sasha-Black) — mini-service checks the reputation of your site and the availability of the site in the blacklists.

## Thanks

Many thanks to those who answered my questions on themes and color schemes on [Stack Overflow](http://stackoverflow.com/), [English](https://forum.sublimetext.com/) and [Russian](http://forum.sublimetext.ru) Sublime Text forums: [@Keith Hall](https://github.com/keith-hall), [@MattDMo](https://github.com/MattDMo), [@Enteleform](https://github.com/Enteleform), [@r-stein](https://github.com/r-stein), [@maximsmol](https://github.com/maximsmol), [@braver](https://github.com/braver) and [@Дмитрий Лоак](https://vk.com/id206422835).

## License

© 2016 [Sasha Chernykh](https://vk.com/hair_in_the_wind)

This is free software. It is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and it would be great if you distribute your work under this or a similar license, but it's not required.