# PSS Python Style Sheet

# Creates css file for only one id or class or tag
class PSS():
    def __init__(self, id, **propvals):
        css = id + " {\n"

        for prop in propvals:
            css += "\t{} : {};\n".format(prop.replace('_',
                                                      '-'), propvals[prop])

        css += "}\n"

        self.css = css

    def __str__(self) -> str:
        return self.css

    # prints out the css code
    def preview(self):
        print(self.css)

    # creates .css file for only one selected id or class or html tag
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(self.css)


# Only returns css code, same as pss_bundler but returns the code instead of creating .css file
def pss(*vars):
    css = ""
    for v in vars:
        css += str(v)

    return css


# bundles multiple css files into one
def pss_bundler(*vars, filename="style.css"):
    css = ""
    for v in vars:
        css += str(v)

    with open(filename, 'w') as file:
        file.write(css)
