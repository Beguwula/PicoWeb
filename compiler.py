def compile(infile, outfile):
    infolder = "./text/"
    outfolder = "./html/"
    with open(infolder + infile, "r") as text_file:
        text = text_file.read()
    html_text = text.replace('\n', '<br>')
    html = f"<!DOCTYPE html><html><head></head><body>{html_text}</body></html>"
    if outfile != None:
        with open(outfolder + outfile, "w") as html_file:
            html_file.write(html)
    else:
        return html

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input")
    parser.add_argument('-o', "--output")

    args = parser.parse_args()
    infile = args.input
    outfile = args.output
    print(f"Input: {infile}")
    print(f"Output: {outfile}")

    compile(infile, outfile)
