import csv


def main():
    ifile = open("/Users/wyatt.tall/Downloads/input.csv", "rU")
    reader = csv.reader(ifile)

    rownum = 0
    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0

            for col in row:
                print ' % -8s: % s' % (header[colnum], col)
                colnum += 1

        rownum += 1

    ifile.close()


if __name__ == '__main__': main()
