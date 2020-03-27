from misc.utils import render as rd
import viewscad
import os
class Renderer():
    def __init__(self, outdir=None, fn=200):
        self.fn=fn
        self.outdir=outdir
        self.renderer = viewscad.Renderer()
        
    def render(self, in_obj, **kw):
        if hasattr(in_obj, 'cone'):
            in_obj=in_obj.cone
        if 'outfile' in kw and self.outdir:
            outfile = kw['outfile']
            kw['outfile']=os.path.join(self.outdir, outfile)
        if 'dollar_sign_vars' in kw:
            if not 'fn' in kw.get('dollar_sign_vars',{}):
                kw['dollar_sign_vars']=dict(**kw.get('dollar_sign_vars',{}), **dict(fn=self.fn))
        else:
            kw['dollar_sign_vars']=dict(fn=self.fn)
        self.renderer.render(in_obj, **kw)
        