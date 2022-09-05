from flask import Blueprint, render_template
from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.palettes import Category10
import pandas as pd
import datetime as dt
import numpy as np
import itertools


BLUEPRINT_NAME = "dashboard"


bp = Blueprint(BLUEPRINT_NAME, __name__, url_prefix=f"/{BLUEPRINT_NAME}")


def make_dataframe():
    times = pd.date_range("2022-01-01", "2022-01-31", freq="1H")
    categories = ["el", "varme", "vand"]
    values = np.random.uniform(0, 100, size=(len(times), len(categories)))
    df = pd.DataFrame(data=values, index=times, columns=categories)
    df.index.name = "tidspunkt"
    df.columns.name = "kategori"
    df = df.stack()
    df = df.reset_index()
    df = df.rename(columns={0: "værdi"})
    return df


def plot_stacked_bar(df, x_col, y_col, category_col):
    df = df.set_index([category_col, x_col])
    df = df.unstack(level=category_col)
    df = df[y_col]
    df = df.reset_index()
    data = dict()
    for col in df.columns:
        data[col] = df[col]
    if pd.api.types.is_datetime64_any_dtype(df[x_col]):
        x_axis_type = "datetime"
    else:
        x_axis_type = None
    p = figure(x_range=data[x_col], height=250, title=y_col,
            toolbar_location=None, tools="hover", tooltips=f"$name @{x_col}: @$name")
    p.vbar_stack(df.columns.to_list(), x=x_col, width=0.9, source=data, color=Category10[10][:len(df.columns)],
                legend_label=df.columns.to_list(), x_axis_type=x_axis_type)
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    html = file_html(p, CDN, "my plot")
    return html


@bp.route("/")
def main():
    df = make_dataframe()
    html = plot_stacked_bar(df, x_col="tidspunkt", y_col="værdi", category_col="kategori")
    return render_template("dashboard.jinja", graph=html)
