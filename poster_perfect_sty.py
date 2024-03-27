from py_tailwind_utils import *

h1 = []

h2 = []  # "prose", "prose-2xl"

h3 = []  # "prose", "prose-2xl"

h4 = []  # "prose", "prose-2xl"

h5 = [fz.lg,  fw.medium, mr / sl / 2, fc/gray/4]  # "prose", "prose-2xl"

h6 = []  # "prose", "prose-2xl"

para = []

ul = []
ol = []
img = []
li = []
button = []

title_text = []
subtitle_text = []

heading_box = [db.f, jc.around]
heading_text = []
subheading_box = [db.f, jc.around]
subheading_text = []

subsubheading_text = []

spacing = []
centering_div = [db.f, jc.center]
span = []

form = []
theme = []
P = []
A = []

stackv = [db.f, flx.col]
stackh = [db.f]
stackw = [db.f, flx.wrap, jc.center]
stackd = [db.f]
_ = dbr = Dict()
_.banner = []
_.result = [hidden / ""]

border_style = []

icon_button = []

theme = []

heading = heading_box
heading2 = subheading_box
heading_span = heading_text
heading2_span = subheading_text

prose = [mr/st/4, indent/4, lh.loose, ls.wide, fz.lg, ff.mono, fw.medium, ta.justify, fc/gray/800]

divbutton = []

expansion_item = []

inputJbutton = []
select = []
selectwbanner = []

infocard = []

barpanel = []

slider = [H / 6, db.f, ai.center]
circle = [W / 6, H / 6, bdr.full, *hover(noop / bds.double, noop / bd)]

expansion_item = []

textarea = []

textinput = [db.f, jc.center]
input = []

cell = []

left_cell = [*cell, ta.end, W / "5/12"]
right_cell = [*cell, ta.start, W / "5/12"]
eq_cell = [*cell, ta.center, op.c]

option = []
label = [db.f, jc.center]

wp = []

nav = [top / 0]
footer = []
div = []

hr = []


def stackG(num_cols, num_rows):
    return [db.g, G / cols / f"{num_cols}", G / rows / f"{num_rows}", gf.row]


def get_color_tag(colorname):
    return globals()[colorname]


def build_classes(*args):
    return tstr(*args)


td = []
tr = []

tbl = [fz.sm, tbl.auto, W / full, overflow.auto, overflowx.auto]

expansion_container = [fz.lg]

togglebtn = []

checkbox = []


def halign(align="center"):
    """
    align the contents : options are start, end, center, between, evenly, around
    """
    return [db.f, getattr(jc, align)]


def valign(align="center"):
    """
    align the contents : options are start, end, center, between, evenly, around
    """
    return [db.f, getattr(ai, align)]


def align(halign="center", valign="center"):
    """
    vertical and horizonal align
    """
    return [db.f, getattr(ai, valign), getattr(jc, halign)]


container = [container, mr/x/auto]

default_border = [bd / 2, bdr.lg]
dockbar = [*stackh, jc.center, W / full, H / 16]
undock_button = []
code = []
pre = []
collapsible = []
chartjs = []
dt = []
dd = []
dl = []
header = []
p = []
section = []
aside = []
main = []

fieldset = []
legend = []
optgroup = []
datalist = []

details = []
summary = []
article = []
small  = []
thead = []
th = []
tbody = []
table = []
br = []
time = []

address = []
script = []
blockquote = []
titledPara = [shadow._, shadow/slate/"200/50", pd/3]

sideMenu_btn = [ ]
