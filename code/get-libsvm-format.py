import sys

FEAT_SELECTED = [i.strip() for i in sys.argv[1].split(',')]
LABEL = sys.argv[2]

print >> sys.stderr, "selecting these feats:\n" + '\n'.join(FEAT_SELECTED)
print >> sys.stderr, "label:" + LABEL
print >> sys.stderr

lineno = 0
total = 0
list_feat = None
list_inst = []
for line in sys.stdin:
    line = line.rstrip()
    lineno += 1
    if lineno == 1:
        list_feat = line.split('\t')
    else:
        list_inst.append(line.split('\t'))

list_ind_selected = [ind for ind, feat in enumerate(list_feat) if feat in FEAT_SELECTED]
ind_label = list_feat.index(LABEL)

print >> sys.stderr, "total number of instances:", len(list_inst)

print >> sys.stderr, "output libsvm-style"

for inst in list_inst:
    print inst[ind_label], ' '.join(str(ind_selected+1)+":"+inst[ind_selected] for ind_selected in list_ind_selected)

print >> sys.stderr, "done"
