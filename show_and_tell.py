import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx

import poster_perfect_sty

with oj.TwStyCtx(poster_perfect_sty):
    
    with writer_ctx:
        with Container():
            with TitledPara(heading_text = "Georage Castanza: The marine biologist", #h5 element controls 
                            fix_sty_section_nesting=True,
                            twsty_tags = []) as titled_para:

                with Prose(text="Your article content goes here. Use this space to showcase your text content, images, and any other media you want to include. So I started to walk into the water. I won't lie to you boys, I was terrified. But I pressed on, and as I made my way past the breakers a strange calm came over me. I don't know if it was divine intervention or the kinship of all living things but I tell you Jerry at that moment, I was a marine biologist.") as prose_box:
                    pass
            



        
tlc = oj.PD.Container(childs = [titled_para],
                      twsty_tags=[mr/x/auto, cc/boxtopo.bd, cc/bd/4, cc/bd/rose/4,
                                  ]
                      )


app = oj.load_app()                 
endpoint = oj.create_endpoint(key="Pretty Tailwind things",
                         childs = [tlc
                                   ],
                              title = "Pretty Tailwind things",
                              twsty_tags=[bg/gray/1]

                              )
oj.add_jproute("/", endpoint)
