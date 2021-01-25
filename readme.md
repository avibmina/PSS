## PSS (Python Style Sheet)

**PSS** is same as css but you can write css in python.

##### See All Examples For Better Understanding

#### NOTE: Try all examples and you will know better

---

Usage:

- clone this repo
- import pss

```python
from pss import PSS
```

- then start styling.

### Examples:

##### Example 1: Basics Of Usage

```python
from pss import PSS
# use '_' instead of '-' like in background_color
h1 = PSS("h1", color="white", background_color="purple")
h1.preview() # Outputs the css code
# OR
print(h1) # Outputs the css code
```

##### Outputs

```css
h1 {
  color: white;
  background-color: purple;
}
```

---

##### Example 2: using css class selector and saving it

```python
from pss import PSS

# Here we used css class selector
container = PSS(".container", color="white", background_color="black")
container.save('style.css') # creates a .css file with the name passed in.

print(container) # as usual prints the css code
```

###### _creates style.css file with below code_

```css
.container {
  color: white;
  background-color: black;
}
```

---

##### Example 3: using with css id selector and saving

```python
from pss import PSS

# Here we used css id selector
div = PSS("#main",
color="white",
background_color="blue",
padding="10px",
border="solid 7px black"
)
div.save('main.css') # creates a .css file with the name passed in.
```

###### _creates main.css file with below code_

```css
#main {
  color: white;
  background-color: blue;
  padding: 10px;
  border: solid 7px black;
}
```

---

But There's a problem. using .save() creates a .css file and writes only one element you styled.
for example: if you see in example 2, it creates file with the one you styled only. we cannot style another one and save those two styled tags or class or id in one css file.

YEAH.. its hard to understand... once againg saying, try it yourself, you will understand it better.

---

##### Example 4: combining and saving all styled elements into one css file

```python
from pss import PSS, pss_bundler

h1 = PSS("h1", color="white", background_color="purple")

container = PSS(".container", color="white", background_color="black")

div = PSS("#main",
color="white",
background_color="blue",
padding="10px",
border="solid 7px black"
)

# Saving These 3 Styled Elements Into One CSS File
# using pss_bundler()
# pss_bundler() takes all styled elements, then combines and saves them in 1 file
# dont forget to pass in the filename
pss_bundler(h1, container, div, filename="bundle.css")
```

code in the generated bundle.css file

```css
h1 {
  color: white;
  background-color: purple;
}

.container {
  color: white;
  background-color: black;
}

#main {
  color: white;
  background-color: blue;
  padding: 10px;
  border: solid 7px black;
}
```

---

##### alternatively below code generates the same result as above css code

```python
from pss import PSS, pss_bundler

# Pass in the file name
# dont forget comma after every styling
pss_bundler(
    PSS("h1", color="white", background_color="purple"), # comma here

    PSS(".container",
        color="white",
        background_color="black"
    ),  # comma here

    PSS("#main",
        color="white",
        background_color="blue",
        padding="10px",
        border="solid 7px black"
    ), filename="bundle.css")
```

##### Example 5: using function pss()

```python
from pss import PSS, pss

# return css code instead of saving like function pss_bundle
# take only styled elements and no file name needed
css = pss(
    PSS("h1", color="white", background_color="purple"),

    PSS(".container",
        color="white",
        background_color="black"
    ),

    PSS("#main",
        color="white",
        background_color="blue",
        padding="10px",
        border="solid 7px black"
    ))

print(css) # prints out css code
```
### Have A Nice Day
### Thanks :)
