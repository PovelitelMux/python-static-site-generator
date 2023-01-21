from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
        # The rglob() method is used to recursively iterate through all the files and directories in the source directory.
        # The for loop iterates through each path returned by rglob(), checks if the current path is a directory using the is_dir() method, and if it is a directory it calls the create_dir(path) method to create the directory in the destination.
