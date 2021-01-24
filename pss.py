# PSS Python Style Sheet

# Creates css file for only one id or class or tag
class PSS():
    def __init__(self, id, **propvals):
        css = id + " {\n"

        for prop in propvals:
            css += "\t{} : {};\n".format(prop.replace('_', '-'), propvals[prop])

        css += "}"

        self.css = css

    def __str__(self) -> str:
        return self.css

    def preview(self):
        print(self.css)
        return self.css

    def save(self, filename):
        with open(filename, 'w') as file:
                file.write(self.css)

# bundles multiple css files into one
def pss_bundler(*vars, filename):  
    css = ""  
    for v in vars:
        css += str(v)

    with open(filename, 'w') as file:
        file.write(css)


