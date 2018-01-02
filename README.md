# Gutenberg-Paralax

Gutenberg-Paralax is a basic theme for [Gutenberg](https://getgutenberg.io) based on [materializecss](https://materializecss.com).

It's design goals are:

* have a landing page,
* have a setup for articles and posts, 
* have it working out of the box, with menu's

## Contents

- [Installation](#installation)
- [Options](#options)
  - [Options - general ](#options-general)
    - [Logo](#logo)
    - [Links](#links)
    - [Color scheme](#color-scheme)
    - [Footer](#footer)
      - [Bio](#bio)
      - [References](#references)
      - [Contact](#contact)
    - [Social](#social)
  - [Options - index page ](#options-index-page)
    - [Images](#images)
    - [Features](#features)
- [License](license)
- [Credits](#credits)
- [Todo](#todo)

## Installation

First, download this theme to your `themes` directory:

```bash
$ cd themes
$ git clone https://github.com/verpeteren/gutenberg-paralax.git
```
and then enable it in your `config.toml`:

```toml
theme = "paralax"
```

Second: check your version:

```bash
gutenberg --version
```

If you are using an pre 0.2.2-next version of gutenberg you might need use the following hack to avoid issue  [Keats/tera#235](https://github.com/Keats/tera/issues/235)

```bash
cp themes/paralax/templates/macro.html templates/macro.html
echo "" > themes/paralax/templates/macro.html
```

Third, set up the options that you want to use in your  `config.toml`. The available options are all present in `themes/paralax/theme.toml' and these are documented in  [Options - general ](#options-general) and [Options - index page ](#options-index-page)

```bash
vi config.toml themes/paralax/theme.toml
```

Forth: finetune your templates by copy any of the `themes/paralax/templates/` into your `templates` folder.
```bash
cp themes/paralax/templates/macros.html templates/macros.html
vi templates/macros.html
```


Fifth, Write some content: gutenberg has a lot of [clever options](https://www.getgutenberg.io/documentation/content/page/). The following files give you a head start with some tags, categories and [linked pages](#links)

````bash
#!/bin/bash

mkdir -p content/pages

cat << EOF > content/pages/projects.md
+++
title = "Projects"
path = "/projects"
date = "2018-01-02"
tags=["article"]
category="documentation"
draft = false
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft.

<p>direct html is possible<p>
EOF

mkdir -p content/blog
cat << EOF > content/blog/_index.md
+++
# section front-matter: see https://www.getgutenberg.io/documentation/content/section/
sort_by = "date"
redirect_to = "/"
+++
EOF

cat << EOF > content/blog/hello-gutenberg.md
+++
# page front matter: see https://www.getgutenberg.io/documentation/content/page/
title = "Hello, Gutenberg!"
date = "2018-01-02"
tags = ["gutenberg"]
category = "documentation"
draft = false

[extra]
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft.

If you enabled [syntax highlighting]()https://www.getgutenberg.io/documentation/getting-started/configuration/#syntax-highlighting, the following should work:

\`\`\`php
$cool_stuff = file_get_contents("http://nidium.com");
\`\`\`

EOF

mkdir -p content/blog/another-post
cat << EOF > content/blog/another-post/index.md
+++
title = "Aonther post"
date = "2018-01-02"
tags = ["gutenberg"]
category = "documentation"
aliases = ["/other-ffing-post"]
draft = false

[extra]
github = "https://github.com/verpeteren/gutenberg-paralax"
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft..
Due to [Asset colocaton](https://www.getgutenberg.io/documentation/content/overview/#assets-colocation), you can save your files in this subdirectory, right next to the \`index.md\`. E.G.
\`content/blog/another-post/[missing_file.png](missing_file.png)\`.
EOF

wget -q -O content/blog/another-post/missing_file.png http://placehold.it/30x130.png

````

Sixth, Start the development server

```bash
gutenberg serve
```


## Options 

### Options - General


#### Logo

Set the `logo` to be used in the navbar and the side bar.
Probably obvious, but transparent logo's work best.

```toml
[extra.paralax]
logo = "http://placehold.it/300x300"
```

#### Links

Set list of `links` to be used in the navbar and the side bar.
Please note, that `tags` and `categories` will be added when these are activated in the site's `config.toml`.


```toml
[extra.paralax]
links = [
    {url = "/", name = "Home"},
    {url = "/blog", name = "Blog"},
]
```

#### Color scheme

It is possible to tweak the some colors. It is not ideal, but it works.

```toml
[extra.paralax.colorscheme]
font = {one = "teal", two="brown", three = "white"}
```

#### Footer

There are 3 blocks in the footer: 

```toml
[extra.paralax.footer]
```

##### Bio

Just a `title` and a `description`.

```toml
[extra.paralax.footer.bio]
title = "Company Bio"
description = "Bla bla bla bla bla. Rubarb Rubarb, Rubarb. Yada yada yada. Bla!"
```

##### References

Just a `title` and a list of `links`.

```toml
[extra.paralax.footer.references]
title = "References"
list = [
    {url = "http://example.com", name="example 1"},
    {url = "http://example.com", name="example 2"},
]
```

##### Contact

Just a `title` and a list of `links`.

```toml
[extra.paralax.footer.contact]
title = "Contact"
list = [
    {url = "mailto://me@example.com", name="mail"},
    {url = "tel://003123456789", name="phone"}
]
```

### Social

The `side bar` can hold a lot of social icons. Some highlights:

* The activation of google analitics has never been easier.
* The most annoying one is the skype icon.
* The most interesting one is `disqus` entry. This is also active on the `content pages`.

```toml
[extra.paralax.social]
ga = "UA-12345678-9"
discuss = "verpeteren"

facebook = "verpeteren"
livejournal = "verpeteren"
twitter = "verpeteren"
reddit = "u/verpeteren"
googleplus = "123456789012345678901"

hackernews = "verpeteren"
slashdot = "verpeteren"
myspace = "verpeteren"
tumblr = "verpeteren"
medium = "verpeteren"

skype = "verpeteren"
slack = "verpeteren"
whatsapp = "0031623456789"
viber = "verpeteren/%2B/en"
wikipedia = "verpeteren"

pinterest = "verpeteren"
pinboard = "verpeteren"
dribble = "verpeteren"
flickr = "16832534@N03"
instagram = "verpeteren"

songkick = "1234567-ver-peteren"
bandcamp = "verpeteren"
soundcloud = "verpeteren"
lastfm = "Ver-Peteren"

github = "verpeteren"
gitlab = "verpeteren"
bitbucket = "verpeteren"
stackoverflow = "1234567/verpeteren"

deviantart = "verpeteren"
shadertoy = "verpeteren"

youtube = "DJtJKMICpb9B1qf7qjEOA"
periscope = "1gqxvYRvnBgJB"
vimeo = "verpeteren"

email = "peter.reijnders@verpeteren.nl"
linkedin = "peter-reijnders-83634149"
xing = "peter_reijnders123"
meetup = "A-Meetup-Group"
justgiving = "verpeteren"

```

### Options - index page

The paralax template makes it easy to create a nice landing page by ust configuring some sections in the configuration file: `text`, `images`, and `features`,

```toml
[extra.paralax.index]
text = "Lorem ipsum dolor sit amet, .."
```

The paralax is based around 3 `images` that give a nice effect during scrolling. 
The sections in the config are labeled `one`, `two` and `three`.
Every image needs to have  `file`/`alt` combination. The files need to be 1440 px wide.
It is optional to set `title`, `subtitle` and a `call to action`. It probably needs some fiddling with the text length and the colors.

#### Images

```toml
[extra.paralax.index.images]

[extra.paralax.index.images.one]
file = "background1.jpg"
alt = "Design thingking by Patrick Perkins"
title = "gutenberg paralax template"
subtitle = "Modern opionated responsive front-end framework Material Design static templates"
cta = { url = "/blog", name = "get started" }
```

#### Features

There are 3 colums with each a [`icon`](http://materializecss.com/icons.html), `title` and a block of `text`.
The coluns in the config are labeled `one`, `two` and `three`.

```toml
[extra.paralax.index.features]

[extra.paralax.index.features.one]
icon = "flash_on"
title ="Reason one"
text = "Bla Bla Bla. Bla, ... "
```

### License

MIT

### Credits

Yes, I cheated and took a lot of ideas from [seventeencups]( https://github.com/17cupsofcoffee/seventeencups.net).

## Todo

This is far from complete:

- [X] add a readme file
- [X] add the license file 
- [X] get a basic working index page
- [ ] get a basic working post/blog page
- [ ] get basic working tag page
- [ ] get basic working categories page
- [ ] make layout of the index page pretty
- [ ] clean up unused css stuff
- [ ] do-da-scss-thing 
- [X] drop/rename `font` in the colorscheme
- [ ] use better names instead of one, two, three in the colorscheme.
- [ ] check manifest.json, sitemap.xml, robots.txt
