from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    assert shorten("glue")== 'gl'
    assert shorten("carabiner")== 'crbnr'
    assert shorten("FalSe")=="FlS"
    assert shorten("DENMARK")=="DNMRK"
    assert shorten("jigsaw2")=="jgsw2"
    assert shorten("Caliber.")=="Clbr."



if __name__ == "__main__":
    main()
