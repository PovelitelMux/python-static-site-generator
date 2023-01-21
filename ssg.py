import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    # creating the Site class instance. ** operator unpack the dicktionary
    Site(**config).build()


typer.run(main)
