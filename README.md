# Gutenberg-Materialize

Gutenberg-Materialize is a basic theme for [Gutenberg](https://getgutenberg.io) based on [materializecss](http://materializecss.com).

It's design goals are:

* have a `paralax` landing page,
* have a setup for articles and posts,
* have it working out of the box, with menu's

## Contents

- [Installation](#installation)
- [Options](#options)
  - [Options - general ](#options-general)
    - [Logo](#logo)
    - [Landing page](#landing-page)
    - [Sidebar](#sidebar)
    - [Copyright](#copyright)
    - [Links](#links)
    - [Color scheme](#color-scheme)
    - [Footer](#footer)
      - [Bio](#bio)
      - [References](#references)
      - [Contact](#contact)
    - [Social](#social)
  - [Options - index - page ](#options-index-page)
    - [Images](#images)
    - [Features](#features)
  - [Options - page ](#options-page)
    - [Discus](#discus)
    - [Github](#github)
- [What is 'rmd.py'](rmd.py)
- [License](license)
- [Credits](#credits)
- [Contributing](#contributing)
- [Todo](#todo)

## Installation

### First, download this theme to your `themes` directory:

```bash
$ git submodule add https://github.com/verpeteren/gutenberg-materialize.git themes/materialize
```

### Second, enable it in your `config.toml`:

Just the `theme` is needed, but this theme is preparde to handle `tag` and `category` pages.

```toml
theme = "materialize"
generate_categories_pages = true
generate_tags_pages = true
```

### Third, check your version:

```bash
gutenberg --version
```

If you are using an pre 0.2.2-next version of gutenberg you might need use the following hack to avoid issue  [Keats/tera#235](https://github.com/Keats/tera/issues/235)

```bash
cp themes/materialize/templates/macro.html templates/macro.html
echo "" > themes/materialize/templates/macro.html
```

### Fourth, set up the options that you want to use in your  `config.toml`.

The available options are all present in `themes/materialize/theme.toml' and these are documented in  [Options - general ](#options-general) and [Options - index page ](#options-index-page)

```bash
vi config.toml themes/materialize/theme.toml
```

or if you are brave:

```
tail -n +`grep -n '\[extra\.materialize\]' themes/materialize/theme.toml |cut -d':' -f1` themes/materialize/theme.toml >> config.toml
vi config.toml
```

### Fifth (optional): finetune your templates by copy any of the `themes/materialize/templates/` into your `templates` folder.

```bash
cp themes/materialize/templates/macros.html templates/macros.html
vi templates/macros.html
```

### Sixth, write some content

Gutenberg has a lot of [clever options](https://www.getgutenberg.io/documentation/content/page/). The following files give you a head start with some tags, categories and [linked pages](#links)

The file `generate_some_dummy_content.sh` can help the brave people that want to touch the ground running.

```bash
./themes/materialize/generate_some_dummy_content.sh

```

### Seventh, start the development server

```bash
gutenberg serve
```

## Options

### Options - General

#### Logo

Set the `logo` to be used in the navbar (small, about 32 px) and in the side bar (big, about 256 px).
Probably obvious, but transparent logo's work best.

```toml
[extra.materialize]
logo = {small = "http://placehold.it/32x32", big = "http://placehold.it/256x256"}
```

#### Sidebar

Activate the sidebar (left side) on a normal page.
Values can be "off", "left"

> Please note: The [paralax index page](#options-index-page) template has a empty sidebar section. that is the reason why paralax has no sidebar.

```toml
[extra.materialize]
sidebar = "off"
```

#### Landing page

Set the links to the `home` page. This works very well with the [paralax index page](#options-index-page)

```toml
[extra.materialize]
home = {url = "/paralax/", name = "Home"}
```

#### Copyright

Sets the link in the footer

```
copyright = {url = "/#", name ="© 2018"}
```

#### Links

Set list of `links` to be used in the navbar and the side bar.
Please note, that `tags` and `categories` will be added when these are activated in the site's `config.toml`.
Also the `home` will be [actived](#Landing-page)

```toml
[extra.materialize]
links = [
    {url = "/projects", name = "Projects"},
    {url = "/blog", name = "Blog"},
]
```

#### Color scheme

It is possible to tweak the some colors. It is not ideal, but it works. 

You can use the [standard color names of materialize](http://materializecss.com/color.html).

```toml
[extra.materialize.colorscheme]
font = {one = "teal", two="brown", three = "white"}
background = {one = "teal", two="brown", three = "white"}
```

#### Footer

There are 3 blocks in the footer:

```toml
[extra.materialize.footer]
```

##### Bio

Just a `title` and a `description`.

```toml
[extra.materialize.footer.bio]
title = "Company Bio"
description = "Bla bla bla bla bla. Rubarb Rubarb, Rubarb. Yada yada yada. Bla!"
```

##### References

Just a `title` and a list of `links`.

```toml
[extra.materialize.footer.references]
title = "References"
list = [
    {url = "http://example.com", name="example 1"},
    {url = "http://example.com", name="example 2"},
]
```

##### Contact

Just a `title` and a list of `links`.

```toml
[extra.materialize.footer.contact]
title = "Contact"
list = [
    {url = "mailto://me@example.com", name="mail"},
    {url = "tel://003123456789", name="phone"}
]
```

### Social

The `side bar` can hold a lot of social icons. Some highlights:

* The activation of google analytics (`ga`) has never been easier.
* The most annoying one is the skype icon.
* The most interesting one is `disqus` entry. This is also active on the `content pages`.

```toml
[extra.materialize.social]
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

The materialize template makes it easy to create a nice landing page by ust configuring some sections in the configuration file: `text`, `images`, and `features`,

```toml
[extra.paralax]
```

The materialize is based around 3 `images` that give a nice effect during scrolling.
The sections in the config are labeled `one`, `two` and `three`.
Every image needs to have  `file`/`alt` combination. The files need to be 1440 px wide.
It is optional to set `title`, `subtitle` and a `call to action`. It probably needs some fiddling with the text length and the colors.

#### Images

```toml
[extra.paralax.images]

[extra.paralax.images.one]
file = "background1.jpg"
alt = "Design thingking by Patrick Perkins"
title = "gutenberg materialize template"
subtitle = "Modern opionated responsive front-end framework Material Design static templates"
cta = { url = "/blog", name = "get started", pulse = "pulse" }
```

I happen to like the photos and the licensing terms at [unsplash.com](http://unsplash.com). To ease the download, resizing and renaming the following oneliner gets you started.

```bash
wget -q -O - https://unsplash.com/photos/45FJgZMXCK8/download?force=true | convert -resize 1440 - static/img//background1.jpg
```

#### Features

There are 3 colums with each a [`icon`](http://materializecss.com/icons.html), `title` and a block of `text`.
The coluns in the config are labeled `one`, `two` and `three`.

```toml
[extra.paralax.features]

[extra.paralax.features.one]
icon = "flash_on"
title ="Reason one"
text = "Bla Bla Bla. Bla, ... "
```

### Options - page

#### Discuss

It is easy to inject `discuss thread` the bottom of your pages. The discuss thread will be picked up by the permalink, slug, and the following 2 configurations:

1. Assert that [`extra.materialize.social.discuss`](#social) is enabled inside your config.toml
2. Set a `date` inside the frontmatter of your content page.

```
+++
#...
date = "2018-01-20"
+++
```

#### Github

It is easy to add a github-icon and a link to a github repository to the bottom of your pages.
This is done by adding a `extra.github` entry inside the frontmatter of your content page.

```
+++
#...

[extra]
github = "https://github.com/verpeteren/SqlDetective"
+++
```

## What is 'rmd.py'?

I do not want to spend too much time on a technical blog.
That means that I want to write te code files once, so that both the blog and the rest of the tools (ide, compiler, ..) can use it as well.
I searched for a way to seperate the prose from the code, but I did not find any thing practical:
- [tera include](https://tera.netlify.com/docs/templates/#include) does only work on templates
- [gutenberg `gist`](https://www.getgutenberg.io/documentation/content/shortcodes/#gist) shortcode needs to have the files in gist, not locally.
- [ribosome.py](http://sustrik.github.io/ribosome/documentation.html), needs to have a '.' prefix
- [#include](https://gcc.gnu.org/onlinedocs/cpp/) would probably require a Makefile
- [cog](https://nedbatchelder.com/code/cog/) is a bit overkill

So I settled for a simple python3 script that uses a tera comment and expands it.

Basically,`rmd.py` does the following:

* Searches recursively for `.rmd` files in 'raw_folder'.
  Replace/expand the `{#{ code_snippet(..) }#}` shortcodes in every `.rmd` file.
  Write the expanded output to the corresponding `.md` file.

* Delete `content_folder` recursively.
  Copy `raw_folder` into `content_folder` recursively.

Needless to say, this is a dangerous operation.

When gutenberg gets such a shortcode in the future, this can retire and `{#{ code_snippet(..) }#}` can be replaced by `{{ code_snippet(..) }}`.

> Totaly unrelated to this theme, but a nice tool to add to your super powers is this poorman's link checker:

``
wget --spider -r -nd -nv -l 10 -o run.log http://127.0.0.1:1111/&&grep -B1 'broken link' run.log | grep http
```

### Example:

File: `rawcontent/blog/index.rmd`

```markdown
bla
{#{ code_snippet(file_name="main.c", file_type="c") }#}
yada
```

and this file:

File: `rawcontent/blog/main.c`

```c
int main(const int argc, const char ** argv) {
    return 0;
}
```

The following command will delete and copy the `content/blog` directory with the expanded `index.md` file and 'main.c'

```bash
python3 ./themes/materialize rmd.py ./rawcontent/blog ./content/blog
```

File: `./content/blog/index.md`

```markdown
bla

__**file**: [main.c](main.c)__

```c
int main(const int argc, const char ** argv) {
	return 0;
}

```


yada
```

That is really nice becausey you can write, test, use, your code snippets

```bash
mkdir -p tmp&&clang -o ./tmp/main main.c&&./tmp/main
```

## License

MIT

## Credits

Yes, I cheated and took a lot of ideas from [seventeencups]( https://github.com/17cupsofcoffee/seventeencups.net).

## Contributing

If you find something strange with this theme, feel free to improve it.
As my layout skills and CSS are not that good, a lot of things can be improved.

## Todo

This is far from complete:

- [X] add a readme file
- [X] add the license file
- [X] get a basic working index page
- [X] get a basic working post/blog page
- [X] get basic working tag page
- [X] get basic working categories page
- [X] use materialize selections/cards for categories, sections, tags, ...
- [X] make layout of the sidebar pretty
- [ ] sidebar 'right' (off, left)
- [ ] clean up unused css stuff
- [ ] do-da-scss-thing
- [ ] improve responsiveness
- [X] drop/rename `font` in the colorscheme
- [ ] use better names instead of one, two, three in the colorscheme.
- [X] check manifest.json, sitemap.xml, robots.txt
- [X] update documentation (options, bash content script)
- [ ] use get_taxonomy_url for tags and categories
- [ ] investigate why the iteration over subsections in a section template does not have a subsection list
- [ ] improve breadcrumb links
- [X] repair the display of li bullet points (materialize hides them)
- [ ] paralax resize pops up the menu, and it stays there
- [ ] find a way to preselect the tabs on a section based: content first, then pages, then sections
- [ ] better/robuster code_snippet regex for rmd.py

