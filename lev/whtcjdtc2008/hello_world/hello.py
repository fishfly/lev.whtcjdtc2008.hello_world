"""
我的第一个潮汐平台工具
Homepage: -
GitHub: -
Type: IMAGE-BASED
Version: v1.0.0
"""
import levrt
from levrt import Cr, ctx, remote, annot
from levrt.annot.cats import Attck, BlackArch

@annot.meta(
    desc="Hello",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def hello(name: str = "world") -> Cr:
    """
    Hello World的唯一工具模式
    ```
    await hello("world")
    ```
    """
    @levrt.remote
    def entry():
        ctx.set(msg=f"Hello, {name}!")

    return Cr("alpine:latest", entry=entry())

@annot.meta(
    desc="Hi",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def hi(name: str = "world") -> Cr:
    """
    Hello World的第二种工具模式
    ```
    await hi("world")
    ```
    """
    @levrt.remote
    def entry():
        ctx.set(msg=f"Hi, {name}!")

    return Cr("alpine:latest", entry=entry())

@annot.meta(
    desc="Exp",
    params=[annot.Param("name", "person name")],
    cats=[Attck.Reconnaissance],
)
def exp(length: int = 9) -> Cr:
    """
    Hello World的第三种工具模式
    ```
    await exp(9)
    ```
    """
    @levrt.remote
    def entry():
        import sys, pdb
        sys.path.append('/usr/local/lib/python3.10/site-packages')
        import numpy,logging
        logging.basicConfig()
        logger = logging.getLogger("lev")
        logger.setLevel(logging.DEBUG)
        pdb.set_trace()
        logger.debug("[lev app - hello world] log from container")
        res = round(numpy.e, length)
        ctx.set(msg=res)

    return Cr("86cf12987", entry=entry())

__lev__ = annot.meta([hello, hi, exp],
                     desc = "hello world", # name of tool
                     cats = {
                        Attck: [Attck.Reconnaissance] # ATT&CK
                     })
