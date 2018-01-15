#!/bin/bash

mkdir -p content

cat > content/_index.md << EOF
+++
redirect_to = "/paralax/"
+++
EOF

cat > content/paralax.md << EOF
+++
template="paralax.html"
title = "paralax"
path = "/paralax"
date = "2018-01-02"
draft = false

[extra]

[extra.paralax]

[extra.paralax.images]

[extra.paralax.images.one]
file = "background1.jpg"
alt = "Design thingking by Patrick Perkins"
title = "gutenberg materialize template"
subtitle = "Modern opionated responsive front-end framework Material Design static templates"
cta = { url = "http://github.com/verpeteren/gutenberg-materialize", name = "get started", pulse = "pulse" }

[extra.paralax.images.two]
file = "background2.jpg"
alt = "Brainstorming over paper by Helloquence"
title = "materialize"
subtitle = "A modern responsive front-end framework based on Material Design"
cta = { url = "http://materializecss.com", name = "Get Materialize", pulse = "" }

[extra.paralax.images.three]
file = "background3.jpg"
alt = "Shot before the shoot by Nik MacMillan"
title = "gutenberg"
subtitle = "An opinionated static site generator with everything built-in"
cta = { url = "http://getgutenberg.io", name = "Get Gutenberg", pulse = ""}

[extra.paralax.features]
[extra.paralax.features.one]
icon = "flash_on"
title ="Reason one"
text = "Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla Bla. Bla Bla."

[extra.paralax.features.two]
icon = "group"
title = "Reason two"
text = "Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb. Rubarb Rubarb."

[extra.paralax.features.three]
icon =  "settings"
title =  "Reason three"
text = "Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada. Yada Yada Yada."

+++
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam scelerisque id nunc nec volutpat. Etiam pellentesque tristique arcu, non consequat magna fermentum ac. Cras ut ultricies eros.

<!-- more -->
Maecenas eros justo, ullamcorper a sapien id, viverra ultrices eros. Morbi sem neque, posuere et pretium eget, bibendum sollicitudin lacus. Aliquam eleifend sollicitudin diam, eu mattis nisl maximus sed. Nulla imperdiet semper molestie. Morbi massa odio, condimentum sed ipsum ac, gravida ultrices erat. Nullam eget dignissim mauris, non tristique erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;"
EOF

mkdir -p content/pages
cat > content/pages/project.md << EOF
+++
title = "Project page"
description = "Overview of some projects"
path = "/project"
date = "2018-01-02"
tags=["article"]
category="documentation"
draft = false
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft.

<p>direct <b>html</b> is possible<p>
EOF

mkdir -p content/blog
cat > content/blog/_index.md << EOF
+++
# section front-matter: see https://www.getgutenberg.io/documentation/content/section/
sort_by = "date"
#redirect_to = "/"
insert_anchor_links = "right"
title = "blog"
description = "glob('blog')"
slug = "BlogBlogBlog"
path = "/blog"
+++
EOF

cat > content/blog/hello-gutenberg.md << EOF
+++
# page front matter: see https://www.getgutenberg.io/documentation/content/page/
title = "Hello, Gutenberg!"
date = "2018-01-02"
tags = ["gutenberg"]
category = "documentation"
draft = false

[extra]
github = "https://github.com/verpeteren/gutenberg-materialize"
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft.

If you enabled [syntax highlighting](https://www.getgutenberg.io/documentation/getting-started/configuration/#syntax-highlighting), the following should work:

\`\`\`php
$awesome_stuff = file_get_contents("http://nidium.com");
\`\`\`

As you can see, the github link also works by adding this to the \`extra\` settings in this page.
EOF

mkdir -p content/blog/another-post
wget -q -O content/blog/another-post/missing_file.png http://placehold.it/30x130.png
cat > content/blog/another-post/index.md << EOF
+++
title = "Another post"
date = "2018-01-02"
tags = ["gutenberg"]
category = "documentation"
aliases = ["/other-ffing-post"]
draft = false

[extra]
+++

This is the teaser line.

<!-- more -->

This is the rest of the cruft..

Due to [Asset colocation](https://www.getgutenberg.io/documentation/content/overview/#assets-colocation), you can save your files in this subdirectory, right next to the \`index.md\`. E.G.
\`content/blog/another-post/[missing_file.png](missing_file.png)\`.
EOF
