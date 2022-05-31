import levrt
from lev.whtcjdtc2008.hello_world import hello

async def main():
    doc = await hello.exp(9)
    data = await doc.get()
    print(data["msg"])


if __name__ == "__main__":
    import logging
    logging.basicConfig()
    logger = logging.getLogger("lev")
    logger.setLevel(logging.DEBUG)
    logger.debug("[lev app - hello world] debug test")
    levrt.run(main())
