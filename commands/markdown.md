

### Inline HTML

The only restricitons are that block-level HTML elements 
- e.g. `<div>, <table>, <pre>, <p> etc.`
- Must be separated from surrounding content by blank lines, and the start and end tags of the block should not be indented with tabs or spaces. Note that Markdown formatting syntax is not processed within block-level HTML tags.

Span-level HTML tags e.g. `<span>, <cite> or <del>` is ok and Markdown syntax is processed within span-level tags.

In HTML, there are two characeters that demand special treatment: < and &. You must escape them as entities, e.g. `&lt; and &amp;`

Inside Markdown code spans and blocks, angle brackets and ampersands are always encoded automatically.

### Block Elements
Markdown translate a paragraph end into a `<br />`
When you do want to insert a `<br />` break tag using Markdown, you end a line with two or more spaces, then type return.

### Headers
### Setext-style headers

```
This is an H1
=============

This is an H2
-------------
```

### Atx-style headers

```
# This is an H1

## This is an H2

###### This is an H6
```

### Blockquotes
Markdown uses email-style > characters for blockquoting
Blockquotes can contain other Markdown elements, including headers, lists, and code blocks.

### Lists
Markdown supports ordered (numbered) and unordered (bulleted) lists
Unordered lists use asterisks, pluses, and hyphens --interchangably -- as list markers:
```
* Red
* Green
* Blue
+ Red
+ Green
+ Blue
- Red
- Green
- Blue
```

Ordered lists use numbers followed by periods:
```
1. Bird
2. McHale
3. Parish
```

a number-period-space sequence at the beginning of a line. To avoid this, you can backslash-escape the period
`1986\. what a great season`

### Horizontal Rules
You can produce a horizontal rule tag `(<hr />)` by placing three or more hyphens, asterisks, or underscores.
```
* * *
***
*****
- - -
----------
```

### Span Elements
#### Links
```
Markdown supports two style of links: inline and reference
the link text is delimited by [square brackets]

This is [an example](http://example.com/ "Title") inline link.
[This link](http://example.net/) has no title attribute.

local resource on the same server [About](/about/).

Reference-style links use a second set of square brackets, inside which you place a label to identify the link:
This is [am example][id] reference-style link.

Then, anywhere in the document, you define your link label like this, on a line by itself:
[id]: http://example.com/ "Optional Title"
You can put the title attribute on the next line

these two links are equivalent
[link text][a]
[link text][A]

The implicit link name shortcut allows you to omit the name of the link.
[Google][]
[Google]: http://google.com/
```

### Emphasis
Text wrapped with one * or _ will be wrapped with an HTML `<em>` tag; double * or _ will be wrapped with an HTML `<strong>` tag
```
*single asterisks*
_single understores_
**double asterisks**
__double underscores__
```

Emphasis can be used in the middle of a word. But if you surround an * or _ with spaces, it'll be treated as a literal asterisk or underscore.

### Code
```
Use the `printf()` function

``There is a literal backtick (`) here.``
```

### Images
```
Inline image syntax looks like this:

![Alt text](/path/to/ima.jpg)
![Alt text](/path/to/img.jpg "Optional title")

Reference-style image syntax:
![Alt text][id]
[id]: url/to/image "Optional title attribute"
```

# Miscellaneous
```
Automatic Links
<http://example.com/>
<address@example.com>

Backslash Escapes
\-*_{}[]()#+-.!
```


