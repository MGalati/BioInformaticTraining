#!/usr/bin/python
# http://rosalind.info/problems/gc/


def dict_seq(seqs):
    dict = {}
    id = ''
    seq = ''

    for line in seqs:
        line = line.strip()
        if line[0] == '>':  # Manage sequences ids
            seq = ''
            id = line[1:]
        else:
            seq = seq + line  # Manage seq over multiple lines
            seq = seq.upper()
            dict[id] = seq
    return dict


def compt_gc(dict):
    dict_gc = {}
    for id, seq in dict.items():
        gc = 0
        content = 0
        number_bases = 0
        for bases in seq:
            number_bases += 1
            if bases == 'G' or bases == 'C':
                gc += 1
            elif bases == 'A' or bases == 'T':
                pass
            else:
                print("NOT A BIOLOGICAL SEQ")
                exit(1)
        content = (gc / number_bases) * 100
        dict_gc[content] = id
    return dict_gc


def highest_gc(dict_gc):
    highest = 0
    for key in dict_gc.keys():
        if key > highest:
            highest = key
        else:
            pass
    print('%s\n%.6f' % (dict_gc[highest], highest))


def main():
    f = open('G:\\Téléchargement\\rosalind_gc.txt', 'r')
    seqs = f.read().splitlines()
    dict = dict_seq(seqs)
    dict_gc = compt_gc(dict)
    print(highest_gc(dict_gc))


if __name__ == '__main__':
    main()
