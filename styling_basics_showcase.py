
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
import ofjustpy as oj
from py_tailwind_utils import *

def on_example_selected(dbref, msg, to_ms):
        print("button clicked")
        pass
    
sideMenu = SimpleSideMenu("Styling basics", twsty_tags=[*gradient(blue/"200/90",
                                                                  yellow/"200/90",
                                                                  pink/"200/90",
                                                                  green/"200/90",
                                                                  indigo/"200/90",
                                                                  purple/"200/90",
                                                                  direction='tr')]
                          )
sideMenu.add_flat_item("A", "A", value="a",
                       on_click = on_example_selected
                       )



comp_display_box = oj.PD.Div(twsty_tags=[H/screen, W/full, bg/pink/2])

        
endpoint = oj.create_endpoint("styling_basics_using_tailwind",
                     
         childs = [oj.HCCMutable.StackH(childs = [sideMenu,
                                          oj.HCCMutable.Container(childs=[comp_display_box
                                                                          ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                                )
                   ],
                              title="Styling basics using tailwind"
                              )

oj.add_jproute("/styling_basics_showcase", endpoint)

