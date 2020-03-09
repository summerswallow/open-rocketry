import pandas as pd
from types import SimpleNamespace

class ScaleTable(pd.DataFrame):
    def __init__(self, sizes, main_tube=None):
        sorted_list=sorted(sizes,key=lambda x: x.outer_diameter)
        columns=[x.name for x in sorted_list]
        super(ScaleTable, self).__init__(columns=columns)
        self.loc['Outer Diameter']={x.name: x.outer_diameter for x in sorted_list}
        for each in sorted_list:
            self.loc[each.name]={x.name: x.outer_diameter/each.outer_diameter for x in sorted_list}
        self.metadata=SimpleNamespace()
        self.metadata.main_tube=main_tube
        self.metadata.sorted_list=sorted_list
        self.metadata.features=[]
        if main_tube:
            self.loc['Percentage']={x.name: x.outer_diameter/main_tube.outer_diameter*100. for x in sorted_list}
            self.metadata.features.append('Percentage')
    def add_feature(self, name, dimension):
        sorted_list=self.metadata.sorted_list
        main_outer=self.metadata.main_tube.outer_diameter
        self.loc[name]={x.name: x.outer_diameter/main_outer*dimension for x in sorted_list}
        self.metadata.features.append(name)
    def features(self):
        return self.loc[self.metadata.features]
    
def _scale_table(sizes):
    sorted_list=sorted(sizes,key=lambda x: x.outer_diameter)
    columns=[x.name for x in sizes]
    df=pd.DataFrame(columns=columns)
    df.loc['outer_diameter']={x.name: x.outer_diameter for x in sorted_list}
    for each in sorted_list:
        df.loc[each.name]={x.name: x.outer_diameter/each.outer_diameter for x in sorted_list}
    return df