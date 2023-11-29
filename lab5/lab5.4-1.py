kmitl_list = ['*****',
              '*MM**',
              '*KIK*',
              '**T**',
              '**L**']
kmitl_count = 0


def findarea(rowbefor, positionbefor, rownow, positionnow):
    check = False
    if (rowbefor-rownow)**2 < 2:
        if (positionbefor-positionnow)**2 < 2:
            check = True
    return check


for krow in range(5):
    if 'K' in kmitl_list[krow]:
        for kletter in range(5):
            if kmitl_list[krow][kletter] == 'K':
                for mrow in range(5):
                    if 'M' in kmitl_list[mrow]:
                        for mletter in range(5):
                            if kmitl_list[mrow][mletter] == 'M' and findarea(krow, kletter, mrow, mletter):
                                for irow in range(5):
                                    if 'I' in kmitl_list[irow]:
                                        for iletter in range(5):
                                            if kmitl_list[irow][iletter] == 'I' and findarea(mrow, mletter, irow, iletter):
                                                for trow in range(5):
                                                    if 'T' in kmitl_list[trow]:
                                                        for tletter in range(5):
                                                            if kmitl_list[trow][tletter] == 'T' and findarea(irow, iletter, trow, tletter):
                                                                for lrow in range(5):
                                                                    if 'L' in kmitl_list[lrow]:
                                                                        for lletter in range(5):
                                                                            if kmitl_list[lrow][lletter] == 'L' and findarea(trow, tletter, lrow, lletter):
                                                                                kmitl_count += 1
                                                                                print(
                                                                                    f"K {krow+1,kletter+1} M {mrow+1,mletter+1} I {irow+1,iletter+1} T {trow+1,tletter+1},L {lrow+1,lletter+1}")
print(f"kmitl Count = {kmitl_count}")
