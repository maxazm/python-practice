with open("writing_file.txt", mode="w") as f:
    # truncatedされる：byte=0に切り詰める
    f.write("You can write contents here\n hello")
    f.write("new write() doesn't break row")

    print("You can add a new row using 'file' parameter", file=f)
    print("You can add a new row using 'file' parameter", file=f)
