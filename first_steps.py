from time import sleep


def extract():
    print("This is the extract")
    sleep(2)


def transform():
    print("This is the transform")
    sleep(2)


def load():
    print("This is the load")
    sleep(2)


def pipeline():
    extract()
    transform()
    load()
    print("Pipeline completed")


if __name__ == "__main__":
    while True:
        pipeline()
        sleep(60)
