import pywal
import click
import pathlib
from urllib import request
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def download_logo(url, build_dir):
    filename = build_dir / f"logo.{url.split('.')[-1]}"
    request.urlretrieve(url, filename=filename)
    return filename


def plot_color(ax, colors):
    text_args = {
        "fontsize": 12,
        "verticalalignment": "center",
        # "horizontalalignment": "center",
        # "rotation": "vertical",
    }

    rec_args = {"width": 1, "height": 1}

    for i, ith_color in enumerate(colors["colors"].values()):
        rec = Rectangle(xy=(0, i), facecolor=ith_color, **rec_args)
        ax.add_patch(rec)
        ax.text(1.1, i + 0.5, f"{i} / {ith_color}", **text_args)

    ax.set_axis_off()
    ax.set_ylim(0, 16)
    ax.set_xlim(0, 2)


def plot_logo(ax, filename):
    img = Image.open(filename)
    ax.imshow(img)
    ax.set_axis_off()


@click.command()
@click.option("--url", help="logo url")
@click.option("--color_name", help="logo url", default=None)
def main(url, color_name):

    build_dir = pathlib.Path("build")

    if not build_dir.exists():
        build_dir.mkdir()

    filename = download_logo(url, build_dir)
    colors = pywal.colors.get(str(filename.resolve()))

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    plot_color(ax, colors)
    plot_logo(ax2, filename)
    plt.show()

    color_i = input("Choose awesome color [0-15]:")
    color = colors["colors"][f"color{color_i}"][1:]

    lines = [
        f"\definecolor{{awesome}}{{HTML}}{{{color}}}\n"
        "\n"
        "% Colors for text\n"
        "\definecolor{darktext}{HTML}{414141}\n"
        "\definecolor{text}{HTML}{333333}\n"
        "\definecolor{graytext}{HTML}{5D5D5D}\n"
        "\definecolor{lighttext}{HTML}{999999}\n"
    ]

    with open(build_dir / "colors.tex", "w") as f:
        for l in lines:
            f.write(l)


if __name__ == "__main__":
    main()
