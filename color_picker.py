import pywal
import click
from urllib import request
import pathlib

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


@click.command()
@click.option("--logo_url", help="logo url")
@click.option("--color_name", help="logo url", default=None)
def main(logo_url, color_name):

    url = pathlib.Path(logo_url)
    logo_filename = pathlib.Path("build/logo").with_suffix(url.suffix)

    request.urlretrieve(logo_url, filename=logo_filename)

    image = pywal.image.get(logo_filename)
    colors = pywal.colors.get(image)

    if not color_name:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        text_args = {
            "fontsize": 14,
            "horizontalalignment": "center",
            "verticalalignment": "bottom",
            "rotation": "vertical",
        }
        rec_args = {"width": 1, "height": 1}
        for i, (name, color) in enumerate(colors["colors"].items()):
            rec = Rectangle(xy=(i, 0), facecolor=color, label=name, **rec_args)
            ax.add_patch(rec)
            ax.text(i + 0.5, 1.1, name, **text_args)
        ax.set_axis_off()
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 2)
        plt.show()

    color = "DC3522"
    if color_name:
        color = colors["colors"][color_name][1:]

    lines = [
        "% Color for highlights\n"
        "% Awesome Colors: awesome-emerald, awesome-skyblue, awesome-red, awesome-pink, awesome-orange\n"
        "%                 awesome-nephritis, awesome-concrete, awesome-darknight\n"
        "% \colorlet{awesome}{awesome-red}\n"
        "% Uncomment if you would like to specify your own color\n"
        f"\definecolor{{awesome}}{{HTML}}{{{color}}}\n"
        "\n"
        "% Colors for text\n"
        "% Uncomment if you would like to specify your own color\n"
        "\definecolor{darktext}{HTML}{414141}\n"
        "\definecolor{text}{HTML}{333333}\n"
        "\definecolor{graytext}{HTML}{5D5D5D}\n"
        "\definecolor{lighttext}{HTML}{999999}\n"
    ]

    with open("colors.tex", "w") as f:
        for l in lines:
            f.write(l)


if __name__ == "__main__":
    main()
