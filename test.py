"""Simple script for wal api."""
import pywal
import click
from urllib import request
import pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


@click.command()
@click.option("--logo_url", help="logo url")
def main(logo_url):

    url = pathlib.Path(logo_url)

    logo_filename = pathlib.Path("build/logo").with_suffix(url.suffix)

    # Set up the image URL
    request.urlretrieve(logo_url, filename=logo_filename)

    """Main function."""
    # Validate image and pick a random image if a
    # directory is given below.
    image = pywal.image.get(logo_filename)

    # Return a dict with the palette.
    # Set quiet to 'True' to disable notifications.
    colors = pywal.colors.get(image)
    print(colors)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for i, (name, color) in enumerate(colors["special"].items()):
        y=1
        ax.add_patch(
            Rectangle(
                xy=(0, i),
                width=1,
                height=1,
                facecolor=color,
                label=name
            )
        )
        ax.text(1+0.1, i + 0.5, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

    for i, (name, color) in enumerate(colors["colors"].items()):
        ax.add_patch(
            Rectangle(
                xy=(3, i),
                width=1,
                height=1,
                facecolor=color,
                label=name
            )
        )
        ax.text(3+1.1, i + 0.5, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

    ax.set_axis_off()
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 16)

    plt.show()


if __name__ == "__main__":
    main()
