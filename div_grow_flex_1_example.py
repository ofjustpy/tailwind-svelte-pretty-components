

# TW: expand to cover remaining space
# TIP: Use flx.one


import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import poster_perfect_sty

with oj.TwStyCtx(poster_perfect_sty):
    with writer_ctx:
        with Container(twsty_tags=[H/screen, db.f, flx.col,  boxtopo.bd, bd/3, bd/red/3]) as tlc_box:
            with Div(twsty_tags = [bg/rose/3, W/full, H/32]):
                with Title(title_text="Place header content here", twsty_tags=[]):
                    pass

                pass
            with Div(twsty_tags = [flx.one, W/full, bg/red/2, ai.center]):
                with Span(text="body context -- should fill up the entire remaining height and width",
                          twsty_tags=[ta.center]):
                    pass
                pass
            with Div(twsty_tags = [bg/pink/1, W/full, H/32]):
                with Span(text="Place footer content here", twsty_tags=[ta.center]):
                    pass
                pass

# introduce a side-menu



app = oj.load_app()                 
endpoint = oj.create_endpoint(key="Tailwind styling basics",
                         childs = [tlc_box
                                   ],
                              title = "Pretty Tailwind things",
                              twsty_tags=[bg/gray/1]

                              )
oj.add_jproute("/styling_basics", endpoint)
